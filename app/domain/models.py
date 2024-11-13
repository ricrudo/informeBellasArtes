from app.interface import db
import sqlalchemy as sqla


class Person(db.Base):
    __tablename__ = 'persons'

    id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True)
    name = sqla.Column(sqla.Text, nullable=False)
    admin_role = sqla.Column(sqla.Boolean, default=False)
    # responde a la pregunta: nivel de formacion
        # pregrado = 1
        # maestria = 2
        # doctorado = 3
        # posdoctorado = 4
    formacion = sqla.Column(sqla.VARCHAR(len("posdoctorado") + 2))
    facultad = sqla.Column(sqla.VARCHAR(50))
    # aunque el valor es un int, realmente es un texto tiene separado por comas sin espacios, eje "1,3,"
        # licenciatura_en_musica = 1
        # artes_plasticas = 2
        # arte_dramatico = 3
        # danza = 4
        # musica = 5
    programas = sqla.Column(sqla.Text)
    email = sqla.Column(sqla.VARCHAR(50), nullable=False)
    date_creation = sqla.Column(sqla.DateTime(timezone=True), server_default=sqla.sql.func.now())
    
class Login(db.Base):
    __tablename__ = 'login'

    id = sqla.Column(sqla.Integer, primary_key=True)
    id_person = sqla.Column(sqla.Integer, sqla.ForeignKey('persons.id'))
    email = sqla.Column(sqla.VARCHAR(50), nullable=False)
    password = sqla.Column(sqla.VARCHAR(80), nullable=False)
    temp_pass = sqla.Column(sqla.Boolean, default=False)
    date_creation = sqla.Column(sqla.DateTime(timezone=True), server_default=sqla.sql.func.now())
    fecha_update = sqla.Column(sqla.DateTime(timezone=True), onupdate=sqla.sql.func.now())  # Se actualiza automáticamente al realizar cambios. La opción onupdate está bien soportada en motores como PostgreSQL, MySQL y SQLite, pero es posible que debas ajustar la implementación según las características específicas de tu base de datos.

class ActiveSections(db.Base):
    '''
    Almacena el estado de las preguntas que dependen de ser activadas por el usuario
    '''
    __tablename__ = 'active_sections'

    id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True)
    id_person = sqla.Column(sqla.Integer, sqla.ForeignKey('persons.id'))
    activateQuestionsection4_1 = sqla.Column(sqla.VARCHAR(2))
    activateQuestionsection4_3 = sqla.Column(sqla.VARCHAR(2))
    activateQuestionsection4_4 = sqla.Column(sqla.VARCHAR(2))
    activateQuestionsection4_5 = sqla.Column(sqla.VARCHAR(2))
    activateQuestionsection4_6 = sqla.Column(sqla.VARCHAR(2))
    activateQuestionsection4_7 = sqla.Column(sqla.VARCHAR(2))
    activateQuestionsection4_8 = sqla.Column(sqla.VARCHAR(2))
    activateQuestionsection4_9 = sqla.Column(sqla.VARCHAR(2))
    activateQuestionsection4_10 = sqla.Column(sqla.VARCHAR(2))
    activateQuestionsection4_11 = sqla.Column(sqla.VARCHAR(2))
    activateQuestionsection4_12 = sqla.Column(sqla.VARCHAR(2))
    activateQuestionsection4_13 = sqla.Column(sqla.VARCHAR(2))
    activateQuestionsection4_14 = sqla.Column(sqla.VARCHAR(2))
    activateQuestionsection4_15 = sqla.Column(sqla.VARCHAR(2))
    activateQuestionsection4_16 = sqla.Column(sqla.VARCHAR(2))
    activateQuestionsection4_17 = sqla.Column(sqla.VARCHAR(2))
    activateQuestionsection5_1 = sqla.Column(sqla.VARCHAR(2))
    activateQuestionsection5_2 = sqla.Column(sqla.VARCHAR(2))
    activateQuestionsection5_3 = sqla.Column(sqla.VARCHAR(2))
    activateQuestionsection6_2 = sqla.Column(sqla.VARCHAR(2))
    activateQuestionsection6_3 = sqla.Column(sqla.VARCHAR(2))
    activateQuestionsection6_4 = sqla.Column(sqla.VARCHAR(2))
    activateQuestionsection6_5 = sqla.Column(sqla.VARCHAR(2))
    activateQuestionsection6_6 = sqla.Column(sqla.VARCHAR(2))
    activateQuestionsection6_7 = sqla.Column(sqla.VARCHAR(2))
    period_spam = sqla.Column(sqla.VARCHAR(10), nullable=False)

