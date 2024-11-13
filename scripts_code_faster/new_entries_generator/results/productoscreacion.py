from app.interface import db
from app.domain.models import ProductosCreacion

def new_entry_productoscreacion(form:dict, id_person):
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
    if not 'nombre_producto' in form or form['nombre_producto'].strip() in db.empty_options:
        error.append('nombre_producto')
    if not 'institucion' in form or form['institucion'].strip() in db.empty_options:
        error.append('institucion')
    if not 'alcance' in form or form['alcance'].strip() in db.empty_options:
        error.append('alcance')
    if not 'fecha' in form or form['fecha'].strip() in db.empty_options:
        error.append('fecha')
    if not 'categoria' in form or form['categoria'].strip() in db.empty_options:
        error.append('categoria')
    if not 'period_spam' in form or form['period_spam'].strip() in db.empty_options:
        error.append('period_spam')
    return error

def _clean_data_form(form):
    if not 'link' in form or form['link'].strip() in db.empty_options:
        form['link'] = ""

def _create_entry(form:dict, id_person):
    entry = ProductosCreacion(
        id_person = id_person,
        tipo_producto = form['tipo_producto'],
        nombre_producto = form['nombre_producto'],
        institucion = form['institucion'],
        alcance = form['alcance'],
        fecha = form['fecha'],
        link = form['link'],
        categoria = form['categoria'],
        period_spam = form['period_spam']
    )
    db.session.add(entry)
    db.session.commit()
    db.session.close()
