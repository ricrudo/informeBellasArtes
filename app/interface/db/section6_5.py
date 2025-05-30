from app.interface import db
from app.interface.db import db_manager
from app.domain.models import DesercionCasosGenerales

import json

'''
{"nombre_persona": null, "detalles": null, "estrategias": null, "observaciones": null}
'''


def new_entry_user(initform:dict):
    #if not db.is_real_person(id_person):
    #    return 'No existe persona con el id indicado'
    index_used = []
    error = []
    for index_entry, content in initform['section6_5'].items():
        if index_entry == 'activateQuestionsection6_5':
            continue
        index_used.append(int(index_entry))
        if len(content) != 4:
            error.append(f'Error: se han enviado {len(content)} datos. Se esperaban 4 datos.')
            continue
        if not all([x in content for x in (['nombre_persona', 'detalles', 'estrategias', 'observaciones'])]):
            error.append(f'Los keys no corresponden a los que recibe la base de datos.')
            continue
        
        content['user'] = initform['user']
        content['period_spam'] = initform['period_spam']
        content['index_entry'] = int(index_entry)
        _send_to_DB(content)
    db_manager._delete_entries(index_used, initform['user'], initform['period_spam'], DesercionCasosGenerales)
    db.session.close()
    if error:
        return error
    return 'ok'

def _create_entry(form:dict):
    entry = DesercionCasosGenerales(
        id_person = form['user'],
        index_entry = form['index_entry'],
        nombre_persona = form['nombre_persona'],
        detalles = form['detalles'],
        estrategias = form['estrategias'],
        observaciones = form['observaciones'],
        period_spam = form['period_spam']
    )
    db.session.add(entry)
    db.session.commit()

def _send_to_DB(content:dict):
    entry = db_manager._check_entry(content, DesercionCasosGenerales)
    if entry:
        db_manager._update_entry(entry, content)
    else:
        _create_entry(content)

