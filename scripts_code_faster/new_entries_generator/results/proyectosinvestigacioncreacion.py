from app.interface import db
from app.domain.models import ProyectosInvestigacionCreacion

def new_entry_proyectosinvestigacioncreacion(form:dict, id_person):
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
    if not 'nombre_pyotecto' in form or form['nombre_pyotecto'].strip() in db.empty_options:
        error.append('nombre_pyotecto')
    if not 'code' in form or form['code'].strip() in db.empty_options:
        error.append('code')
    if not 'tipo_convocatoria' in form or form['tipo_convocatoria'].strip() in db.empty_options:
        error.append('tipo_convocatoria')
    if not 'nombre_convocatoria' in form or form['nombre_convocatoria'].strip() in db.empty_options:
        error.append('nombre_convocatoria')
    if not 'financiamiento' in form or form['financiamiento'].strip() in db.empty_options:
        error.append('financiamiento')
    if not 'ods' in form or form['ods'].strip() in db.empty_options:
        error.append('ods')
    if not 'software' in form or form['software'].strip() in db.empty_options:
        error.append('software')
    if not 'idi5' in form or form['idi5'].strip() in db.empty_options:
        error.append('idi5')
    if not 'period_spam' in form or form['period_spam'].strip() in db.empty_options:
        error.append('period_spam')
    return error

def _clean_data_form(form):
    if not 'elegido' in form or form['elegido'].strip() in db.empty_options:
        form['elegido'] = False
    if not 'co_investigadores' in form or form['co_investigadores'].strip() in db.empty_options:
        form['co_investigadores'] = ""
    if not 'estudiantes' in form or form['estudiantes'].strip() in db.empty_options:
        form['estudiantes'] = ""

def _create_entry(form:dict, id_person):
    entry = ProyectosInvestigacionCreacion(
        id_person = id_person,
        nombre_pyotecto = form['nombre_pyotecto'],
        code = form['code'],
        tipo_convocatoria = form['tipo_convocatoria'],
        nombre_convocatoria = form['nombre_convocatoria'],
        elegido = form['elegido'],
        financiamiento = form['financiamiento'],
        co_investigadores = form['co_investigadores'],
        estudiantes = form['estudiantes'],
        ods = form['ods'],
        software = form['software'],
        idi5 = form['idi5'],
        period_spam = form['period_spam']
    )
    db.session.add(entry)
    db.session.commit()
    db.session.close()
