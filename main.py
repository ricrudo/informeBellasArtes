from flask import Flask, request, send_from_directory
from flask_jwt_extended import JWTManager, create_access_token,, create_refresh_token, jwt_required, get_jwt_identity
from pathlib import Path
import json

from app.interface.db import person_exists

from app.interface.db import get_Data, set_Data, filesManager, userValidation

from flask_cors import CORS
from datetime import timedelta

#from app.application import users_credential

name_db = 'BELLAS_ARTES_UA.db'

static_folder = Path.cwd() / 'app' / 'interface' / 'statics'
template_folder = Path.cwd() / 'app' / 'interface' / 'templates'

app = Flask(__name__, static_folder=static_folder, template_folder=template_folder)

CORS(app)

app.secret_key = '0664b5da52f853402fec9426f86764f2c5a5222d98a0807c4fefbdea92248b84'
app.config['JWT_SECRET_KEY'] = '0664b5da52f853402fec9426f86764f2c5a5222d98a0807c4fefbdea92248b84'
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=24)

jwt = JWTManager(app)

@app.route("/", methods=['POST'])
@jwt_required()
def setData():
    '''
    Punto de entrada de la app
    '''
    #aca se debe hacer la validacion de identidad
    id_person = person_exists.is_real_person(get_jwt_identity())
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
    if messages:
        return str(messages)
    return 'ok'

@app.route("/getDataUser", methods=['GET'])
@jwt_required()
def getDataUser():
    '''
    Entrada para obetener todos los datos que esten registrados con un user
    '''
    id_person = person_exists.is_real_person(get_jwt_identity())
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
@jwt_required()
def get_file():
    id_person = person_exists.is_real_person(get_jwt_identity())
    if not id_person:
        return 'no user registered.'
    path, filename = filesManager.getFile(request.args, id_person)
    if path and filename:
        return send_from_directory(path, filename, as_attachment=True)
    return 'no file'

@app.route('/loginUser', methods=['POST'])
def login():
    data = request.json
    response = userValidation.login(data)
    finalResponse = {'message': response}
    if response in ['acceso_aprobado', 'change_password']:
        email = data.get('username')
        access_token = create_access_token(identity=email)
        finalResponse['Authorization'] = f"Bearer {access_token}"
        refresh_token = create_refresh_token(identity=email)
        finalResponse['Refresh_token'] = f"Bearer {refresh_token}"
    return json.dumps(finalResponse)

@app.route('/recoveryPassword', methods=['POST'])
def recoveryPassword():
    data = request.json
    response = userValidation.recoveryPassword(data, app)
    return json.dumps({'message': response})


@app.route('/setPassword', methods=['POST'])
@jwt_required()
def setPassword():
    data = request.json
    email = get_jwt_identity()
    response = userValidation.setPassword(data, email)
    finalResponse = json.dumps({'message': response})
    return finalResponse
