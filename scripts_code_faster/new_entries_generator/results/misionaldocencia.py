from app.interface import db
from app.domain.models import MisionalDocencia

def new_entry_misionaldocencia(form:dict, id_person):
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
    if not 'materia' in form or form['materia'].strip() in db.empty_options:
        error.append('materia')
    if not 'code' in form or form['code'].strip() in db.empty_options:
        error.append('code')
    if not 'programa' in form or form['programa'].strip() in db.empty_options:
        error.append('programa')
    if not 'period_spam' in form or form['period_spam'].strip() in db.empty_options:
        error.append('period_spam')
    return error

def _clean_data_form(form):
    if not 'status_done' in form or form['status_done'].strip() in db.empty_options:
        form['status_done'] = False
    if not 'estudiantes_total' in form or form['estudiantes_total'].strip() in db.empty_options:
        form['estudiantes_total'] = ""
    if not 'estudiantes_pass' in form or form['estudiantes_pass'].strip() in db.empty_options:
        form['estudiantes_pass'] = ""
    if not 'observaciones' in form or form['observaciones'].strip() in db.empty_options:
        form['observaciones'] = ""
    if not 'contenidos_especiales' in form or form['contenidos_especiales'].strip() in db.empty_options:
        form['contenidos_especiales'] = ""
    if not 'motivos_cancel' in form or form['motivos_cancel'].strip() in db.empty_options:
        form['motivos_cancel'] = ""

def _create_entry(form:dict, id_person):
    entry = MisionalDocencia(
        id_person = id_person,
        materia = form['materia'],
        code = form['code'],
        programa = form['programa'],
        status_done = form['status_done'],
        estudiantes_total = form['estudiantes_total'],
        estudiantes_pass = form['estudiantes_pass'],
        observaciones = form['observaciones'],
        contenidos_especiales = form['contenidos_especiales'],
        motivos_cancel = form['motivos_cancel'],
        period_spam = form['period_spam']
    )
    db.session.add(entry)
    db.session.commit()
    db.session.close()
