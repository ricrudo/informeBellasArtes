from app.interface import db
from app.domain.models import MovilidadEstudiantesSemilleros

def new_entry_movilidadestudiantessemilleros(form:dict, id_person):
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
    if not 'evento' in form or form['evento'].strip() in db.empty_options:
        error.append('evento')
    if not 'proyecto' in form or form['proyecto'].strip() in db.empty_options:
        error.append('proyecto')
    if not 'lugar' in form or form['lugar'].strip() in db.empty_options:
        error.append('lugar')
    if not 'fecha' in form or form['fecha'].strip() in db.empty_options:
        error.append('fecha')
    if not 'estudiantes' in form or form['estudiantes'].strip() in db.empty_options:
        error.append('estudiantes')
    if not 'period_spam' in form or form['period_spam'].strip() in db.empty_options:
        error.append('period_spam')
    return error

def _clean_data_form(form):

def _create_entry(form:dict, id_person):
    entry = MovilidadEstudiantesSemilleros(
        id_person = id_person,
        semillero = form['semillero'],
        evento = form['evento'],
        proyecto = form['proyecto'],
        lugar = form['lugar'],
        fecha = form['fecha'],
        estudiantes = form['estudiantes'],
        period_spam = form['period_spam']
    )
    db.session.add(entry)
    db.session.commit()
    db.session.close()
