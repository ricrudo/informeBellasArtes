from app.interface import db
from app.interface.db import db_manager, clean_data
from app.domain.models import MovilidadEstudiantesSemilleros

import json

'''
{"semillero": null, "evento": null, "proyecto": null, "lugar": null, "fecha": null, "estudiante": [""]}
'''


def new_entry_user(initform:dict):
    #if not db.is_real_person(id_person):
    #    return 'No existe persona con el id indicado'
    index_used = []
    error = []
    for index_entry, content in initform['section4_14'].items():
        if index_entry == 'activateQuestionsection4_14':
            continue
        index_used.append(int(index_entry))
        if len(content) != 6:
            error.append(f'Error: se han enviado {len(content)} datos. Se esperaban 6 datos.')
            continue
        if not all([x in content for x in (['semillero', 'evento', 'proyecto', 'lugar', 'fecha', 'estudiante'])]):
            error.append(f'Los keys no corresponden a los que recibe la base de datos.')
            continue
        estudiantes = clean_data.getActualParticipant(content['estudiante'])
        content['estudiante'] = json.dumps(estudiantes)
        content['user'] = initform['user']
        content['period_spam'] = initform['period_spam']
        content['index_entry'] = int(index_entry)
        _send_to_DB(content)
    db_manager._delete_entries(index_used, initform['user'], initform['period_spam'], MovilidadEstudiantesSemilleros)
    db.session.close()
    if error:
        return error
    return 'ok'

def _create_entry(form:dict):
    entry = MovilidadEstudiantesSemilleros(
        id_person = form['user'],
        index_entry = form['index_entry'],
        semillero = form['semillero'],
        evento = form['evento'],
        proyecto = form['proyecto'],
        lugar = form['lugar'],
        fecha = form['fecha'],
        estudiante = form['estudiante'],
        period_spam = form['period_spam']
    )
    db.session.add(entry)
    db.session.commit()

def _send_to_DB(content:dict):
    entry = db_manager._check_entry(content, MovilidadEstudiantesSemilleros)
    if entry:
        db_manager._update_entry(entry, content)
    else:
        _create_entry(content)

