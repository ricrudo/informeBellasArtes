from pathlib import Path

tab = " "*4

def grouping_content(content_models):
    omitted_words = [' import ', '__ =', 'primary_key', 'sqla.sql.func.now()']
    result = {}
    for con in content_models:
        if not con.strip():
            continue
        if any([x in con for x in omitted_words]):
            continue
        if 'class' in con:
            function = con.replace('class', '').strip().split("(")[0]
            result[function] = {}
        elif not '=' in con:
            continue
        else:
            value = con.strip().split(' =')[0]
            result[function][value] = []
            if "Boolean" in con:
                result[function][value].append("Boolean")
            if "nullable" in con:
                result[function][value].append("nullable")
    return result

def add_imports(clase):
    return f'''from app.interface import db
from app.domain.models import {clase}\n'''

def create_factory(clase, content):
    response = f'\ndef new_entry_{clase.lower()}(form:dict, id_person):\n'
    response += tab + '''response = _check_content(form)
    if response:
        return f'faltan datos {response}']
    if not db.is_real_person(id_person):
        return 'No existe persona con el id indicado'
    _clean_data_form(form)
    _create_entry(form, id_person)
    return 'ok'\n'''
    return response

def create_check_content(clase, content):
    result = '''\ndef _check_content(form:dict, id_person):
    error = []
    if not id_person or id_person.strip() in db.empty_options:
        error.append('id_person')'''
    for value, adjective in content.items():
        if 'nullable' in adjective:
            result += f"\n{tab}if not '{value}' in form or form['{value}'].strip() in db.empty_options:"
            result += f"\n{tab}{tab}error.append('{value}')"
    result += f'\n{tab}return error\n'
    return result

def create_id_person_exists():
    return '''\ndef _id_person_exists(id_person):
    persons = session.query(Person).filter(Person.id == id_person)
    session.close()
    return persons\n'''

def create_clean_data(clase, content):
    result = '\ndef _clean_data_form(form):'
    for value, adjective in content.items():
        if value == "id_person":
            continue
        if "nullable" not in adjective:
            if "Boolean" in adjective:
                final = "False"
            else:
                final = '""'
            result += f"\n{tab}if not '{value}' in form or form['{value}'].strip() in db.empty_options:\n{tab}{tab}form['{value}'] = {final}"
    return result + "\n"

def create_create_entry(clase, content):
    result = f'''\ndef _create_entry(form:dict, id_person):
    entry = {clase}(
        id_person = id_person,'''
    for value in content.keys():
        if value == "id_person":
            continue
        result += f"\n{tab}{tab}{value} = form['{value}'],"
    result = result[:-1]
    result += '''
    )
    db.session.add(entry)
    db.session.commit()
    db.session.close()\n'''
    return result


def new_entries_generator(origin, destino, copy_to_folder=None):
    content_models = origin.read_text().split('\n')
    grouped_content = grouping_content(content_models)
    for clase, content in grouped_content.items():
        if clase in ['Person', 'Login']:
            continue
        content_file = add_imports(clase)
        content_file += create_factory(clase, content)
        content_file += create_check_content(clase, content)
        content_file += create_clean_data(clase, content)
        content_file += create_create_entry(clase, content)
        salida = destino / f'{clase.lower()}.py'
        salida.write_text(content_file)
        if copy_to_folder:
            destination = copy_to_folder / f'{clase.lower()}.py'
            destination.write_text(content_file)



