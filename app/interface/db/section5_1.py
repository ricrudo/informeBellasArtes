from app.interface import db
from app.interface.db import db_manager
from app.domain.models import PropuestasEducacion

import json

'''
{"nombre": null, "tipo_propuesta": null, "fecha_inicio": null, "fecha_fin": null, "modalidad": null,"internacional": null,"bool_diferencial": null,"diferencial": null,"bool_entidad": null,"entidad_convenio": null}
'''


def new_entry_user(initform:dict):
    #if not db.is_real_person(id_person):
    #    return 'No existe persona con el id indicado'
    index_used = []
    error = []
    for index_entry, content in initform['section5_1'].items():
        if index_entry == 'activateQuestionsection5_1':
            continue
        index_used.append(int(index_entry))
        if len(content) != 10:
            error.append(f'Error: se han enviado {len(content)} datos. Se esperaban 10 datos.')
            continue
        if not all([x in content for x in (['nombre', 'tipo_propuesta', 'fecha_inicio', 'fecha_fin', 'modalidad', 'internacional', 'bool_diferencial', 'diferencial', 'bool_entidad', 'entidad'])]):
            error.append(f'Los keys no corresponden a los que recibe la base de datos.')
            continue
        
        content['user'] = initform['user']
        content['period_spam'] = initform['period_spam']
        content['index_entry'] = int(index_entry)
        _send_to_DB(content)
    db_manager._delete_entries(index_used, initform['user'], initform['period_spam'], PropuestasEducacion)
    db.session.close()
    if error:
        return error
    return 'ok'

def _create_entry(form:dict):
    entry = PropuestasEducacion(
        id_person = form['user'],
        index_entry = form['index_entry'],
        nombre = form['nombre'],
        tipo_propuesta = form['tipo_propuesta'],
        fecha_inicio = form['fecha_inicio'],
        fecha_fin = form['fecha_fin'],
        modalidad = form['modalidad'],
        internacional = form['internacional'],
        bool_diferencial = form['bool_diferencial'],
        diferencial = form['diferencial'],
        bool_entidad = form['bool_entidad'],
        entidad = form['entidad'],
        period_spam = form['period_spam']
    )
    db.session.add(entry)
    db.session.commit()

def _send_to_DB(content:dict):
    entry = db_manager._check_entry(content, PropuestasEducacion)
    if entry:
        db_manager._update_entry(entry, content)
    else:
        _create_entry(content)

