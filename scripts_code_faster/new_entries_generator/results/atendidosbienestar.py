from app.interface import db
from app.domain.models import AtendidosBienestar

def new_entry_atendidosbienestar(form:dict, id_person):
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
    if not 'tipo_atencion' in form or form['tipo_atencion'].strip() in db.empty_options:
        error.append('tipo_atencion')
    if not 'nombre_persona' in form or form['nombre_persona'].strip() in db.empty_options:
        error.append('nombre_persona')
    if not 'period_spam' in form or form['period_spam'].strip() in db.empty_options:
        error.append('period_spam')
    return error

def _clean_data_form(form):
    if not 'superado' in form or form['superado'].strip() in db.empty_options:
        form['superado'] = False
    if not 'detalles' in form or form['detalles'].strip() in db.empty_options:
        form['detalles'] = ""
    if not 'remision' in form or form['remision'].strip() in db.empty_options:
        form['remision'] = False
    if not 'estrategias' in form or form['estrategias'].strip() in db.empty_options:
        form['estrategias'] = ""
    if not 'observaciones' in form or form['observaciones'].strip() in db.empty_options:
        form['observaciones'] = ""

def _create_entry(form:dict, id_person):
    entry = AtendidosBienestar(
        id_person = id_person,
        tipo_atencion = form['tipo_atencion'],
        nombre_persona = form['nombre_persona'],
        superado = form['superado'],
        detalles = form['detalles'],
        remision = form['remision'],
        estrategias = form['estrategias'],
        observaciones = form['observaciones'],
        period_spam = form['period_spam']
    )
    db.session.add(entry)
    db.session.commit()
    db.session.close()
