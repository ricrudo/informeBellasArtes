from flask import Flask, request, send_from_directory
from pathlib import Path
import json

from app.interface.db import person_exists

from app.interface.db import get_Data, set_Data, filesManager

from flask_cors import CORS

#from app.application import users_credential

name_db = 'BELLAS_ARTES_UA.db'

static_folder = Path.cwd() / 'app' / 'interface' / 'statics'
template_folder = Path.cwd() / 'app' / 'interface' / 'templates'

app = Flask(__name__, static_folder=static_folder, template_folder=template_folder)

CORS(app)

app.secret_key = '0664b5da52f853402fec9426f86764f2c5a5222d98a0807c4fefbdea92248b84'


@app.route("/", methods=['POST'])
def setData():
    '''
    Punto de entrada de la app
    '''
    #aca se debe hacer la validacion de identidad
    id_person = person_exists.is_real_person(request.authorization.token)
    if not id_person:
        return 'no user registered.'
    if request.form:
        jsonData = json.loads(request.form['jsonData'])
        if request.files:
            jsonData.update(request.files)
    else:
        return 'ok'
    jsonData['user'] = id_person
    messages = set_Data.setData(jsonData)
    '''messages = []
    for store in jsonData.keys():
        if 'section' in store:
            section = getSection(store)
            if section == 'question no valida':
                return section
            response = section.new_entry_user(jsonData)
            if response != 'ok':
                messages.append(response)
    '''
    if messages:
        return str(messages)
    return 'ok'

@app.route("/getDataUser", methods=['GET'])
def getDataUser():
    '''
    Entrada para obetener todos los datos que esten registrados con un user
    '''
    id_person = person_exists.is_real_person(request.authorization.token)
    if not id_person:
        return 'no user registered.'
    period_spam = request.args.get('period_spam')
    if period_spam:
        return get_Data.getAllDataUser(id_person, period_spam)


@app.route("/get/<section>", methods=['GET'])
def getData(section):
    '''
    Esto se debe borrar para la version production
    '''
    result = get_Data.getAllData(section)
    return result


@app.route('/getFile', methods=['GET'])
def get_file():
    id_person = person_exists.is_real_person(request.authorization.token)
    if not id_person:
        return 'no user registered.'
    path, filename = filesManager.getFile(request.args, id_person)
    if path and filename:
        return send_from_directory(path, filename, as_attachment=True)
    return 'no file'

