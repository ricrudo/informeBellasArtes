from app.interface import db
from app.domain.models import GruposInvestigacion

def new_entry_gruposinvestigacion(form:dict, id_person):
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
    if not 'grupo' in form or form['grupo'].strip() in db.empty_options:
        error.append('grupo')
    if not 'linea_investiga' in form or form['linea_investiga'].strip() in db.empty_options:
        error.append('linea_investiga')
    if not 'programa' in form or form['programa'].strip() in db.empty_options:
        error.append('programa')
    if not 'period_spam' in form or form['period_spam'].strip() in db.empty_options:
        error.append('period_spam')
    return error

def _clean_data_form(form):
    if not 'actividades' in form or form['actividades'].strip() in db.empty_options:
        form['actividades'] = ""

def _create_entry(form:dict, id_person):
    entry = GruposInvestigacion(
        id_person = id_person,
        grupo = form['grupo'],
        linea_investiga = form['linea_investiga'],
        programa = form['programa'],
        actividades = form['actividades'],
        period_spam = form['period_spam']
    )
    db.session.add(entry)
    db.session.commit()
    db.session.close()
