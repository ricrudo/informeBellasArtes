from app.interface import db
from app.interface.db import section1_1, section2_1
from pathlib import Path
import json

PERIODO_SPAM = '2024-2'

def loadData(path):
    return json.loads(path.read_text())

def setEmail(dataPtas):
    for cedula, data in dataPtas.items():
        email = data['nombre'].replace(" ", "").lower() + '@mail.uniatlantico.edu.co'
        dataPtas[cedula]['email'] = email

def saveToDB(dataPtas):
    for cedula, data in dataPtas.items():
        if not data['email']:
            continue
        packagePerson = {
            'name': data['nombre'],
            'admin_role' : False,
            'facultad' : 'Bellas Artes',
            'email' : data['email']
        }
        id_person = section1_1.new_entry_admin(packagePerson)
        for index_entry, materia in enumerate(data['materias']):
            packageMateria = {
                'user': id_person,
                'index_entry': index_entry,
                'materia' : materia['materia'],
                'code' : materia['code'],
                'programa': None,
                'status_done': None,
                'observaciones': None,
                'contenidos_especiales': None,
                'motivos_cancel': None,
                'period_spam': PERIODO_SPAM

            }
            section2_1._create_entry(packageMateria)

def loadDB():
    path = Path.cwd() / 'parse_pta' / 'ptas_analizados.json'
    dataPtas = loadData(path)
    #setEmail(dataPtas)
    saveToDB(dataPtas)

def updateTable():
    from app.domain.models import JovenesInvestigadores
    JovenesInvestigadores.__table__.drop(db.engine)
    db.Base.metadata.create_all(db.engine, tables=[JovenesInvestigadores.__table__])

if __name__ == "__main__":
    loadDB()



