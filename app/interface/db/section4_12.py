from app.interface import db
from app.interface.db import db_manager
from app.domain.models import CoordSemilleros

import json

'''
{"semillero": null, "total_integrantes": null, "nuevos_integrantes": null, "grupo": null, "programa": null, "update_sia": null}
'''


def new_entry_user(initform:dict):
    #if not db.is_real_person(id_person):
    #    return 'No existe persona con el id indicado'
    index_used = []
    error = []
    for index_entry, content in initform['section4_12'].items():
        if index_entry == 'activateQuestionsection4_12':
            continue
        index_used.append(int(index_entry))
        if len(content) != 6:
            error.append(f'Error: se han enviado {len(content)} datos. Se esperaban 6 datos.')
            continue
        if not all([x in content for x in (['semillero', 'total_integrantes', 'nuevos_integrantes', 'grupo', 'programa', 'update_sia'])]):
            error.append(f'Los keys no corresponden a los que recibe la base de datos.')
            continue
        
        content['user'] = initform['user']
        content['period_spam'] = initform['period_spam']
        content['index_entry'] = int(index_entry)
        _send_to_DB(content)
    db_manager._delete_entries(index_used, initform['user'], initform['period_spam'], CoordSemilleros)
    db.session.close()
    if error:
        return error
    return 'ok'

def _create_entry(form:dict):
    entry = CoordSemilleros(
        id_person = form['user'],
        index_entry = form['index_entry'],
        semillero = form['semillero'],
        total_integrantes = form['total_integrantes'],
        nuevos_integrantes = form['nuevos_integrantes'],
        grupo = form['grupo'],
        programa = form['programa'],
        update_sia = form['update_sia'],
        period_spam = form['period_spam']
    )
    db.session.add(entry)
    db.session.commit()

def _send_to_DB(content:dict):
    entry = db_manager._check_entry(content, CoordSemilleros)
    if entry:
        db_manager._update_entry(entry, content)
    else:
        _create_entry(content)

