from flask import Blueprint, render_template, request
from app.interface.flask_app.routes import go_to
from app.interface.db.gruposinvestigacion import new_entry_gruposinvestigacion
from app.interface.db.redesacademicas import new_entry_redesacademicas
from app.interface.db.proyectosinvestigacioncreacion import new_entry_proyectosinvestigacioncreacion
from app.interface.db.productoscreacion import new_entry_productoscreacion
from app.interface.db.publicacionarticulos import new_entry_publicacionarticulos
from app.interface.db.publicacionlibros import new_entry_publicacionlibros
from app.interface.db.participacioneventos import new_entry_participacioneventos
from app.interface.db.conveniosinterinstitucionales import new_entry_conveniosinterinstitucionales
from app.interface.db.patentes import new_entry_patentes
from app.interface.db.direcciontesis import new_entry_direcciontesis
from app.interface.db.evaluaciontesis import new_entry_evaluaciontesis
from app.interface.db.coordsemilleros import new_entry_coordsemilleros
from app.interface.db.convocatoriassemilleros import new_entry_convocatoriassemilleros
from app.interface.db.movilidadestudiantessemilleros import new_entry_movilidadestudiantessemilleros
from app.interface.db.jovenesinvestigadores import new_entry_jovenesinvestigadores

bp = Blueprint('investigacion', __name__, url_prefix='/investigacion')

@bp.route("/part_grupos_investigacion", methods=['GET', 'POST'])
def part_grupos_investigacion():
    if request.method == 'POST':
        #guarda la informacion en la base de datos
        id_person = 1
        response = new_entry_gruposinvestigacion(dict(request.form), id_person)
        if response != 'ok':
            return response
        else:
            return go_to('investigacion.part_grupos_investigacion', request.form.get('action'))
    return render_template('4_1_part_grupos_investigacion.html')

@bp.route("/redes_academicas_profesores", methods=['GET', 'POST'])
def redes_academicas_profesores():
    if request.method == 'POST':
        #guarda la informacion en la base de datos
        id_person = 1
        response = new_entry_redesacademicas(dict(request.form), id_person)
        if response != 'ok':
            return response
        else:
            return go_to('investigacion.redes_academicas_profesores', request.form.get('action'))
    
    return render_template('4_2_redes_academicas_profesores.html')

@bp.route("/desarollo_proyectos_investigacion_creacion", methods=['GET', 'POST'])
def desarollo_proyectos_investigacion_creacion():
    if request.method == 'POST':
        #guarda la informacion en la base de datos
        id_person = 1
        response = new_entry_proyectosinvestigacioncreacion(dict(request.form), id_person)
        if response != 'ok':
            return response
        else:
            return go_to('investigacion.desarollo_proyectos_investigacion_creacion', request.form.get('action'))
    
    return render_template('4_3_desarollo_proyectos_investigacion_creacion.html')

@bp.route("/productos_creacion", methods=['GET', 'POST'])
def productos_creacion():
    if request.method == 'POST':
        #guarda la informacion en la base de datos
        id_person = 1
        response = new_entry_productoscreacion(dict(request.form), id_person)
        if response != 'ok':
            return response
        else:
            return go_to('investigacion.productos_creacion', request.form.get('action'))
    return render_template('4_4_productos_creacion.html')

@bp.route("/publicacion_articulos", methods=['GET', 'POST'])
def publicacion_articulos():
    if request.method == 'POST':
        #guarda la informacion en la base de datos
        id_person = 1
        response = new_entry_publicacionarticulos(dict(request.form), id_person)
        if response != 'ok':
            return response
        else:
            return go_to('investigacion.publicacion_articulos', request.form.get('action'))
    
    return render_template('4_5_publicacion_articulos.html')

@bp.route("/publicacion_libros", methods=['GET', 'POST'])
def publicacion_libros():
    if request.method == 'POST':
        #guarda la informacion en la base de datos
        id_person = 1
        response = new_entry_publicacionlibros(dict(request.form), id_person)
        if response != 'ok':
            return response
        else:
            return go_to('investigacion.publicacion_libros', request.form.get('action'))
    
    return render_template('4_6_publicacion_libros.html')

@bp.route("/part_eventos_academicos", methods=['GET', 'POST'])
def part_eventos_academicos():
    if request.method == 'POST':
        #guarda la informacion en la base de datos
        id_person = 1
        response = new_entry_participacioneventos(dict(request.form), id_person)
        if response != 'ok':
            return response
        else:
            return go_to('investigacion.part_eventos_academicos', request.form.get('action'))
    
    return render_template('4_7_part_eventos_academicos.html')

