from flask import Blueprint, render_template, request
from app.interface.flask_app.routes import go_to

bp = Blueprint('bienestar', __name__, url_prefix='/bienestar')


@bp.route("/asignacion_misional_bienestar", methods=['GET', 'POST'])
def asignacion_misional_bienestar():
    if request.method == 'POST':
        #guarda la informacion en la base de datos
        return go_to('bienestar.asignacion_misional_bienestar', request.form.get('action'))
    return render_template('6_1_asignacion_misional_bienestar.html')


@bp.route("/atendidos_bienestar", methods=['GET', 'POST'])
def atendidos_bienestar():
    if request.method == 'POST':
        #guarda la informacion en la base de datos
        return go_to('bienestar.atendidos_bienestar', request.form.get('action'))
    return render_template('6_2_atendidos_bienestar.html')
