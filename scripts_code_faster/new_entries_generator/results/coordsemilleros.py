from app.interface import db
from app.domain.models import CoordSemilleros

def new_entry_coordsemilleros(form:dict, id_person):
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
    if not 'total_integrantes' in form or form['total_integrantes'].strip() in db.empty_options:
        error.append('total_integrantes')
    if not 'nuevos_integrantes' in form or form['nuevos_integrantes'].strip() in db.empty_options:
        error.append('nuevos_integrantes')
    if not 'grupo' in form or form['grupo'].strip() in db.empty_options:
        error.append('grupo')
    if not 'programa' in form or form['programa'].strip() in db.empty_options:
        error.append('programa')
    if not 'update_sia' in form or form['update_sia'].strip() in db.empty_options:
        error.append('update_sia')
    if not 'period_spam' in form or form['period_spam'].strip() in db.empty_options:
        error.append('period_spam')
    return error

def _clean_data_form(form):

def _create_entry(form:dict, id_person):
    entry = CoordSemilleros(
        id_person = id_person,
        semillero = form['semillero'],
        total_integrantes = form['total_integrantes'],
        nuevos_integrantes = form['nuevos_integrantes'],
        grupo = form['grupo'],
        programa = form['programa'],
        update_sia = form['update_sia'],
        period_spam = form['period_spam']
    )
    db.session.add(entry)
    db.session.commit()
    db.session.close()
