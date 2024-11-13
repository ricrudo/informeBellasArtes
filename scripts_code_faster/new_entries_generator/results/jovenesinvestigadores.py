from app.interface import db
from app.domain.models import JovenesInvestigadores

def new_entry_jovenesinvestigadores(form:dict, id_person):
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
    if not 'convocatoria' in form or form['convocatoria'].strip() in db.empty_options:
        error.append('convocatoria')
    if not 'estudiantes' in form or form['estudiantes'].strip() in db.empty_options:
        error.append('estudiantes')
    if not 'programa' in form or form['programa'].strip() in db.empty_options:
        error.append('programa')
    if not 'period_spam' in form or form['period_spam'].strip() in db.empty_options:
        error.append('period_spam')
    return error

def _clean_data_form(form):

def _create_entry(form:dict, id_person):
    entry = JovenesInvestigadores(
        id_person = id_person,
        convocatoria = form['convocatoria'],
        estudiantes = form['estudiantes'],
        programa = form['programa'],
        period_spam = form['period_spam']
    )
    db.session.add(entry)
    db.session.commit()
    db.session.close()
