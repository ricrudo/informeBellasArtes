from app.interface import db
from app.domain.models import PropuestasEducacion

def new_entry_propuestaseducacion(form:dict, id_person):
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
    if not 'nombre' in form or form['nombre'].strip() in db.empty_options:
        error.append('nombre')
    if not 'tipo_propuesta' in form or form['tipo_propuesta'].strip() in db.empty_options:
        error.append('tipo_propuesta')
    if not 'fecha_inicio' in form or form['fecha_inicio'].strip() in db.empty_options:
        error.append('fecha_inicio')
    if not 'fecha_fin' in form or form['fecha_fin'].strip() in db.empty_options:
        error.append('fecha_fin')
    if not 'modalidad' in form or form['modalidad'].strip() in db.empty_options:
        error.append('modalidad')
    if not 'internacional' in form or form['internacional'].strip() in db.empty_options:
        error.append('internacional')
    if not 'period_spam' in form or form['period_spam'].strip() in db.empty_options:
        error.append('period_spam')
    return error

def _clean_data_form(form):
    if not 'diferencial' in form or form['diferencial'].strip() in db.empty_options:
        form['diferencial'] = ""
    if not 'entidad_convenio' in form or form['entidad_convenio'].strip() in db.empty_options:
        form['entidad_convenio'] = ""

def _create_entry(form:dict, id_person):
    entry = PropuestasEducacion(
        id_person = id_person,
        nombre = form['nombre'],
        tipo_propuesta = form['tipo_propuesta'],
        fecha_inicio = form['fecha_inicio'],
        fecha_fin = form['fecha_fin'],
        modalidad = form['modalidad'],
        internacional = form['internacional'],
        diferencial = form['diferencial'],
        entidad_convenio = form['entidad_convenio'],
        period_spam = form['period_spam']
    )
    db.session.add(entry)
    db.session.commit()
    db.session.close()
