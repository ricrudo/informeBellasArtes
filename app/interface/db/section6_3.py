from app.interface import db
from app.interface.db import db_manager, filesManager
from app.domain.models import AtendidosSAT

import json

'''
{"nombre_persona": null, "superado": null, "remision": null, "observaciones": null, "name_file": null}
'''


def new_entry_user(initform:dict):
    #if not db.is_real_person(id_person):
    #    return 'No existe persona con el id indicado'
    index_used = []
    error = []
    for index_entry, content in initform['section6_3'].items():
        if index_entry == 'activateQuestionsection6_3':
            continue
        index_used.append(int(index_entry))
        if len(content) != 5:
            error.append(f'Error: se han enviado {len(content)} datos. Se esperaban 5 datos.')
            continue
        if not all([x in content for x in (['nombre_persona', 'superado', 'remision', 'observaciones', 'name_file'])]):
            error.append(f'Los keys no corresponden a los que recibe la base de datos.')
            continue
        
        content['name_file'] = filesManager.saveFile('section6_3', index_entry, initform)
        content['user'] = initform['user']
        content['period_spam'] = initform['period_spam']
        content['index_entry'] = int(index_entry)
        _send_to_DB(content)
    db_manager._delete_entries(index_used, initform['user'], initform['period_spam'], AtendidosSAT)
    db.session.close()
    if error:
        return error
    return 'ok'

def _create_entry(form:dict):
    entry = AtendidosSAT(
        id_person = form['user'],
        index_entry = form['index_entry'],
        nombre_persona = form['nombre_persona'],
        superado = form['superado'],
        remision = form['remision'],
        observaciones = form['observaciones'],
        name_file = form['name_file'],
        period_spam = form['period_spam']
    )
    db.session.add(entry)
    db.session.commit()

def _send_to_DB(content:dict):
    entry = db_manager._check_entry(content, AtendidosSAT)
    if entry:
        db_manager._update_entry(entry, content)
    else:
        _create_entry(content)

