from datetime import datetime
import re

def date_converter_or_none(date_input):
    try:
        response = datetime.strptime(date_input, '%Y-%m-%d').date()
    except (ValueError, TypeError):
        response = None
    return response

def date_converter_or_error(date_input):
    try:
        response = datetime.strptime(date_input, '%Y-%m-%d').date()
    except (ValueError, TypeError):
        response = 'error'
    return response

def join_students(initform, keyword, new_keyword=''):
    if not new_keyword:
        new_keyword += keyword
    groups = {}
    error = False
    keys = [x for x in initform.keys() if keyword in x]
    for key in keys:
        match = re.search(r'.+?_(\d+)_(\d+)$', key)
        if match:
            if f'{new_keyword}_{match.group(1)}' not in groups:
                groups[f'{new_keyword}_{match.group(1)}'] = []
            groups[f'{new_keyword}_{match.group(1)}'].append(initform.pop(key))
        else:
            error = True
    initform.update(groups)
    if error:
        return f'los campos {keyword} se encuentran en el formato incorrecto\n'
    return ''

def simple_form_separator(form:dict, keyword:str):
    '''
    separa formularios que tiene campos repetidos pero diferencias por un contador al final en el formato campo_1
    el keyword es el nombre de algun campo que sirve para encontrar la referencia, generalmente es el primer campo del formulario
    '''
    responses = {}
    for key in form.keys():
        if keyword in key:
            new_key = key.replace(keyword, '')
            responses[new_key] = {}
    for response in responses.keys():
        pattern = re.compile(re.escape(response) + r'$')
        for key, value in form.items():
            if pattern.search(key):
                new_key = key.replace(response, '')
                responses[response][new_key] = value
        responses[response]['period_spam'] = form['period_spam']
    return responses

def get_value_enums(form:dict, keyword, enumClass, inverted=False, get_value=True):
    if not inverted:
        try:
            value = enumClass[form[keyword].lower()].value
            if get_value:
                form[keyword] = value
            return ''
        except KeyError:
            return f"{form[keyword]} no es un valor valido\n"