class MisionalDocenciaPTA(db.Base):
    '''
    2.1 FUNCIÓN MISIONAL DE DOCENCIA - MATERIAS PTA
    '''
    __tablename__ = 'misional_docencia_pta'

    id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True)
    id_person = sqla.Column(sqla.Integer, sqla.ForeignKey('persons.id'))
    index_entry = sqla.Column(sqla.Integer, nullable=False)
    materia = sqla.Column(sqla.Text)
    code = sqla.Column(sqla.VARCHAR(50))
        # licenciatura_en_musica = 1
        # artes_plasticas = 2
        # arte_dramatico = 3
        # danza = 4
        # musica = 5
    programa = sqla.Column(sqla.VARCHAR(len("licenciatura_en_musica") + 2))
    status_done = sqla.Column(sqla.VARCHAR(3))
    # Respuesta a la pregunta: Observaciones sobre el desarrollo de las actividades docentes
    observaciones = sqla.Column(sqla.Text)
    # Respuesta a la pregunta: Contenidos que abodardan tematicas ciudadanas y de responsabilidad social
    contenidos_especiales = sqla.Column(sqla.Text)
    # Respuesta a la pregunta: motivos de cancelacion
    motivos_cancel = sqla.Column(sqla.Text)
    period_spam = sqla.Column(sqla.VARCHAR(10), nullable=False)

class MisionalDocenciaAdicionales(db.Base):
    '''
    2.2 FUNCIÓN MISIONAL DE DOCENCIA - MATERIAS ADICIONALES
    '''
    __tablename__ = 'misional_docencia_adicionales'

    id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True)
    id_person = sqla.Column(sqla.Integer, sqla.ForeignKey('persons.id'))
    index_entry = sqla.Column(sqla.Integer, nullable=False)
        # licenciatura_en_musica = 1
        # artes_plasticas = 2
        # arte_dramatico = 3
        # danza = 4
        # musica = 5
    programa_add = sqla.Column(sqla.VARCHAR(len("licenciatura_en_musica") + 2))
    materia_add = sqla.Column(sqla.Text)
    code_add = sqla.Column(sqla.VARCHAR(50))
    # Respuesta a la pregunta: Observaciones sobre el desarrollo de las actividades docentes
    observaciones_add = sqla.Column(sqla.Text)
    # Respuesta a la pregunta: Contenidos que abodardan tematicas ciudadanas y de responsabilidad social
    contenidos_especiales_add = sqla.Column(sqla.Text)
    period_spam = sqla.Column(sqla.VARCHAR(10), nullable=False)

class Part_ProcesosCurriculares(db.Base):
    '''
    3.1 PARTICIPACIÓN EN PROCESOS CURRICULARES
    '''
    __tablename__ = 'participa_procesos_curriculares'

    id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True)
    id_person = sqla.Column(sqla.Integer, sqla.ForeignKey('persons.id'))
    index_entry = sqla.Column(sqla.Integer, nullable=False)
    # responde a la pregunta nombre del proceso
        # autoevaluacion = 1
        # acreditacion = 2
        # curricular = 3
        # estudio = 4
        # disciplinar = 5
        # silabos = 6
        # grado = 7
        # misional = 8
        # oportuna = 9
        # nuevos = 10
        # facultad = 11
    proceso = sqla.Column(sqla.VARCHAR(len("autoevaluacion")+2))
    status_ = sqla.Column(sqla.VARCHAR(2))
    # response a la pregunta: Programa o misional
        # programa = 1
        # misional = 2
    type_ = sqla.Column(sqla.VARCHAR(len("programa")+2))
    # Respuesta a la pregunta: Observaciones sobre el proceso
    misional_ = sqla.Column(sqla.VARCHAR(len("mis_autoevaluacion") + 2))
    programa_ = sqla.Column(sqla.VARCHAR(len("licenciatura_en_musica") + 2))
    observaciones_ = sqla.Column(sqla.Text)
    period_spam = sqla.Column(sqla.VARCHAR(10), nullable=False)

class GruposInvestigacion(db.Base):
    '''
    4.1 PARTICIPACIÓN EN GRUPOS DE INVESTIGACIÓN (Avalados por la universidad del Atlántico)

    template = '{"grupo": null, "linea_investiga": {"musical": false, "cultura": false, "estetica": false, "pedagogia": false}, "programa": null, "actividades": null}'
    '''
    __tablename__ = 'grupos_investigacion'

    id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True)
    id_person = sqla.Column(sqla.Integer, sqla.ForeignKey('persons.id'), nullable=False)
    index_entry = sqla.Column(sqla.Integer, nullable=False)
        # art = 'ARTE – ACCIÓN'
        # sam = 'Sapiencia, Arte y Música (S.A.M.)'
        # fel = 'Feliza Bursztyn: Redes, Arte, Cultura'
        # vid = 'Investigaciones Visuales del Caribe VIDENS'
        # tei = 'Teatro, Espacio e Interactividad _TEI_'
    grupo = sqla.Column(sqla.VARCHAR(len("arte-accion") + 2))
    linea_investiga = sqla.Column(sqla.Text)
        # licenciatura_en_musica = 1
        # artes_plasticas = 2
        # arte_dramatico = 3
        # danza = 4
        # musica = 5
    programa = sqla.Column(sqla.VARCHAR(len("licenciatura_en_musica") + 2))
    actividades = sqla.Column(sqla.Text)
    period_spam = sqla.Column(sqla.VARCHAR(10), nullable=False)

    
