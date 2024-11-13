from app.interface import db
from app.domain.models import Person

import json

'''
{nombre: null, facultad: null, formacion: null, programa: [""], period_spam: null}
'''


def new_entry_user(initform:dict):
    #if not db.is_real_person(id_person):
    #    return 'No existe persona con el id indicado'
    index_used = []
    error = []
    content = {}
    for index_entry, form in initform['section1_1'].items():
        index_used.append(int(index_entry))
        if len(form) != 4:
            error.append(f'Error: se han enviado {len(form)} datos. Se esperaban 5 datos.')
            continue
        if not all([x in form for x in (['name', 'facultad', 'formacion', 'programas'])]):
            error.append(f'Los keys no corresponden a los que recibe la base de datos.')
            continue

        content['formacion'] = form['formacion']
        content['user'] = initform['user']
        content['period_spam'] = initform['period_spam']
        if error:
            return error
        _update_entry(content)
        return 'ok'

def _update_entry(content:dict):
    result = db.session.query(Person).filter(
        Person.id == content['user'],
    ).first()  # `first()` devuelve el primer resultado o None si no hay coincidencias
    if getattr(result, 'formacion') != content['formacion']:
        setattr(result, 'formacion', content['formacion'])
        db.session.commit()
    db.session.close()


######adminAccess#####

def new_entry_admin(initform:dict):
    error = []
    if len(initform) != 4:
        error.append(f'Error: se han enviado {len(initform)} datos. Se esperaban 4 datos.')
    if not all([x in initform for x in (['name', 'admin_role', 'facultad', 'email'])]):
        error.append(f'Los keys no corresponden a los que recibe la base de datos.')
    if not error:
        _delete_old_entry(initform['email'])
        _create_entry(initform)
        id_person = _getIdPerson(initform['email'])
        print(id_person)
        db.session.close()
        return id_person

def _create_entry(form:dict):
    entry = Person(
        name = form['name'],
        admin_role = form['admin_role'],
        facultad = form['facultad'],
        email = form['email'],
    )
    db.session.add(entry)
    db.session.commit()

def _getIdPerson(email:str):
    result = db.session.query(Person).filter(Person.email == email).first()
    return result.id

def _delete_old_entry(email:str):
    result = db.session.query(Person).filter(Person.email == email).all()
    if result:
        for entry in result:
            db.session.delete(entry)
        db.session.commit()

