from app.interface import db
from app.domain.models import PublicacionLibros

def new_entry_publicacionlibros(form:dict, id_person):
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
    if not 'autores' in form or form['autores'].strip() in db.empty_options:
        error.append('autores')
    if not 'editorial' in form or form['editorial'].strip() in db.empty_options:
        error.append('editorial')
    if not 'fecha' in form or form['fecha'].strip() in db.empty_options:
        error.append('fecha')
    if not 'issn' in form or form['issn'].strip() in db.empty_options:
        error.append('issn')
    if not 'period_spam' in form or form['period_spam'].strip() in db.empty_options:
        error.append('period_spam')
    return error

def _clean_data_form(form):

def _create_entry(form:dict, id_person):
    entry = PublicacionLibros(
        id_person = id_person,
        titulo = form['titulo'],
        autores = form['autores'],
        editorial = form['editorial'],
        fecha = form['fecha'],
        issn = form['issn'],
        period_spam = form['period_spam']
    )
    db.session.add(entry)
    db.session.commit()
    db.session.close()