class RedesAcademicas(db.Base):
    '''
    4.2 REDES ACADÉMICAS DEL PROFESOR
    '''
    __tablename__ = 'redes_academicas'

    id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True)
    id_person = sqla.Column(sqla.Integer, sqla.ForeignKey('persons.id'))
    index_entry = sqla.Column(sqla.Integer, nullable=False)
    # responde a la pregunta: nombre red
        #cvlac = cvl
        #google_scholar = ggs
        #researchgate = rsg
        #orcid = ord
        #youtube = ytb
    name_red = sqla.Column(sqla.VARCHAR(len('google_scholar')+2))
    status = sqla.Column(sqla.VARCHAR(3))
    link = sqla.Column(sqla.Text)
    update_date =  sqla.Column(sqla.VARCHAR(10))
    period_spam = sqla.Column(sqla.VARCHAR(10), nullable=False)

class ProyectosInvestigacionCreacion(db.Base):
    '''
    4.3 DESARROLLO DE PROYECTOS DE INVESTIGACIÓN O CREACIÓN
    '''
    __tablename__ = 'proyectos_investigacion_creacion'

    id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True)
    id_person = sqla.Column(sqla.Integer, sqla.ForeignKey('persons.id'))
    index_entry = sqla.Column(sqla.Integer, nullable=False)
    nombre_proyecto = sqla.Column(sqla.Text)
    code = sqla.Column(sqla.VARCHAR(50))
    #respose a la pregunta: Tipo de convocatoria
        # interna = 1
        # externa = 2
    tipo_convocatoria = sqla.Column(sqla.VARCHAR(10))
    nombre_convocatoria = sqla.Column(sqla.Text)
        # no = 0
        # si = 1
        # espera = 2
    elegido = sqla.Column(sqla.VARCHAR(6))
    financiamiento = sqla.Column(sqla.Text)
    # responde a la pregunta: Tipo de participacion
        # principal = 1
        # co_investigador = 2
    tipo_participacion = sqla.Column(sqla.VARCHAR(len("co-investigador") + 2))
    # responde a la pregunta: participa semillero de investigacion
    bool_semillero = sqla.Column(sqla.VARCHAR(2))
    semillero = sqla.Column(sqla.Text)
    estudiante = sqla.Column(sqla.Text)
    # response a la pregunta: El proyecto aporta a los ODS
    ods = sqla.Column(sqla.VARCHAR(2))
    # response a la pregunta: ¿Incluyen desarrollo de software para la creación artística?
    software = sqla.Column(sqla.VARCHAR(2))
    # response a la pregunta: Es un proyecto I+D+I5
    idi5 = sqla.Column(sqla.VARCHAR(2))
    period_spam = sqla.Column(sqla.VARCHAR(10), nullable=False)

class ProductosCreacion(db.Base):
    '''
    4.4 PRODUCTOS DE CREACIÓN
    '''
    __tablename__ = 'productos_creacion'

    id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True)
    id_person = sqla.Column(sqla.Integer, sqla.ForeignKey('persons.id'))
    index_entry = sqla.Column(sqla.Integer, nullable=False)
    tipo_producto = sqla.Column(sqla.VARCHAR(3))
    nombre_producto = sqla.Column(sqla.Text)
    # responde a la pregunta: Institución donde fue exhibido o presentado
    institucion = sqla.Column(sqla.Text)
    # responde a la pregunta: alcance
        # local = 1
        # regional = 2
        # nacional = 3
        # internacional = 4
    alcance = sqla.Column(sqla.VARCHAR(len("internacional") + 2))
    fecha =  sqla.Column(sqla.VARCHAR(10))
    # responde a la pregunta: Link de difusión del evento/obra o nombre del catálogo si lo hubiera
    link = sqla.Column(sqla.Text)
    # responde a la pregunta: Categoría de reconocimiento por Minciencias
        # tipo_A = 1
        # tipo_B = 2
        # no_responde = 3
    categoria = sqla.Column(sqla.VARCHAR(len("no_responde") + 2))
    period_spam = sqla.Column(sqla.VARCHAR(10), nullable=False)

class PublicacionArticulos(db.Base):
    '''
    4.5 PUBLICACIÓN DE ARTÍCULOS
    '''
    __tablename__ = 'publicacion_articulos'

    id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True)
    id_person = sqla.Column(sqla.Integer, sqla.ForeignKey('persons.id'))
    index_entry = sqla.Column(sqla.Integer, nullable=False)
    titulo = sqla.Column(sqla.Text)
    autores = sqla.Column(sqla.Text)
    revista = sqla.Column(sqla.Text)
    link = sqla.Column(sqla.Text)
    fecha =  sqla.Column(sqla.VARCHAR(10))
    issn = sqla.Column(sqla.Text)
    # responde a la pregunta: Tipo de indexacion de la revista
        # otros = 0
        # publindex = 1
        # wos = 2
        # scopus = 3
    index_revista = sqla.Column(sqla.VARCHAR(len("publindex") + 2))
    period_spam = sqla.Column(sqla.VARCHAR(10), nullable=False)

