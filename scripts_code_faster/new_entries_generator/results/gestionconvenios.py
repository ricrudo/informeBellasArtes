from app.interface import db
from app.domain.models import GestionConvenios

def new_entry_gestionconvenios(form:dict, id_person):
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
    if not 'entidad' in form or form['entidad'].strip() in db.empty_options:
        error.append('entidad')
    if not 'actividades' in form or form['actividades'].strip() in db.empty_options:
        error.append('actividades')
    if not 'tipo_vinculo' in form or form['tipo_vinculo'].strip() in db.empty_options:
        error.append('tipo_vinculo')
    if not 'beneficiarios' in form or form['beneficiarios'].strip() in db.empty_options:
        error.append('beneficiarios')
    if not 'period_spam' in form or form['period_spam'].strip() in db.empty_options:
        error.append('period_spam')
    return error

def _clean_data_form(form):

def _create_entry(form:dict, id_person):
    entry = GestionConvenios(
        id_person = id_person,
        entidad = form['entidad'],
        actividades = form['actividades'],
        tipo_vinculo = form['tipo_vinculo'],
        beneficiarios = form['beneficiarios'],
        period_spam = form['period_spam']
    )
    db.session.add(entry)
    db.session.commit()
    db.session.close()
