from app.interface import db
from app.domain.models import ConvocatoriasSemilleros

def new_entry_convocatoriassemilleros(form:dict, id_person):
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
    if not 'semillero' in form or form['semillero'].strip() in db.empty_options:
        error.append('semillero')
    if not 'tipo_convovatoria' in form or form['tipo_convovatoria'].strip() in db.empty_options:
        error.append('tipo_convovatoria')
    if not 'nombre' in form or form['nombre'].strip() in db.empty_options:
        error.append('nombre')
    if not 'proyecto' in form or form['proyecto'].strip() in db.empty_options:
        error.append('proyecto')
    if not 'participantes' in form or form['participantes'].strip() in db.empty_options:
        error.append('participantes')
    if not 'fecha' in form or form['fecha'].strip() in db.empty_options:
        error.append('fecha')
    if not 'period_spam' in form or form['period_spam'].strip() in db.empty_options:
        error.append('period_spam')
    return error

def _clean_data_form(form):
    if not 'observaciones' in form or form['observaciones'].strip() in db.empty_options:
        form['observaciones'] = ""

def _create_entry(form:dict, id_person):
    entry = ConvocatoriasSemilleros(
        id_person = id_person,
        semillero = form['semillero'],
        tipo_convovatoria = form['tipo_convovatoria'],
        nombre = form['nombre'],
        proyecto = form['proyecto'],
        participantes = form['participantes'],
        fecha = form['fecha'],
        observaciones = form['observaciones'],
        period_spam = form['period_spam']
    )
    db.session.add(entry)
    db.session.commit()
    db.session.close()
