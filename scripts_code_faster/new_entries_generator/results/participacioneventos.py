from app.interface import db
from app.domain.models import ParticipacionEventos

def new_entry_participacioneventos(form:dict, id_person):
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
    if not 'titulo' in form or form['titulo'].strip() in db.empty_options:
        error.append('titulo')
    if not 'evento' in form or form['evento'].strip() in db.empty_options:
        error.append('evento')
    if not 'lugar' in form or form['lugar'].strip() in db.empty_options:
        error.append('lugar')
    if not 'fecha' in form or form['fecha'].strip() in db.empty_options:
        error.append('fecha')
    if not 'tipo_participacion' in form or form['tipo_participacion'].strip() in db.empty_options:
        error.append('tipo_participacion')
    if not 'modalidad' in form or form['modalidad'].strip() in db.empty_options:
        error.append('modalidad')
    if not 'period_spam' in form or form['period_spam'].strip() in db.empty_options:
        error.append('period_spam')
    return error

def _clean_data_form(form):

def _create_entry(form:dict, id_person):
    entry = ParticipacionEventos(
        id_person = id_person,
        titulo = form['titulo'],
        evento = form['evento'],
        lugar = form['lugar'],
        fecha = form['fecha'],
        tipo_participacion = form['tipo_participacion'],
        modalidad = form['modalidad'],
        period_spam = form['period_spam']
    )
    db.session.add(entry)
    db.session.commit()
    db.session.close()
