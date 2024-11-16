from app.interface import db
from app.interface.db import db_manager
from app.domain.models import MisionalDocenciaPTA

import json

'''
{"materia": null, "code": null, "programa": null, "status_done": null, "observaciones": null, "motivos_cancel": null, "bool_internacional": null, "internacional": null, "bool_tic": null, "tic": null}
'''


def new_entry_user(initform:dict):
    #if not db.is_real_person(id_person):
    #    return 'No existe persona con el id indicado'
    index_used = []
    error = []
    for index_entry, content in initform['section2_1'].items():
        index_used.append(int(index_entry))
        if len(content) != 10:
            error.append(f'Error: se han enviado {len(content)} datos. Se esperaban 7 datos.')
            continue
        if not all([x in content for x in (['materia', 'code', 'programa', 'status_done', 'observaciones', 'motivos_cancel', "bool_internacional", "internacional", "bool_tic", "tic"])]):
            error.append(f'Los keys no corresponden a los que recibe la base de datos.')
            continue
        if content['status_done'] == 'si':
            content['motivos_cancel'] = None
            if content['bool_internacional'] != 'si':
                content['internacional'] = None
            if content['bool_tic'] != 'si':
                content['tic'] = None
        elif content['status_done'] == 'no':
            content['observaciones'] = None
            content['bool_internacional'] = None
            content['internacional'] = None
            content['bool_tic'] = None
            content['tic'] = None
        else:
            content['motivos_cancel'] = None
            content['observaciones'] = None
            content['bool_internacional'] = None
            content['internacional'] = None
            content['bool_tic'] = None
            content['tic'] = None
        content['user'] = initform['user']
        content['period_spam'] = initform['period_spam']
        content['index_entry'] = int(index_entry)
        _send_to_DB(content)
    db.session.close()
    if error:
        return error
    return 'ok'

def _create_entry(form:dict):
    entry = MisionalDocenciaPTA(
        id_person = form['user'],
        index_entry = form['index_entry'],
        materia = form['materia'],
        code = form['code'],
        programa = form['programa'],
        status_done = form['status_done'],
        observaciones = form['observaciones'],
        bool_internacional = form['bool_internacional'],
        internacional = form['internacional'],
        bool_tic = form['bool_tic'], 
        tic = form['tic'],
        motivos_cancel = form['motivos_cancel'],
        period_spam = form['period_spam']
    )
    db.session.add(entry)
    db.session.commit()

def _send_to_DB(content:dict):
    entry = db_manager._check_entry(content, MisionalDocenciaPTA)
    if entry:
        db_manager._update_entry(entry, content)

