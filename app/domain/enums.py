import enum

class PartProcesosNames(enum.Enum):
    autoevaluacion = "Proceso de Autoevaluación"
    acreditacion = "Apoyo a proceso de acreditación"
    curricular = "Comité Curricular de Programa"
    estudio = "Modificación de planes de estudio"
    disciplinar = "Comité de área disciplinar del Programa"
    silabos = "Revisión o actualización de sílabos"
    grado = "Comité de trabajo de grado"
    misional = "Comité misional de la Facultad"
    oportuna = "Estrategias implementadas para la graduación oportuna"
    nuevos = "Creación de nuevos Programas de Pregrado y/o Postgrado"
    facultad = "Participación en el Consejo de Facultad"
    virtuales = "Diseño de cursos virtuales"
    factibilidad = "Estudios de factibilidd de programas académicos postgraduales"

class PartProcesosProMis(enum.Enum):
    program = 1
    misional = 2

class ProgramasFacultad(enum.Enum):
    licenciatura_en_musica = "Licenciatura en música"
    artes_plasticas = "Artes plásticas"
    arte_dramatico = "Arte dramático"
    danza = "Danza"
    musica = "Música"

class MisionalesFacultad(enum.Enum):
    mis_curricular = "Comité Misional Curricular"
    mis_investigacion = "Comité misional de investigación"
    mis_extension = "Comité misional de extensión"
    mis_bienestar = "Comité misional bienestar"
    mis_artistico = "Comité misional artístico"
    mis_trb_grado = "Comité de trabajo de grado"
    mis_autoevaluacion = "Comité de Autoevaluación"

class LineasInvestigacionFacultad(enum.Enum):
    musical = "Creación musical"
    cultura = "Desarrollo y cultura"
    estetica = "Estética"
    pedagogia = "Pedagogía"

class GruposInvesFacultad(enum.Enum):
    arte_accion = "ARTE – ACCIÓN"
    sam = "Sapiencia, Arte y Música (S.A.M.)"
    feliza = "Feliza Bursztyn: Redes, Arte, Cultura"
    videns = "Investigaciones Visuales del Caribe VIDENS"
    tei = "Teatro, Espacio e Interactividad TEI"

class TiposProductoCreacion(enum.Enum):
    gnc = 'Generación de nuevo conocimiento'
    dti = 'Desarrollo tecnológico e innovación'
    asc = 'Apropiación social del conocimiento'
    frh = 'Formación de Recurso Humano en CTeI'


class TipoProductosPatentesRegistroAutor(enum.Enum):
    artistica = "Obras artísticas"
    audiovisuales = "Obras audiovisuales"
    musicales = "Registros musicales"
    software = "Registros de software"
    otro = "Otro"


class OtrasInvestigacionTipoParticipacion(enum.Enum):
    par = "Participación como par evaluador"
    redes = "Participación en redes de investigación"
    editoriales = "Participación en comités editoriales de revistas especializadas"
    cientifico = "Organización de evento científico"
    design = "Diseño de cursos de pregrado, maestría y/o doctorado"
    propuestas = "Elaboración de propuestas o proyectos de políticas públicas"
    fortalecimiento = "Fortalecimiento de capacidades emprendedoras"

class otrasActividades4_17(enum.Enum):
    creacion = "Recursos digitales disponibles en el repositorio institucional"
    design = "Estrategias para la permanencia y graduación oportuna"
    actividades = "Actividades con componente nacional / internacional en el aula de clases"
    participacion = "Capacitaciones en competencias digitales"
    capacitacion = "Capacitaciones relacionadas con educación inclusiva, interculturalidad y pluridiversidad"


##############


class RedesAcademicasNames(enum.Enum):
    cvlac = 'cvl'
    google_scholar = 'ggs'
    researchgate = 'rsg'
    orcid = 'ord'

class ProyectosInvestTipoConv(enum.Enum):
    interna = 1
    externa = 2

class ProductosCreacionAlcance(enum.Enum):
    local = 1
    regional = 2
    nacional = 3
    internacional = 4

class ProductosCreacionCategoria(enum.Enum):
    no_responde = 0
    tipo_a = 1
    tipo_b = 2

class DireccionTesisNivel(enum.Enum):
    pregrado = 1
    maestria = 2
    doctorado = 3

class DireccionTesisStatus(enum.Enum):
    en_proceso = 1
    esperando_sustentacion = 2
    finalizado = 3

class ConvocatoriasSemillerosTipo(enum.Enum):
    interna = 1
    externa = 2


class OtrasRecursosTipo(enum.Enum):
    dig = 'recursos digitales creados disponibles en el repositorio institucional de la biblioteca digital'
    per = 'diseno o participacion en estrategias academico-administrativas de acompanamiento para la permanencia y graduacion oportuna'
    nia = 'actividades con componente nacional / internacional en el aula de clases (clases espejo, etc).'
    ccd = 'participacion en capacitaciones en competencias digitales'
    cip = 'participacion en capacitaciones en tematicas relacionadas con educacion inclusiva, interculturalidad y pluridiversidad'

class OtrasRecursosAlcance(enum.Enum):
    nacional = 1
    internacional = 2

class PropuestasEducacionTipo(enum.Enum):
    otro = 0
    taller = 1
    seminario = 2
    diplomado = 3

class PropuestasEducacionModalidad(enum.Enum):
    presencial = 1
    semipresencial = 2
    virtual = 3
    distancia = 4

class GestionConveniosTipo(enum.Enum):
    otro = 0
    convenio = 1
    alianza = 2
    carta_de_intencion = 3

class GestionConveniosBeneficiarios(enum.Enum):
    estudiantes = 1
    docentes = 2
    personal_administrativo = 3

class ProyeccionPoblacionPriorizadaBeneficiarios(enum.Enum):
    estudiantes = 1
    docentes = 2
    personal_administrativo = 3

class AtendidosBienestarTipo(enum.Enum):
    bjr = 'tutorias de bajo rendimiento'
    sat = 'tutorias de SAT'
    uni = 'estudiantes en materia unica atendidos'
    dsr = 'estudiantes en desercion atendidos casos generales'
    dsg = 'estudiantes en desercion atendidos desercion por graduacion'
    csp = 'relacion de casos especiales presentados en su programa atendidos desde bienestar'

class ProyectosInvestElegido(enum.Enum):
    no = 0
    si = 1
    espera = 2

class ProyectosInvestParticipacion(enum.Enum):
    principal = 1
    co_investigador = 2

class PubliArticIndex(enum.Enum):
    otros = 0
    publindex = 1
    wos = 2
    scopus = 3

class PartEventosModalidad(enum.Enum):
    virtual = 1
    presencial = 2

class PartEventosMovilidad(enum.Enum):
    internacional = 1
    nacional = 2
    regional = 3


class PatenteTipo(enum.Enum):
    otro = 0
    artisticas = 1
    audiovisuales = 2
    musicales = 3
    software = 4

