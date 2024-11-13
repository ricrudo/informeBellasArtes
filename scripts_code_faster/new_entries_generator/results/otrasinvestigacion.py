from app.interface import db
from app.domain.models import OtrasInvestigacion

def new_entry_otrasinvestigacion(form:dict, id_person):
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
    if not 'tipo_actividad' in form or form['tipo_actividad'].strip() in db.empty_options:
        error.append('tipo_actividad')
    if not 'nombre' in form or form['nombre'].strip() in db.empty_options:
        error.append('nombre')
    if not 'institucion' in form or form['institucion'].strip() in db.empty_options:
        error.append('institucion')
    if not 'actividades' in form or form['actividades'].strip() in db.empty_options:
        error.append('actividades')
    if not 'period_spam' in form or form['period_spam'].strip() in db.empty_options:
        error.append('period_spam')
    return error

def _clean_data_form(form):
    if not 'detalles' in form or form['detalles'].strip() in db.empty_options:
        form['detalles'] = ""
    if not 'observaciones' in form or form['observaciones'].strip() in db.empty_options:
        form['observaciones'] = ""

def _create_entry(form:dict, id_person):
    entry = OtrasInvestigacion(
        id_person = id_person,
        tipo_actividad = form['tipo_actividad'],
        nombre = form['nombre'],
        institucion = form['institucion'],
        actividades = form['actividades'],
        detalles = form['detalles'],
        observaciones = form['observaciones'],
        period_spam = form['period_spam']
    )
    db.session.add(entry)
    db.session.commit()
    db.session.close()
