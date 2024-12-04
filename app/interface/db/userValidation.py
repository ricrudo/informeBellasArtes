from werkzeug.security import generate_password_hash, check_password_hash

from string import ascii_letters, digits
import random
import threading
from datetime import datetime, timedelta, timezone

from app.interface import db
from app.domain.models import Login, Person

from app.interface.email import email_sender

from pathlib import Path

import logging

# Configuración para guardar los logs en un archivo
logging.basicConfig(
    filename='mi_log.log',         # Nombre del archivo de logs
    level=logging.INFO,             # Nivel mínimo de registro
    format='%(asctime)s - %(levelname)s - %(message)s'  # Formato del log
)


def login(data):
    email = data.get('username').lower().strip()
    password = data.get('password')
    user = db.session.query(Login).filter_by(email=email).first()
    if  not user:
        return "usuario_no_registrado"
    elif not check_password_hash(user.password, password):
        return "wrong_access_data"
    elif user and check_password_hash(user.password, password):
        if user.temp_pass:
            if not checkExpirationTempPass(user):
                return "timeLimit_superado"
            return 'change_password'
        return 'acceso_aprobado'


def recoveryPassword(data, app):
    email = data.get('username').lower().strip()
    logging.info(f'Intentando crear tempPass para {email}')

    person = db.session.query(Person).filter_by(email=email).first()
    if not person:
        return "usuario_no_registrado"
    user = db.session.query(Login).filter_by(email=email).first()
    tempPass = "".join(random.choices(ascii_letters + digits, k=random.randrange(8,12)))
    if not user:
        setTempPass(person, tempPass)
    else:
        updatePassword(user, tempPass, True)
    email_sender.sendTemporalPass(email, tempPass, app)
    #email_thread = threading.Thread(target=email_sender.sendTemporalPass, args=(email, tempPass, app))
    #email_thread.start()
    destino = Path.cwd() / 'temp.txt'
    destino.write_text(tempPass)
    return "Correo_segundo_plano"


def setTempPass(person, password):
    entry = Login(
        id_person = person.id,
        email = person.email,
        password = generate_password_hash(password),
        temp_pass = True,
    )
    db.session.add(entry)
    db.session.commit()
    db.session.close()


def setPassword(data, email):
    password = data.get('password')
    user = db.session.query(Login).filter_by(email=email).first()
    if not user:
        return "usuario_no_registrado"
    updatePassword(user, password)
    return "ok_change_password"


def updatePassword(entry, password, temp_pass=False):
    entry.password = generate_password_hash(password)
    entry.temp_pass = temp_pass
    db.session.commit()
    db.session.close()


def checkExpirationTempPass(user):
    if user.fecha_update:
        if not user.fecha_update.tzinfo:
            user_date = user.fecha_update.replace(tzinfo=timezone.utc)
            now = datetime.now(timezone.utc)
        else:
            user_date = user.fecha_update
            now = datetime.now(user.fecha_update.tzinfo)
    else:
        if not user.date_creation.tzinfo:
            user_date = user.date_creation.replace(tzinfo=timezone.utc)
            now = datetime.now(timezone.utc)
        else:
            user_date = user.date_creation
            now = datetime.now(user.date_creation.tzinfo)
    time_difference = now - user_date
    return time_difference <= timedelta(minutes=15)