class PublicacionLibros(db.Base):
    '''
    4.6 PUBLICACIÓN DE LIBROS Y /O CAPITULOS DE LIBRO
    '''
    __tablename__ = 'publicacion_libros'

    id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True)
    id_person = sqla.Column(sqla.Integer, sqla.ForeignKey('persons.id'))
    index_entry = sqla.Column(sqla.Integer, nullable=False)
    titulo = sqla.Column(sqla.Text)
    autores = sqla.Column(sqla.Text)
    editorial = sqla.Column(sqla.Text)
    fecha =  sqla.Column(sqla.VARCHAR(10))
    issn = sqla.Column(sqla.Text)
    period_spam = sqla.Column(sqla.VARCHAR(10), nullable=False)

class ParticipacionEventos(db.Base):
    '''
    4.7 PARTICIPACIÓN EN EVENTOS ACADÉMICOS Y/O ARTÍSTICOS NACIONALES E INTERNACIONALES
    '''
    __tablename__ = 'participacion_eventos'

    id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True)
    id_person = sqla.Column(sqla.Integer, sqla.ForeignKey('persons.id'))
    index_entry = sqla.Column(sqla.Integer, nullable=False)
    #response a la pregunta: nombre ponencia o intervencion
    titulo = sqla.Column(sqla.Text)
    evento = sqla.Column(sqla.Text)
    lugar = sqla.Column(sqla.Text)
    fecha =  sqla.Column(sqla.VARCHAR(10))
    tipo_participacion = sqla.Column(sqla.VARCHAR(len("conferencista") + 2))
    # responde a la pregunta: modalidad
        # virtual = 1
        # presencial = 2
    modalidad = sqla.Column(sqla.VARCHAR(len("presencial") + 2))
    aprobado =  sqla.Column(sqla.VARCHAR(2))
    name_file = sqla.Column(sqla.Text)
    bool_semillero = sqla.Column(sqla.VARCHAR(2))
    semillero = sqla.Column(sqla.Text)
    participantes = sqla.Column(sqla.Text)
    # responde a la pregunta: movilidad
        # internacional = 1
        # nacional = 2
        # regional = 3
    movilidad = sqla.Column(sqla.VARCHAR(len("internacional") + 2))
    period_spam = sqla.Column(sqla.VARCHAR(10), nullable=False)

class ConveniosInterinstitucionales(db.Base):
    '''
    4.8 CONVENIOS INTERINSTITUCIONALES Y PRODUCTOS DERIVADOS DEL TRABAJO EN REDES
    '''
    __tablename__ = 'convenios_interinstitucionales'

    id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True)
    id_person = sqla.Column(sqla.Integer, sqla.ForeignKey('persons.id'))
    index_entry = sqla.Column(sqla.Integer, nullable=False)
    convenio = sqla.Column(sqla.Text)
    #responde a la pregunta: producto derivado
    producto = sqla.Column(sqla.Text)
    # responde a la pregunta: grupo de investigacion
    grupo = sqla.Column(sqla.VARCHAR(len("arte-accion") + 2))
    # responde a la pregunta: Impacto del proyecto en la formación de los estudiantes
    impacto = sqla.Column(sqla.Text)
    period_spam = sqla.Column(sqla.VARCHAR(10), nullable=False)


class Patentes(db.Base):
    '''
    4.9 PATENTES Y/O REGISTRO DE DERECHOS DE AUTOR
    '''
    __tablename__ = 'patentes_derechos_de_autor'

    id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True)
    id_person = sqla.Column(sqla.Integer, sqla.ForeignKey('persons.id'))
    index_entry = sqla.Column(sqla.Integer, nullable=False)
    # responde a la pregunta: tipo de producto
        # artisticas = 1
        # audiovisuales = 2
        # musicales = 3
        # software = 4
        # otro = 0
    tipo_producto = sqla.Column(sqla.VARCHAR(len("audiovisuales") + 2))
    registro = sqla.Column(sqla.Text)
    fecha =  sqla.Column(sqla.VARCHAR(10))
    period_spam = sqla.Column(sqla.VARCHAR(10), nullable=False)

