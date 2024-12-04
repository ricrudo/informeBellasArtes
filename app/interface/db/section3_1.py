from app.interface import db
from app.interface.db import db_manager, clean_data
from app.domain.models import Part_ProcesosCurriculares

import json

'''
{"status": null, "type": null, "misional": null , "programa": null, "observaciones": null}
'''


def new_entry_user(initform:dict):
    #if not db.is_real_person(id_person):
    #    return 'No existe persona con el id indicado'
    index_used = []
    content = {}
    error = []
    for index_entry, form in initform['section3_1'].items():
        breakpoint()
        index_used.append(int(index_entry))
        if len(form) != 5:
            error.append(f'Error: se han enviado {len(form)} datos. Se esperaban 5 datos.')
        proceso = ''
        for key, value in form.items():
            if '_' not in key:
                error.append('los keys no coinciden con los que recibe la base de datos')
                break
            if not proceso:
                proceso = key.split('_')[1]
                content['proceso'] = proceso
            content[key.replace(f'_{proceso}', '_')] = value
        if not all([x in content for x in ('proceso', 'status_', 'type_', 'misional_', 'programa_', 'observaciones_')]):
            error.append(f'Los keys no corresponden a los que recibe la base de datos.')
        content = clean_data.cleanFromStatus(content, 'status_', ['status_', 'proceso'])
        if content['type_'] == 'programa':
            content['misional_'] = None
        elif content['type_'] == 'misional':
            content['programa_'] = None
        elif content['type_'] is not None:
            error.append(f'El valor de type_ es erroneo.')
        if error:
            continue
        content['user'] = initform['user']
        content['period_spam'] = initform['period_spam']
        content['index_entry'] = int(index_entry)
        _send_to_DB(content)
    db_manager._delete_entries(index_used, initform['user'], initform['period_spam'], Part_ProcesosCurriculares)
    db.session.close()
    if error:
        return error
    return 'ok'

def _create_entry(form:dict):
    entry = Part_ProcesosCurriculares(
        id_person = form['user'],
        index_entry = form['index_entry'],
        proceso = form['proceso'],
        status_ = form['status_'],
        type_ = form['type_'],
        misional_ = form['misional_'],
        programa_ = form['programa_'],
        observaciones_ = form['observaciones_'],
        period_spam = form['period_spam']
    )
    db.session.add(entry)
    db.session.commit()

def _send_to_DB(content:dict):
    entry = db_manager._check_entry(content, Part_ProcesosCurriculares)
    if entry:
        db_manager._update_entry(entry, content)
    else:
        _create_entry(content)