@bp.route("/convenios_productos_redes", methods=['GET', 'POST'])
def convenios_productos_redes():
    if request.method == 'POST':
        #guarda la informacion en la base de datos
        id_person = 1
        response = new_entry_conveniosinterinstitucionales(dict(request.form), id_person)
        if response != 'ok':
            return response
        else:
            return go_to('investigacion.convenios_productos_redes', request.form.get('action'))
    
    return render_template('4_8_convenios_productos_redes.html')

@bp.route("/patentes_derechos_autor", methods=['GET', 'POST'])
def patentes_derechos_autor():
    if request.method == 'POST':
        #guarda la informacion en la base de datos
        id_person = 1
        response = new_entry_patentes(dict(request.form), id_person)
        if response != 'ok':
            return response
        else:
            return go_to('investigacion.patentes_derechos_autor', request.form.get('action'))
    
    return render_template('4_9_patentes_derechos_autor.html')

@bp.route("/direcion_tesis", methods=['GET', 'POST'])
def direcion_tesis():
    if request.method == 'POST':
        #guarda la informacion en la base de datos
        id_person = 1
        response = new_entry_direcciontesis(dict(request.form), id_person)
        if response != 'ok':
            return response
        else:
            return go_to('investigacion.direcion_tesis', request.form.get('action'))
    
    return render_template('4_10_direcion_tesis.html')

@bp.route("/evaluacion_tesis", methods=['GET', 'POST'])
def evaluacion_tesis():
    if request.method == 'POST':
        #guarda la informacion en la base de datos
        id_person = 1
        response = new_entry_evaluaciontesis(dict(request.form), id_person)
        if response != 'ok':
            return response
        else:
            return go_to('investigacion.evaluacion_tesis', request.form.get('action'))
    
    return render_template('4_11_evaluacion_tesis.html')

@bp.route("/coordinacion_semilleros", methods=['GET', 'POST'])
def coordinacion_semilleros():
    if request.method == 'POST':
        #guarda la informacion en la base de datos
        id_person = 1
        response = new_entry_coordsemilleros(dict(request.form), id_person)
        if response != 'ok':
            return response
        else:
            return go_to('investigacion.coordinacion_semilleros', request.form.get('action'))
    
    return render_template('4_12_coordinacion_semilleros.html')

@bp.route("/convocatorias_semilleros", methods=['GET', 'POST'])
def convocatorias_semilleros():
    if request.method == 'POST':
        #guarda la informacion en la base de datos
        id_person = 1
        response = new_entry_convocatoriassemilleros(dict(request.form), id_person)
        if response != 'ok':
            return response
        else:
            return go_to('investigacion.convocatorias_semilleros', request.form.get('action'))
    
    return render_template('4_13_convocatorias_semilleros.html')

@bp.route("/movilidad_estudiantes_semilleros", methods=['GET', 'POST'])
def movilidad_estudiantes_semilleros():
    if request.method == 'POST':
        #guarda la informacion en la base de datos
        id_person = 1
        response = new_entry_movilidadestudiantessemilleros(dict(request.form), id_person)
        if response != 'ok':
            return response
        else:
            return go_to('investigacion.movilidad_estudiantes_semilleros', request.form.get('action'))
    
    return render_template('4_14_movilidad_estudiantes_semilleros.html')

@bp.route("/jovenes_investigadores", methods=['GET', 'POST'])
def jovenes_investigadores_apoyados():
    if request.method == 'POST':
        #guarda la informacion en la base de datos
        id_person = 1
        response = new_entry_jovenesinvestigadores(dict(request.form), id_person)
        if response != 'ok':
            return response
        else:
            return go_to('investigacion.jovenes_investigadores_apoyados', request.form.get('action'))
    
    return render_template('4_15_jovenes_investigadores_apoyados.html')

@bp.route("/otras_actividades_investigacion_extension_creacion", methods=['GET', 'POST'])
def otras_actividades_investigacion_extension_creacion():
    if request.method == 'POST':
        #guarda la informacion en la base de datos
        return go_to('investigacion.otras_actividades_investigacion_extension_creacion', request.form.get('action'))
    
    return render_template('4_16_otras_actividades_investigacion_extension_creacion.html')

@bp.route("/otras_actividades_recursos_estrategias", methods=['GET', 'POST'])
def otras_actividades_recursos_estrategias():
    if request.method == 'POST':
        #guarda la informacion en la base de datos
        return go_to('investigacion.otras_actividades_recursos_estrategias', request.form.get('action'))
    
    return render_template('4_17_otras_actividades_recursos_estrategias.html')