class DireccionTesis(db.Base):
    '''
    4.10 DIRECCIÓN DE TESIS O TRABAJOS DE GRADO
    '''
    __tablename__ = 'direccion_tesis'

    id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True)
    id_person = sqla.Column(sqla.Integer, sqla.ForeignKey('persons.id'))
    index_entry = sqla.Column(sqla.Integer, nullable=False)
    titulo = sqla.Column(sqla.Text)
    estudiante = sqla.Column(sqla.Text)
    # responde a la pregunta: nivel de formacion
        # pregrado = 1
        # maestria = 2
        # doctorado = 3
    nivel_formacion = sqla.Column(sqla.VARCHAR(len("doctorado") + 2))
        # licenciatura_en_musica = 1
        # artes_plasticas = 2
        # arte_dramatico = 3
        # danza = 4
        # musica = 5
    programa = sqla.Column(sqla.VARCHAR(len("licenciatura_en_musica") + 2))
    # responde a la pregunta: estado actual del trabajo
        # en_proceso = 1
        # esperando_sustentacion = 2
        # finalizado = 3
    status = sqla.Column(sqla.VARCHAR(len("sustentacion") + 2))
    period_spam = sqla.Column(sqla.VARCHAR(10), nullable=False)

class EvaluacionTesis(db.Base):
    '''
    4.11 EVALUACIÓN DE TESIS O TRABAJOS DE GRADO
    '''
    __tablename__ = 'evaluacion_tesis'

    id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True)
    id_person = sqla.Column(sqla.Integer, sqla.ForeignKey('persons.id'))
    index_entry = sqla.Column(sqla.Integer, nullable=False)
    titulo = sqla.Column(sqla.Text)
    estudiante = sqla.Column(sqla.Text)
    # responde a la pregunta: nivel de formacion
        # pregrado = 1
        # maestria = 2
        # doctorado = 3
    nivel_formacion = sqla.Column(sqla.VARCHAR(len("doctorado") + 2))
        # licenciatura_en_musica = 1
        # artes_plasticas = 2
        # arte_dramatico = 3
        # danza = 4
        # musica = 5
    programa = sqla.Column(sqla.VARCHAR(len("licenciatura_en_musica") + 2))
    period_spam = sqla.Column(sqla.VARCHAR(10), nullable=False)

class CoordSemilleros(db.Base):
    '''
    4.12 CREACIÓN, GESTIÓN Y COORDINACIÓN DE SEMILLEROS DE INVESTIGACIÓN
    '''
    __tablename__ = 'coordinacion_semilleros'

    id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True)
    id_person = sqla.Column(sqla.Integer, sqla.ForeignKey('persons.id'))
    index_entry = sqla.Column(sqla.Integer, nullable=False)
    semillero = sqla.Column(sqla.Text)
    total_integrantes = sqla.Column(sqla.VARCHAR(4))
    nuevos_integrantes = sqla.Column(sqla.VARCHAR(4))
        # art = 'ARTE – ACCIÓN'
        # sam = 'Sapiencia, Arte y Música (S.A.M.)'
        # fel = 'Feliza Bursztyn: Redes, Arte, Cultura'
        # vid = 'Investigaciones Visuales del Caribe VIDENS'
        # tei = 'Teatro, Espacio e Interactividad _TEI_'
    grupo = sqla.Column(sqla.VARCHAR(len("arte-accion") + 2))
        # licenciatura_en_musica = 1
        # artes_plasticas = 2
        # arte_dramatico = 3
        # danza = 4
        # musica = 5
    programa = sqla.Column(sqla.VARCHAR(len("licenciatura_en_musica") + 2))
    # responde a al pregunta: Actualizado en RedSIA en el semestre actual (Si o No)
    update_sia = sqla.Column(sqla.VARCHAR(2))
    period_spam = sqla.Column(sqla.VARCHAR(10), nullable=False)
    
class ConvocatoriasSemilleros(db.Base):
    '''
    4.13 PARTICIPACIÓN EN CONVOCATORIAS DE SEMILLEROS DE INVESTIGACIÓN
    '''
    __tablename__ = 'convocatorias_semilleros'

    id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True)
    id_person = sqla.Column(sqla.Integer, sqla.ForeignKey('persons.id'))
    index_entry = sqla.Column(sqla.Integer, nullable=False)
    semillero = sqla.Column(sqla.Text)
    #respose a la pregunta: Tipo de convocatoria
        # interna = 1
        # externa = 2
    tipo_convovatoria = sqla.Column(sqla.VARCHAR(len("externa") + 2))
    # responde a la pregunta: Nombre convocatoria
    nombre = sqla.Column(sqla.Text)
    # responde a la pregunta: Nombre del proyecto
    proyecto = sqla.Column(sqla.Text)
    participantes = sqla.Column(sqla.Text)
    fecha =  sqla.Column(sqla.VARCHAR(10))
    observaciones = sqla.Column(sqla.Text)
    period_spam = sqla.Column(sqla.VARCHAR(10), nullable=False)

