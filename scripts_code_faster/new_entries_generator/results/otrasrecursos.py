from app.interface import db
from app.domain.models import OtrasRecursos

def new_entry_otrasrecursos(form:dict, id_person):
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
    if not 'tipo_recurso' in form or form['tipo_recurso'].strip() in db.empty_options:
        error.append('tipo_recurso')
    if not 'programa' in form or form['programa'].strip() in db.empty_options:
        error.append('programa')
    if not 'nombre' in form or form['nombre'].strip() in db.empty_options:
        error.append('nombre')
    if not 'impacto' in form or form['impacto'].strip() in db.empty_options:
        error.append('impacto')
    if not 'fecha' in form or form['fecha'].strip() in db.empty_options:
        error.append('fecha')
    if not 'ofertado_por' in form or form['ofertado_por'].strip() in db.empty_options:
        error.append('ofertado_por')
    if not 'finalizado' in form or form['finalizado'].strip() in db.empty_options:
        error.append('finalizado')
    if not 'alcance' in form or form['alcance'].strip() in db.empty_options:
        error.append('alcance')
    if not 'period_spam' in form or form['period_spam'].strip() in db.empty_options:
        error.append('period_spam')
    return error

def _clean_data_form(form):
    if not 'detalles' in form or form['detalles'].strip() in db.empty_options:
        form['detalles'] = ""
    if not 'observaciones' in form or form['observaciones'].strip() in db.empty_options:
        form['observaciones'] = ""

def _create_entry(form:dict, id_person):
    entry = OtrasRecursos(
        id_person = id_person,
        tipo_recurso = form['tipo_recurso'],
        programa = form['programa'],
        nombre = form['nombre'],
        impacto = form['impacto'],
        fecha = form['fecha'],
        detalles = form['detalles'],
        ofertado_por = form['ofertado_por'],
        finalizado = form['finalizado'],
        alcance = form['alcance'],
        observaciones = form['observaciones'],
        period_spam = form['period_spam']
    )
    db.session.add(entry)
    db.session.commit()
    db.session.close()
