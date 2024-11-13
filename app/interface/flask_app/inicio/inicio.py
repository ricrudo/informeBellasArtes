from flask import Blueprint, render_template, request
from app.interface.flask_app.routes import go_to

bp = Blueprint('inicio', __name__, url_prefix='/inicio')

@bp.route("/")
def inicio():
    '''
    Permite que el usuario vaya a actualizar borrador, revision y envio del informe final, consulta de informes enviados
    TODO se debe validar si el usuario ya envio el formulario para saber las opciones que tiene disponible, tal como se describe a continuacion
    Si ya envio el formulario de este year la opcion actualizar borrador no debe aparecer. Hecho[N]
    Si no hay ingresado ningun dato la primera opcion es debe decir Crear borrador y la opcion revision y envio del informe final no debe aparecer. Hecho[N]
    Si nunca ha enviado informes, no debe aparecer la opcion Consulta de informes enviados. Hecho[N] 
    '''
    return render_template('initial_menu.html')

@bp.route("/secciones")
def sections_menu():
    return render_template('sections_menu.html')

@bp.route("/info_docente", methods=['GET', 'POST'])
def informacion_docente():
    if request.method == 'POST':
        # guarda la informacion en la base de datos
        return go_to('inicio.informacion_docente', request.form.get('action'))
    nivel_actual = ''
    niveles = ['', 'Pregado', 'Maestría', 'Doctorado']
    return render_template('informacion_docente.html', nivel_actual=nivel_actual, niveles=niveles)


