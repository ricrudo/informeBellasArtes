from app.interface import db
from app.interface.db import db_manager, clean_data
from app.domain.models import ProyectosInvestigacionCreacion

import json

'''
{"nombre_proyecto": null, "code": null, "tipo_convocatoria": null, "nombre_convocatoria": null, "elegido": null, "financiamiento": null, "tipo_participacion": null, "bool_semillero": null, "semillero": null, "estudiante": [""], "ods": null, "software": null, "idi5": null}
'''


def new_entry_user(initform:dict):
    #if not db.is_real_person(id_person):
    #    return 'No existe persona con el id indicado'
    index_used = []
    error = []
    for index_entry, content in initform['section4_3'].items():

        if index_entry == 'activateQuestionsection4_3':
            continue
        index_used.append(int(index_entry))
        if len(content) != 13:
            error.append(f'Error: se han enviado {len(content)} datos. Se esperaban 13 datos.')
            continue
        if not all([x in content for x in (['nombre_proyecto', 'code', 'tipo_convocatoria', 'nombre_convocatoria', 'elegido', 'financiamiento', 'tipo_participacion', 'bool_semillero', 'semillero', 'estudiante', 'ods', 'software', 'idi5'])]):
            error.append(f'Los keys no corresponden a los que recibe la base de datos.')
            continue

        estudiantes = clean_data.getActualParticipant(content['estudiante'])
        content['estudiante'] = json.dumps(estudiantes)
        content['user'] = initform['user']
        content['period_spam'] = initform['period_spam']
        content['index_entry'] = int(index_entry)
        _send_to_DB(content)
    db_manager._delete_entries(index_used, initform['user'], initform['period_spam'], ProyectosInvestigacionCreacion)
    db.session.close()
    if error:
        return error
    return 'ok'

def _create_entry(form:dict):
    entry = ProyectosInvestigacionCreacion(
        id_person = form['user'],
        index_entry = form['index_entry'],
        nombre_proyecto = form['nombre_proyecto'],
        code = form['code'],
        tipo_convocatoria = form['tipo_convocatoria'],
        nombre_convocatoria = form['nombre_convocatoria'],
        elegido = form['elegido'],
        financiamiento = form['financiamiento'],
        tipo_participacion = form['tipo_participacion'],
        bool_semillero = form['bool_semillero'],
        semillero = form['semillero'],
        estudiante = form['estudiante'],
        ods = form['ods'],
        software = form['software'],
        idi5 = form['idi5'],
        period_spam = form['period_spam']
    )
    db.session.add(entry)
    db.session.commit()

def _send_to_DB(content:dict):
    entry = db_manager._check_entry(content, ProyectosInvestigacionCreacion)
    if entry:
        db_manager._update_entry(entry, content)
    else:
        _create_entry(content)