class MovilidadEstudiantesSemilleros(db.Base):
    '''
    4.14 MOVILIDAD REGIONAL, NACIONAL E INTERNACIONAL DE ESTUDIANTES Y SEMILLEROS DE INVESTIGACIÓN
    '''
    __tablename__ = 'movilidad_estudiantes_semilleros'

    id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True)
    id_person = sqla.Column(sqla.Integer, sqla.ForeignKey('persons.id'))
    index_entry = sqla.Column(sqla.Integer, nullable=False)
    semillero = sqla.Column(sqla.Text)
    evento = sqla.Column(sqla.Text)
    proyecto = sqla.Column(sqla.Text)
    lugar = sqla.Column(sqla.Text)
    fecha =  sqla.Column(sqla.VARCHAR(10))
    estudiante = sqla.Column(sqla.Text)
    period_spam = sqla.Column(sqla.VARCHAR(10), nullable=False)

class JovenesInvestigadores(db.Base):
    '''
    4.15 JÓVENES INVESTIGADORES APOYADOS PARA SU FORMACIÓN 
    '''
    __tablename__ = 'jovenes_investigadores'

    id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True)
    id_person = sqla.Column(sqla.Integer, sqla.ForeignKey('persons.id'))
    index_entry = sqla.Column(sqla.Integer, nullable=False)
    convocatoria = sqla.Column(sqla.Text)
    estudiante = sqla.Column(sqla.Text)
    programa = sqla.Column(sqla.VARCHAR(len("licenciatura_en_musica") + 2))
    period_spam = sqla.Column(sqla.VARCHAR(10), nullable=False)

class OtrasInvestigacion(db.Base):
    '''
    4.16 OTRAS ACTIVIDADES DE INVESTIGACIÓN, EXTENSIÓN O CREACIÓN
    '''
    __tablename__ = 'otras_investigacion'

    id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True)
    id_person = sqla.Column(sqla.Integer, sqla.ForeignKey('persons.id'))
    index_entry = sqla.Column(sqla.Integer, nullable=False)
    # responde a la pregunta: Tipo de actividad que puede ser 
        # par = 'participacion como par evaluador (incluyendo par evaluador de redcolsi)'
        # red = 'participacion en redes de investigacion'
        # edi = 'participacion en comites editoriales de revistas especializadas'
        # ctf = 'organizacion de evento cientifico'
        # dis = 'diseno de cursos de pregrado, maestria y/o doctorado'
        # ppp = 'participacion en elaboracion de propuestas o proyectos de politicas publicas'
        # frt = 'actividades para el fortalecimiento de capacidades emprendedoras'
    tipo_actividad = sqla.Column(sqla.VARCHAR(len("fortalecimiento") + 2))
    # responde a la pregunta: Nombre del producto, red, evento, curso, etc.
    nombre = sqla.Column(sqla.Text)
    institucion = sqla.Column(sqla.Text)
    actividades = sqla.Column(sqla.Text)
    # responde a la pregunta: Observaciones y/o detalles adicionales
    detalles = sqla.Column(sqla.Text)
    # Respuesta a la pregunta: Observaciones generales
    period_spam = sqla.Column(sqla.VARCHAR(10), nullable=False)

class OtrasRecursos(db.Base):
    '''
    4.17 OTRAS ACTIVIDADES RELACIONADAS CON RECURSOS, ESTRATEGIAS Y CAPACITACIONES
    '''
    __tablename__ = 'otras_recursos'

    id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True)
    id_person = sqla.Column(sqla.Integer, sqla.ForeignKey('persons.id'))
    index_entry = sqla.Column(sqla.Integer, nullable=False)
    # responde a la pregunta: Tipo de actividad
        # dig = 'recursos digitales creados disponibles en el repositorio institucional de la biblioteca digital'
        # per = 'diseno o participacion en estrategias academico-administrativas de acompanamiento para la permanencia y graduacion oportuna'
        # nia = 'actividades con componente nacional / internacional en el aula de clases (clases espejo, etc).'
        # ccd = 'participacion en capacitaciones en competencias digitales'
        # cip = 'participacion en capacitaciones en tematicas relacionadas con educacion inclusiva, interculturalidad y pluridiversidad'
    tipo_actividad = sqla.Column(sqla.VARCHAR(len("participacion") + 2))
    # responde a la pregunta: Nombre del recurso, estrategia, actividad o capacitación
    nombre = sqla.Column(sqla.Text)
    # responde a la pregunta: Programa
    programa = sqla.Column(sqla.VARCHAR(len("licenciatura_en_musica") + 2))
    asignatura = sqla.Column(sqla.Text)
    fecha =  sqla.Column(sqla.VARCHAR(10))
    finalizado =  sqla.Column(sqla.VARCHAR(2))
    # responde a la pregunta: Alcance
        # nacional = 1
        # internacional = 2
    alcance = sqla.Column(sqla.VARCHAR(len("internacional") + 2))
    impacto = sqla.Column(sqla.Text)
    # responde a la pregunta: observaciones y/o detalles adicionales sobre el ítem
    detalles = sqla.Column(sqla.Text)
    ofertado = sqla.Column(sqla.Text)
    period_spam = sqla.Column(sqla.VARCHAR(10), nullable=False)

