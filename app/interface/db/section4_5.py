from app.interface import db
from app.interface.db import db_manager, clean_data
from app.domain.models import PublicacionArticulos

import json

'''
{"titulo": null, "autores": [""], "revista": null, "link": null, "fecha": null, "issn": null, "index_revista": null}
'''


def new_entry_user(initform:dict):
    #if not db.is_real_person(id_person):
    #    return 'No existe persona con el id indicado'
    index_used = []
    error = []
    for index_entry, content in initform['section4_5'].items():
        if index_entry == 'activateQuestionsection4_5':
            continue
        index_used.append(int(index_entry))
        if len(content) != 7:
            error.append(f'Error: se han enviado {len(content)} datos. Se esperaban 7 datos.')
            continue
        if not all([x in content for x in (['titulo', 'autores', 'revista', 'link', 'fecha', 'issn', 'index_revista'])]):
            error.append(f'Los keys no corresponden a los que recibe la base de datos.')
            continue
        autores = clean_data.getActualParticipant(content['autores'])
        content['autores'] = json.dumps(autores)
        content['user'] = initform['user']
        content['period_spam'] = initform['period_spam']
        content['index_entry'] = int(index_entry)
        _send_to_DB(content)
    db_manager._delete_entries(index_used, initform['user'], initform['period_spam'], PublicacionArticulos)
    db.session.close()
    if error:
        return error
    return 'ok'

def _create_entry(form:dict):
    entry = PublicacionArticulos(
        id_person = form['user'],
        index_entry = form['index_entry'],
        titulo = form['titulo'],
        autores = form['autores'],
        revista = form['revista'],
        link = form['link'],
        fecha = form['fecha'],
        issn = form['issn'],
        index_revista = form['index_revista'],
        period_spam = form['period_spam']
    )
    db.session.add(entry)
    db.session.commit()

def _send_to_DB(content:dict):
    entry = db_manager._check_entry(content, PublicacionArticulos)
    if entry:
        db_manager._update_entry(entry, content)
    else:
        _create_entry(content)

