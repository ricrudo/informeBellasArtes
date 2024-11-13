import enum

class PartProcesosNames(enum.Enum):
    autoevaluacion = 1
    acreditacion = 2
    curricular = 3
    estudio = 4
    disciplinar = 5
    silabos = 6
    grado = 7
    misional = 8
    oportuna = 9
    nuevos = 10
    facultad = 11

class PartProcesosProMis(enum.Enum):
    program = 1
    misional = 2

class ProgramasFacultad(enum.Enum):
    licenciatura_en_musica = 1
    artes_plasticas = 2
    arte_dramatico = 3
    danza = 4
    musica = 5

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

class OtrasInvestigacionTipo(enum.Enum):
    par = 'participacion como par evaluador (incluyendo par evaluador de redcolsi)'
    red = 'participacion en redes de investigacion'
    edi = 'participacion en comites editoriales de revistas especializadas'
    ctf = 'organizacion de evento cientifico'
    dis = 'diseno de cursos de pregrado, maestria y/o doctorado'
    ppp = 'participacion en elaboracion de propuestas o proyectos de politicas publicas'
    frt = 'actividades para el fortalecimiento de capacidades emprendedoras'

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

class GruposInvesFacultad(enum.Enum):
    art = 'ARTE – ACCIÓN'
    sam = 'Sapiencia, Arte y Música (S.A.M.)'
    fel = 'Feliza Bursztyn: Redes, Arte, Cultura'
    vid = 'Investigaciones Visuales del Caribe VIDENS'
    tei = 'Teatro, Espacio e Interactividad _TEI_'
