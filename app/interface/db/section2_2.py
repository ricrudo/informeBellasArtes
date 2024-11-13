from app.interface import db
from app.interface.db import db_manager
from app.domain.models import MisionalDocenciaAdicionales

import json

'''
{"programa_add": null, "materia_add": null, "code_add": null, "observaciones_add": null, "contenidos_especiales_add": null}
'''


def new_entry_user(initform:dict):
    #if not db.is_real_person(id_person):
    #    return 'No existe persona con el id indicado'
    index_used = []
    error = []
    for index_entry, content in initform['section2_2'].items():
        if len(content) != 5:
            error.append(f'Error: se han enviado {len(content)} datos. Se esperaban 5 datos.')
            continue
        if not all([x in content for x in (['programa_add', 'materia_add', 'code_add', 'observaciones_add', 'contenidos_especiales_add'])]):
            error.append(f'Los keys no corresponden a los que recibe la base de datos.')
            continue
        if all([content[x] is None for x in (['programa_add', 'materia_add', 'code_add', 'observaciones_add', 'contenidos_especiales_add'])]):
            continue
        index_used.append(int(index_entry))
        content['user'] = initform['user']
        content['period_spam'] = initform['period_spam']
        content['index_entry'] = int(index_entry)
        _send_to_DB(content)
    db_manager._delete_entries(index_used, initform['user'], initform['period_spam'], MisionalDocenciaAdicionales)
    db.session.close()
    if error:
        return error
    return 'ok'

def _create_entry(form:dict):
    entry = MisionalDocenciaAdicionales(
        id_person = form['user'],
        index_entry = form['index_entry'],
        programa_add = form['programa_add'],
        materia_add = form['materia_add'],
        code_add = form['code_add'],
        observaciones_add = form['observaciones_add'],
        contenidos_especiales_add = form['contenidos_especiales_add'],
        period_spam = form['period_spam']
    )
    db.session.add(entry)
    db.session.commit()

def _send_to_DB(content:dict):
    entry = db_manager._check_entry(content, MisionalDocenciaAdicionales)
    if entry:
        db_manager._update_entry(entry, content)
    else:
        _create_entry(content)

