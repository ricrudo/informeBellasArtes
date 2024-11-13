from app.interface import db
from app.domain.models import Patentes

def new_entry_patentes(form:dict, id_person):
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
    if not 'tipo_producto' in form or form['tipo_producto'].strip() in db.empty_options:
        error.append('tipo_producto')
    if not 'registro' in form or form['registro'].strip() in db.empty_options:
        error.append('registro')
    if not 'fecha' in form or form['fecha'].strip() in db.empty_options:
        error.append('fecha')
    if not 'period_spam' in form or form['period_spam'].strip() in db.empty_options:
        error.append('period_spam')
    return error

def _clean_data_form(form):

def _create_entry(form:dict, id_person):
    entry = Patentes(
        id_person = id_person,
        tipo_producto = form['tipo_producto'],
        registro = form['registro'],
        fecha = form['fecha'],
        period_spam = form['period_spam']
    )
    db.session.add(entry)
    db.session.commit()
    db.session.close()
