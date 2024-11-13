from app.interface import db
from app.domain.models import Part_ProcesosCurriculares

def new_entry_part_procesoscurriculares(form:dict, id_person):
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
    if not 'name_proceso' in form or form['name_proceso'].strip() in db.empty_options:
        error.append('name_proceso')
    if not 'period_spam' in form or form['period_spam'].strip() in db.empty_options:
        error.append('period_spam')
    return error

def _clean_data_form(form):
    if not 'status_done' in form or form['status_done'].strip() in db.empty_options:
        form['status_done'] = False
    if not 'program_misional' in form or form['program_misional'].strip() in db.empty_options:
        form['program_misional'] = ""
    if not 'observaciones' in form or form['observaciones'].strip() in db.empty_options:
        form['observaciones'] = ""
    if not 'path_files' in form or form['path_files'].strip() in db.empty_options:
        form['path_files'] = ""

def _create_entry(form:dict, id_person):
    entry = Part_ProcesosCurriculares(
        id_person = id_person,
        name_proceso = form['name_proceso'],
        status_done = form['status_done'],
        program_misional = form['program_misional'],
        observaciones = form['observaciones'],
        path_files = form['path_files'],
        period_spam = form['period_spam']
    )
    db.session.add(entry)
    db.session.commit()
    db.session.close()
