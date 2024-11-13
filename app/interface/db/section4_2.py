from app.interface import db
from app.interface.db import db_manager
from app.domain.models import RedesAcademicas

import json

'''
    0: {status_cvlac: null, link_cvlac: null, update_cvlac: null},
    1: {status_google_scholar: null, link_google_scholar: null, update_google_scholar: null},
    2: {status_researchgate: null, link_researchgate: null, update_researchgate: null},
    3: {status_orcid: null, link_orcid: null, update_orcid: null},
'''


def new_entry_user(initform:dict):
    #if not db.is_real_person(id_person):
    #    return 'No existe persona con el id indicado'
    index_used = []
    error = []
    for index_entry, form in initform['section4_2'].items():
        content = {}
        if len(form) != 3:
            error.append(f'Error: se han enviado {len(form)} datos. Se esperaban 3 datos.')
            continue
        keysForm = [x for x in form.keys() if 'status_' in x]
        if not keysForm:
            error.append(f'Los keys no corresponden a los que recibe la base de datos.')
            continue
        name_red = keysForm[0].replace('status_', '')

        if (index_entry == "0" and name_red != 'cvlac') or (index_entry == "1" and name_red != 'google_scholar') or (index_entry == "2" and name_red != 'researchgate') or (index_entry == "3" and name_red != 'orcid'):
            if not all([x in form for x in ('status_cvlac', 'link_cvlac', 'update_cvlac')]):
                error.append(f'Los keys no corresponden a los que recibe la base de datos.')
                continue
        if form[f'status_{name_red}'] not in ['si', 'no']:
            continue
        index_used.append(int(index_entry))
        content['name_red'] = name_red
        content['status'] = form[f'status_{name_red}']
        if form[f'status_{name_red}'] == 'si':
            content['link'] = form[f'link_{name_red}']
            content['update_date'] = form[f'update_{name_red}']
        else:
            content['link'] = None
            content['update_date'] = None
        content['user'] = initform['user']
        content['period_spam'] = initform['period_spam']
        content['index_entry'] = int(index_entry)
        _send_to_DB(content)
    db_manager._delete_entries(index_used, initform['user'], initform['period_spam'], RedesAcademicas)
    db.session.close()
    if error:
        return error
    return 'ok'

def _create_entry(form:dict):
    entry = RedesAcademicas(
        id_person = form['user'],
        index_entry = form['index_entry'],
        name_red = form['name_red'],
        status = form['status'],
        link = form['link'],
        update_date = form['update_date'],
        period_spam = form['period_spam']
    )
    db.session.add(entry)
    db.session.commit()

def _send_to_DB(content:dict):
    entry = db_manager._check_entry(content, RedesAcademicas)
    if entry:
        db_manager._update_entry(entry, content)
    else:
        _create_entry(content)

