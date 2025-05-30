from app.interface import db
from app.interface.db import db_manager
from app.domain.models import **base_de_datos**

import json

'''
**template**
'''


def new_entry_gruposinvestigacion(initform:dict):
    #if not db.is_real_person(id_person):
    #    return 'No existe persona con el id indicado'
    index_used = []
    error = []
    for index_entry, content in initform['**name_section**'].items():
        index_used.append(int(index_entry))
        if len(content) != **len_template**:
            error.append(f'Error: se han enviado {len(content)} datos. Se esperaban **len_template** datos.')
            continue
        if not all([x in content for x in (**content_template**)]):
            error.append(f'Los keys no corresponden a los que recibe la base de datos.')
            continue
        **list_data**
        content['user'] = initform['user']
        content['period_spam'] = initform['period_spam']
        content['index_entry'] = int(index_entry)
        _send_to_DB(content)
    db_manager._delete_entries(index_used, initform['user'], initform['period_spam'], **base_de_datos**)
    db.session.close()
    if error:
        return error
    return 'ok'

def _create_entry(form:dict):
    entry = **base_de_datos**(
        id_person = form['user'],
        index_entry = form['index_entry'],
        **fields**
        period_spam = form['period_spam']
    )
    db.session.add(entry)
    db.session.commit()

def _send_to_DB(content:dict):
    entry = db_manager._check_entry(content, **base_de_datos**)
    if entry:
        db_manager._update_entry(entry, content)
    else:
        _create_entry(content)

