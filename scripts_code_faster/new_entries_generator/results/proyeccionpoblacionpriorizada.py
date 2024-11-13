from app.interface import db
from app.domain.models import ProyeccionPoblacionPriorizada

def new_entry_proyeccionpoblacionpriorizada(form:dict, id_person):
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
    if not 'nombre_proyecto' in form or form['nombre_proyecto'].strip() in db.empty_options:
        error.append('nombre_proyecto')
    if not 'fecha_inicio' in form or form['fecha_inicio'].strip() in db.empty_options:
        error.append('fecha_inicio')
    if not 'beneficiarios' in form or form['beneficiarios'].strip() in db.empty_options:
        error.append('beneficiarios')
    if not 'period_spam' in form or form['period_spam'].strip() in db.empty_options:
        error.append('period_spam')
    return error

def _clean_data_form(form):
    if not 'participantes' in form or form['participantes'].strip() in db.empty_options:
        form['participantes'] = ""

def _create_entry(form:dict, id_person):
    entry = ProyeccionPoblacionPriorizada(
        id_person = id_person,
        nombre_proyecto = form['nombre_proyecto'],
        fecha_inicio = form['fecha_inicio'],
        beneficiarios = form['beneficiarios'],
        participantes = form['participantes'],
        period_spam = form['period_spam']
    )
    db.session.add(entry)
    db.session.commit()
    db.session.close()
