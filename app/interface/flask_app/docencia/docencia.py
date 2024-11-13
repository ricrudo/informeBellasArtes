from flask import Blueprint, render_template, request
from app.interface.flask_app.routes import go_to
from app.interface.db.misionaldocencia import new_entry_misionaldocencia
from app.interface.db.participa_procesos_curriculares import new_entry_participa_procesos_curriculares

bp = Blueprint('docencia', __name__, url_prefix='/docencia')

@bp.route("/", methods=['GET', 'POST'])
def func_misional_docencia():
    if request.method == 'POST':
        # guarda la informacion en la base de datos
        id_person = 1
        response = new_entry_misionaldocencia(dict(request.form), id_person)
        if response != 'ok':
            return response
        else:
            return go_to('docencia.func_misional_docencia', request.form.get('action'))
    clases = {123456789:
              {"code": "123456789", "name":"Técnicas en composición I", "programa":"Música", "open-html":False},
              1234: 
              {"code": "1234589", "name":"Técnicas en composición II", "programa":"Música", "open-html":True}
              }
    
    return render_template('func_misional_docencia.html', clases=clases)

@bp.route("/participa_procesos_curriculares", methods=['GET', 'POST'])
def participa_procesos_curriculares():
    if request.method == 'POST':
        #guarda la informacion en la base de datos
        id_person = 1
        response = new_entry_participa_procesos_curriculares(dict(request.form), id_person)
        if response != 'ok':
            return response
        else:
            return go_to('docencia.participa_procesos_curriculares', request.form.get('action'))
    
    return render_template('procesos_curriculares.html')