class PropuestasEducacion(db.Base):
    '''
    5.1 PROPUESTAS DE EDUCACIÓN CONTÍNUA PRESENTADAS
    '''
    __tablename__ = 'propuestas_educacion'

    id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True)
    id_person = sqla.Column(sqla.Integer, sqla.ForeignKey('persons.id'))
    index_entry = sqla.Column(sqla.Integer, nullable=False)
    # responde a la pregunta: nombre de la propuesta
    nombre = sqla.Column(sqla.Text)
    # responde a la pregunta: tipo Curso
        # taller = 1
        # seminario = 2
        # diplomado = 3
        # otro = 4
    tipo_propuesta = sqla.Column(sqla.VARCHAR(len("diplomado") + 2))
    fecha_inicio =  sqla.Column(sqla.VARCHAR(10))
    fecha_fin =  sqla.Column(sqla.VARCHAR(10))
    # responde a la pregunta: modalidad
        # presencial = 1
        # semipresencial = 2
        # virtual = 3
        # distancia = 4
    modalidad = sqla.Column(sqla.VARCHAR(len("semipresencial") + 2))
    # responde a la pregunta: ¿La propuesta incluye componente internacional? si/no
    internacional =  sqla.Column(sqla.VARCHAR(2))
    # responde a la pregunta: ¿Atiende a población diferencial?
        # si la respuesta es si esta entrada contiene el nombre de la poblacion
        # si la respuesta es no esta entrada esta vacia
    bool_diferencial =  sqla.Column(sqla.VARCHAR(2))
    diferencial = sqla.Column(sqla.Text)
    # responde a la pregunta: ¿Es realizada en convenio con otra entidad del sector público o privado?
        # si al respuesta es si esta entrada contiene el nombre de la entidad
        # si la respuesta es no esta entrada esta vacia
    bool_entidad =  sqla.Column(sqla.VARCHAR(2))
    entidad = sqla.Column(sqla.Text)
    period_spam = sqla.Column(sqla.VARCHAR(10), nullable=False)

class GestionConvenios(db.Base):
    '''
    5.2 GESTIÓN DE CONVENIOS O ALIANZAS PARA ACCESO A LA CULTURA
    '''
    __tablename__ = 'gestion_convenios'

    id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True)
    id_person = sqla.Column(sqla.Integer, sqla.ForeignKey('persons.id'))
    index_entry = sqla.Column(sqla.Integer, nullable=False)
    entidad = sqla.Column(sqla.Text)
    actividades = sqla.Column(sqla.Text)
    # responde a la pregunta: tipo de vinculo
        # convenio = 1
        # alianza = 2
        # carta_intencion = 3
        # otro = 4
    tipo_vinculo = sqla.Column(sqla.VARCHAR(len("carta_intencion") + 2))
    # responde a la pregunta: Población beneficiada
        # estudiantes = 1
        # docentes = 2
        # administrativo = 3
    beneficiarios = sqla.Column(sqla.VARCHAR(len("administrativo") + 2))
    period_spam = sqla.Column(sqla.VARCHAR(10), nullable=False)

class ProyeccionPoblacionPriorizada(db.Base):
    '''
    5.3 PROYECTOS DE PROYECCIÓN SOCIAL EJECUTADOS CON INTERVENCIÓN EN POBLACIÓN PRIORIZADA, CON ENFOQUE DIFERENCIAL Y/O CAPACIDADES DIVERSAS   
    '''
    __tablename__ = 'proyeccion_poblacion_priorizada'

    id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True)
    id_person = sqla.Column(sqla.Integer, sqla.ForeignKey('persons.id'))
    index_entry = sqla.Column(sqla.Integer, nullable=False)
    nombre_proyecto = sqla.Column(sqla.Text)
    fecha_inicio =  sqla.Column(sqla.VARCHAR(10))
    # responde a la pregunta: Población beneficiada
        # estudiantes = 1
        # docentes = 2
        # administrativo = 3
    beneficiarios = sqla.Column(sqla.VARCHAR(len("administrativo") + 2))
    # responde a la pregunta: Docentes o estudiantes participantes (si aplica)
    participantes = sqla.Column(sqla.Text)
    period_spam = sqla.Column(sqla.VARCHAR(10), nullable=False)

class AsignacionMisionalBienestar(db.Base):
    '''
    6.1 ASIGNACIÓN MISIONAL DE BIENESTAR SEGÚN PTA
    '''
    __tablename__ = 'asignacion_misional_bienestar'

    id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True)
    id_person = sqla.Column(sqla.Integer, sqla.ForeignKey('persons.id'))
    index_entry = sqla.Column(sqla.Integer, nullable=False)
    representante_misional = sqla.Column(sqla.VARCHAR(2))
    tutor_rendimiento = sqla.Column(sqla.VARCHAR(2))
    tutor_SAT = sqla.Column(sqla.VARCHAR(2))
    coordinador = sqla.Column(sqla.VARCHAR(2))
    period_spam = sqla.Column(sqla.VARCHAR(10), nullable=False)

