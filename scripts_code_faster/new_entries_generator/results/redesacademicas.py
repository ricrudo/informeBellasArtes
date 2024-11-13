from app.interface import db
from app.domain.models import RedesAcademicas

def new_entry_redesacademicas(form:dict, id_person):
    response = _check_content(form)
    if response:
        return f'faltan datos {response}']
    if not db.is_real_person(id_person):
        return 'No existe persona con el id indicado'
    _clean_data_form(form)
    _create_entry(form, id_person)
    return 'ok'

def _check_content(form:dict, id_person):
    error = []
    if not id_person or id_person.strip() in db.empty_options:
        error.append('id_person')
    if not 'name_red' in form or form['name_red'].strip() in db.empty_options:
        error.append('name_red')
    if not 'link' in form or form['link'].strip() in db.empty_options:
        error.append('link')
    if not 'period_spam' in form or form['period_spam'].strip() in db.empty_options:
        error.append('period_spam')
    return error

def _clean_data_form(form):
    if not 'update_date' in form or form['update_date'].strip() in db.empty_options:
        form['update_date'] = ""

def _create_entry(form:dict, id_person):
    entry = RedesAcademicas(
        id_person = id_person,
        name_red = form['name_red'],
        link = form['link'],
        update_date = form['update_date'],
        period_spam = form['period_spam']
    )
    db.session.add(entry)
    db.session.commit()
    db.session.close()
