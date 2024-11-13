from app.interface import db
from app.interface.db import db_manager
from app.domain.models import ConveniosInterinstitucionales

import json

'''
{"convenio": null, "producto": null, "grupo": null, "impacto": null}
'''


def new_entry_user(initform:dict):
    #if not db.is_real_person(id_person):
    #    return 'No existe persona con el id indicado'
    index_used = []
    error = []
    for index_entry, content in initform['section4_8'].items():
        if index_entry == 'activateQuestionsection4_8':
            continue
        index_used.append(int(index_entry))
        if len(content) != 4:
            error.append(f'Error: se han enviado {len(content)} datos. Se esperaban 4 datos.')
            continue
        if not all([x in content for x in (['convenio', 'producto', 'grupo', 'impacto'])]):
            error.append(f'Los keys no corresponden a los que recibe la base de datos.')
            continue

        content['user'] = initform['user']
        content['period_spam'] = initform['period_spam']
        content['index_entry'] = int(index_entry)
        _send_to_DB(content)
    db_manager._delete_entries(index_used, initform['user'], initform['period_spam'], ConveniosInterinstitucionales)
    db.session.close()
    if error:
        return error
    return 'ok'

def _create_entry(form:dict):
    entry = ConveniosInterinstitucionales(
        id_person = form['user'],
        index_entry = form['index_entry'],
        convenio = form['convenio'],
        producto = form['producto'],
        grupo = form['grupo'],
        impacto = form['impacto'],
        period_spam = form['period_spam']
    )
    db.session.add(entry)
    db.session.commit()

def _send_to_DB(content:dict):
    entry = db_manager._check_entry(content, ConveniosInterinstitucionales)
    if entry:
        db_manager._update_entry(entry, content)
    else:
        _create_entry(content)

