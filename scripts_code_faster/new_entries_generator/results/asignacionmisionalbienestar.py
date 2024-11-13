from app.interface import db
from app.domain.models import AsignacionMisionalBienestar

def new_entry_asignacionmisionalbienestar(form:dict, id_person):
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
    if not 'representante_misional' in form or form['representante_misional'].strip() in db.empty_options:
        error.append('representante_misional')
    if not 'tutor_rendimiento' in form or form['tutor_rendimiento'].strip() in db.empty_options:
        error.append('tutor_rendimiento')
    if not 'tutor_SAT' in form or form['tutor_SAT'].strip() in db.empty_options:
        error.append('tutor_SAT')
    if not 'coordinador' in form or form['coordinador'].strip() in db.empty_options:
        error.append('coordinador')
    if not 'period_spam' in form or form['period_spam'].strip() in db.empty_options:
        error.append('period_spam')
    return error

def _clean_data_form(form):

def _create_entry(form:dict, id_person):
    entry = AsignacionMisionalBienestar(
        id_person = id_person,
        representante_misional = form['representante_misional'],
        tutor_rendimiento = form['tutor_rendimiento'],
        tutor_SAT = form['tutor_SAT'],
        coordinador = form['coordinador'],
        period_spam = form['period_spam']
    )
    db.session.add(entry)
    db.session.commit()
    db.session.close()
