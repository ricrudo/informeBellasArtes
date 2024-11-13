from app.interface import db
from app.domain.models import DireccionTesis

def new_entry_direcciontesis(form:dict, id_person):
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
    if not 'titulo' in form or form['titulo'].strip() in db.empty_options:
        error.append('titulo')
    if not 'estudiante' in form or form['estudiante'].strip() in db.empty_options:
        error.append('estudiante')
    if not 'nivel_formacion' in form or form['nivel_formacion'].strip() in db.empty_options:
        error.append('nivel_formacion')
    if not 'programa' in form or form['programa'].strip() in db.empty_options:
        error.append('programa')
    if not 'institucion' in form or form['institucion'].strip() in db.empty_options:
        error.append('institucion')
    if not 'status' in form or form['status'].strip() in db.empty_options:
        error.append('status')
    if not 'period_spam' in form or form['period_spam'].strip() in db.empty_options:
        error.append('period_spam')
    return error

def _clean_data_form(form):

def _create_entry(form:dict, id_person):
    entry = DireccionTesis(
        id_person = id_person,
        titulo = form['titulo'],
        estudiante = form['estudiante'],
        nivel_formacion = form['nivel_formacion'],
        programa = form['programa'],
        institucion = form['institucion'],
        status = form['status'],
        period_spam = form['period_spam']
    )
    db.session.add(entry)
    db.session.commit()
    db.session.close()
