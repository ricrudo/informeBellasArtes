from app.interface import db
from app.domain.models import ConveniosInterinstitucionales

def new_entry_conveniosinterinstitucionales(form:dict, id_person):
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
    if not 'convenio' in form or form['convenio'].strip() in db.empty_options:
        error.append('convenio')
    if not 'producto' in form or form['producto'].strip() in db.empty_options:
        error.append('producto')
    if not 'grupo' in form or form['grupo'].strip() in db.empty_options:
        error.append('grupo')
    if not 'impacto' in form or form['impacto'].strip() in db.empty_options:
        error.append('impacto')
    if not 'period_spam' in form or form['period_spam'].strip() in db.empty_options:
        error.append('period_spam')
    return error

def _clean_data_form(form):

def _create_entry(form:dict, id_person):
    entry = ConveniosInterinstitucionales(
        id_person = id_person,
        convenio = form['convenio'],
        producto = form['producto'],
        grupo = form['grupo'],
        impacto = form['impacto'],
        period_spam = form['period_spam']
    )
    db.session.add(entry)
    db.session.commit()
    db.session.close()
