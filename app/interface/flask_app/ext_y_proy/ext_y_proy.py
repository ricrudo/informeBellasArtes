from flask import Blueprint, render_template, request
from app.interface.flask_app.routes import go_to

bp = Blueprint('ext_y_proy', __name__, url_prefix='/ext_y_proy')


@bp.route("/propuestas_educacion", methods=['GET', 'POST'])
def propuestas_educacion():
    if request.method == 'POST':
        #guarda la informacion en la base de datos
        return go_to('ext_y_proy.propuestas_educacion', request.form.get('action'))
    return render_template('5_1_propuestas_educacion.html')


@bp.route("/gestion_convenios", methods=['GET', 'POST'])
def gestion_convenios():
    if request.method == 'POST':
        #guarda la informacion en la base de datos
        return go_to('ext_y_proy.gestion_convenios', request.form.get('action'))
    return render_template('5_2_gestion_convenios.html')


@bp.route("/proyeccion_poblacion_priorizada", methods=['GET', 'POST'])
def proyeccion_poblacion_priorizada():
    if request.method == 'POST':
        #guarda la informacion en la base de datos
        return go_to('ext_y_proy.proyeccion_poblacion_priorizada', request.form.get('action'))
    return render_template('5_3_proyeccion_poblacion_priorizada.html')
