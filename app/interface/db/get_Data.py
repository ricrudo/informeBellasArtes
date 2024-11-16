from app.interface import db
from app.interface.db import db_manager
from app.domain import models
import json

NEEDACTIVEQUESTION = ('section4_1', 'section4_3', 'section4_4', 'section4_5', 'section4_6', 'section4_7', 'section4_8', 'section4_9', 'section4_10', 'section4_11', 'section4_12', 'section4_13', 'section4_14', 'section4_15', 'section4_16', 'section4_17', 'section5_1', 'section5_2', 'section5_3', 'section6_2', 'section6_3', 'section6_4', 'section6_5', 'section6_6', 'section6_7')

def getTables(section=None):
    tables = {
    'section1_1' : models.Person,
    'section2_1' : models.MisionalDocenciaPTA,
    'section2_2' : models.MisionalDocenciaAdicionales,
    'section3_1' : models.Part_ProcesosCurriculares,
    'section4_1' : models.GruposInvestigacion,
    'section4_2' : models.RedesAcademicas,
    'section4_3' : models.ProyectosInvestigacionCreacion,
    'section4_4' : models.ProductosCreacion,
    'section4_5' : models.PublicacionArticulos,
    'section4_6' : models.PublicacionLibros,
    'section4_7' : models.ParticipacionEventos,
    'section4_8' : models.ConveniosInterinstitucionales,
    'section4_9' : models.Patentes,
    'section4_10' : models.DireccionTesis,
    'section4_11' : models.EvaluacionTesis,
    'section4_12' : models.CoordSemilleros,
    'section4_13' : models.ConvocatoriasSemilleros,
    'section4_14' : models.MovilidadEstudiantesSemilleros,
    'section4_15' : models.JovenesInvestigadores,
    'section4_16' : models.OtrasInvestigacion,
    'section4_17' : models.OtrasRecursos,
    'section5_1' : models.PropuestasEducacion,
    'section5_2' : models.GestionConvenios,
    'section5_3' : models.ProyeccionPoblacionPriorizada,
    'section6_1' : models.AsignacionMisionalBienestar,
    'section6_2' : models.AtendidosBajoRendimiento,
    'section6_3' : models.AtendidosSAT,
    'section6_4' : models.AtendidosMateriaUnica,
    'section6_5' : models.DesercionCasosGenerales,
    'section6_6' : models.DesercionGraduacion,
    'section6_7' : models.AtendidosCasosEspeciales,
    'activesections' : models.ActiveSections,
    }
    if section is None:
        return tables
    elif section == 'section2_1':
        return tables['section2_1'], tables['section2_2']
    result = tables.get(section, f"la seccion {section} no existe")
    if not isinstance(result, str):
        return [result]


def getAllData(section):
    tables = getTables(section)
    if isinstance(tables, str):
        return tables
    result = {}
    for table in tables:
        name = table.__tablename__
        result[name] = []
        data = db.session.query(table).all()
        for record in data:
            entry = {}
            for field in dir(record):
                if field.startswith("_") or field in ('registry', 'metadata'):
                    continue
                entry[field] = getattr(record, field)
            result[name].append(entry)
    return result

def getAllDataUser(id_person, period_spam):
    content = {}
    activateQuestions = getActivateQuestion(id_person, period_spam)
    for section, table in getTables().items():
        if section in ['section1_1', 'activesections']:
            data = db.session.query(table).filter(table.id == id_person).first()
        else:
            data = db.session.query(table).filter(
                table.id_person == id_person,
                table.period_spam == period_spam,
            ).all()
        if not data and section in NEEDACTIVEQUESTION and activateQuestions:
            content[section] = formatNoDataforActiveQuestion(section, activateQuestions)
        if data:
            content[section] = formatData(data, section, activateQuestions)

    return json.dumps(content)

def formatNoDataforActiveQuestion(section, activateQuestions):
    entries = dict()
    entries['answers'] = {}
    entries['activateQuestion'] = getattr(activateQuestions, f'activateQuestion{section}')
    return entries


def formatData(data, section, activateQuestions):
    blacklist = ['registry', 'metadata']
    if section == 'section1_1':
        blacklist.extend(['id', 'admin_role', 'email', 'date_creation'])
        entry = {0:{}}
        for field in dir(data):
            if field.startswith("_") or field in blacklist:
                continue
            entry[0][field] = getattr(data, field)
        return entry
    else:
        blacklist.extend(['id', 'id_person', 'period_spam', 'index_entry'])
        entries = {}
        for record in data:
            index_entry = record.index_entry
            if section == "section3_1":
                entries[index_entry] = organizeSection3_1(record, blacklist)
            elif section == "section4_2":
                entries[index_entry] = organizeSection4_2(record, blacklist)
            else:
                entries[index_entry] = {}
                for field in dir(record):
                    if field.startswith("_") or field in blacklist:
                        continue
                    entries[index_entry][field] = getattr(record, field)
            if section == "section4_1":
                entries[index_entry]['linea_investiga'] = json.loads(entries[index_entry]['linea_investiga'])
            elif section in ["section4_3", "section4_10", "section4_11", "section4_14", "section4_15"]:
                entries[index_entry]['estudiante'] = formatParticipantes(entries[index_entry]['estudiante'])
            elif section in ["section4_5", "section4_6"]:
                entries[index_entry]['autores'] = formatParticipantes(entries[index_entry]['autores'])
            elif section in ["section4_7", "section4_13", "section5_3"]:
                entries[index_entry]['participantes'] = formatParticipantes(entries[index_entry]['participantes'])
        if section in NEEDACTIVEQUESTION:
            answers = {key: value for key, value in entries.items()}
            entries = dict()
            entries['answers'] = answers
            entries['activateQuestion'] = getattr(activateQuestions, f'activateQuestion{section}')
        return entries

def formatParticipantes(content):
    result = json.loads(content)
    if not result:
        result.append("")
    return result

def organizeSection3_1(record, blacklist):
    blacklist.append('proceso')
    proceso = record.proceso
    entry = {}
    for field in dir(record):
        if field.startswith("_") or field in blacklist:
            continue
        entry[f'{field}{proceso}'] = getattr(record, field)
    return entry

def getActivateQuestion(id_person, period_spam):
    data = db.session.query(models.ActiveSections).filter(
        models.ActiveSections.id_person == id_person,
        models.ActiveSections.period_spam == period_spam,
    ).first()
    return data

def organizeSection4_2(record, blacklist):
    #status_cvlac: null, link_cvlac: null, update_cvlac: null
    name_red = record.name_red
    entry = {}
    entry[f'status_{name_red}'] = record.status
    entry[f'link_{name_red}'] = record.link
    entry[f'update_{name_red}'] = record.update_date
    return entry




    