class AtendidosBajoRendimiento(db.Base):
    '''
    6.2 TUTORÍAS Y ESTUDIANTES ATENDIDOS DESDE BIENESTAR - BAJO RENDIMIENTO
    '''
    __tablename__ = 'atendidos_bajo_rendimiento'

    id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True)
    id_person = sqla.Column(sqla.Integer, sqla.ForeignKey('persons.id'))
    index_entry = sqla.Column(sqla.Integer, nullable=False)
    nombre_persona = sqla.Column(sqla.Text)
    superado = sqla.Column(sqla.VARCHAR(2))
    remision = sqla.Column(sqla.VARCHAR(2))
    observaciones = sqla.Column(sqla.Text)
    name_file = sqla.Column(sqla.Text)
    period_spam = sqla.Column(sqla.VARCHAR(10), nullable=False)

class AtendidosSAT(db.Base):
    '''
    6.3 TUTORÍAS Y ESTUDIANTES ATENDIDOS DESDE BIENESTAR - TUTORIAS SAT
    '''
    __tablename__ = 'atendidos_tutorias_sat'

    id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True)
    id_person = sqla.Column(sqla.Integer, sqla.ForeignKey('persons.id'))
    index_entry = sqla.Column(sqla.Integer, nullable=False)
    nombre_persona = sqla.Column(sqla.Text)
    superado = sqla.Column(sqla.VARCHAR(2))
    remision = sqla.Column(sqla.VARCHAR(2))
    observaciones = sqla.Column(sqla.Text)
    name_file = sqla.Column(sqla.Text)
    period_spam = sqla.Column(sqla.VARCHAR(10), nullable=False)

class AtendidosMateriaUnica(db.Base):
    '''
    6.4 TUTORÍAS Y ESTUDIANTES ATENDIDOS DESDE BIENESTAR - MATERIA UNICA
    '''
    __tablename__ = 'atendidos_materia_unica'

    id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True)
    id_person = sqla.Column(sqla.Integer, sqla.ForeignKey('persons.id'))
    index_entry = sqla.Column(sqla.Integer, nullable=False)
    nombre_persona = sqla.Column(sqla.Text)
    superado = sqla.Column(sqla.VARCHAR(2))
    remision = sqla.Column(sqla.VARCHAR(2))
    observaciones = sqla.Column(sqla.Text)
    name_file = sqla.Column(sqla.Text)
    period_spam = sqla.Column(sqla.VARCHAR(10), nullable=False)

class DesercionCasosGenerales(db.Base):
    '''
    6.5 TUTORÍAS Y ESTUDIANTES ATENDIDOS DESDE BIENESTAR - DESERCION CASOS GENERALES
    '''
    __tablename__ = 'desercion_casos_generales'

    id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True)
    id_person = sqla.Column(sqla.Integer, sqla.ForeignKey('persons.id'))
    index_entry = sqla.Column(sqla.Integer, nullable=False)
    nombre_persona = sqla.Column(sqla.Text)
    detalles = sqla.Column(sqla.Text)
    estrategias = sqla.Column(sqla.Text)
    observaciones = sqla.Column(sqla.Text)
    period_spam = sqla.Column(sqla.VARCHAR(10), nullable=False)

class DesercionGraduacion(db.Base):
    '''
    6.6 TUTORÍAS Y ESTUDIANTES ATENDIDOS DESDE BIENESTAR - DESERCION POR GRADUACION
    '''
    __tablename__ = 'desercion_por_graduacion'

    id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True)
    id_person = sqla.Column(sqla.Integer, sqla.ForeignKey('persons.id'))
    index_entry = sqla.Column(sqla.Integer, nullable=False)
    nombre_persona = sqla.Column(sqla.Text)
    detalles = sqla.Column(sqla.Text)
    estrategias = sqla.Column(sqla.Text)
    observaciones = sqla.Column(sqla.Text)
    period_spam = sqla.Column(sqla.VARCHAR(10), nullable=False)

class AtendidosCasosEspeciales(db.Base):
    '''
    6.7 TUTORÍAS Y ESTUDIANTES ATENDIDOS DESDE BIENESTAR - CASOS ESPECIALES
    '''
    __tablename__ = 'atendidos_casos_especiales'

    id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True)
    id_person = sqla.Column(sqla.Integer, sqla.ForeignKey('persons.id'))
    index_entry = sqla.Column(sqla.Integer, nullable=False)
    nombre_persona = sqla.Column(sqla.Text)
    detalles = sqla.Column(sqla.Text)
    remision = sqla.Column(sqla.VARCHAR(2))
    observaciones = sqla.Column(sqla.Text)
    name_file = sqla.Column(sqla.Text)
    period_spam = sqla.Column(sqla.VARCHAR(10), nullable=False)


db.Base.metadata.create_all(bind=db.engine)
