from app.interface import db
from app.interface.db import db_manager, clean_data, filesManager
from app.domain.models import ParticipacionEventos

import json

'''
{"titulo": null, "evento": null, "lugar": null, "fecha": null, "tipo_participacion": null, "modalidad": null, "aprobado": null, "name_file": null, "bool_semillero": null, "semillero": null, "participantes": [""], "movilidad": null}
'''


def new_entry_user(initform:dict):
    #if not db.is_real_person(id_person):
    #    return 'No existe persona con el id indicado'
    index_used = []
    error = []
    for index_entry, content in initform['section4_7'].items():
        if index_entry == 'activateQuestionsection4_7':
            continue
        index_used.append(int(index_entry))
        if len(content) != 12:
            error.append(f'Error: se han enviado {len(content)} datos. Se esperaban 12 datos.')
            continue
        if not all([x in content for x in (['titulo', 'evento', 'lugar', 'fecha', 'tipo_participacion', 'modalidad', 'aprobado', 'name_file', 'bool_semillero', 'semillero', 'participantes', 'movilidad'])]):
            error.append(f'Los keys no corresponden a los que recibe la base de datos.')
            continue
        participantes = clean_data.getActualParticipant(content['participantes'])
        content['participantes'] = json.dumps(participantes)
        content['name_file'] = filesManager.saveFile('section4_7', index_entry, initform)
        content['user'] = initform['user']
        content['period_spam'] = initform['period_spam']
        content['index_entry'] = int(index_entry)
        _send_to_DB(content)
    db_manager._delete_entries(index_used, initform['user'], initform['period_spam'], ParticipacionEventos)
    db.session.close()
    if error:
        return error
    return 'ok'

def _create_entry(form:dict):
    entry = ParticipacionEventos(
        id_person = form['user'],
        index_entry = form['index_entry'],
        titulo = form['titulo'],
        evento = form['evento'],
        lugar = form['lugar'],
        fecha = form['fecha'],
        tipo_participacion = form['tipo_participacion'],
        modalidad = form['modalidad'],
        aprobado = form['aprobado'],
        name_file = form['name_file'],
        bool_semillero = form['bool_semillero'],
        semillero = form['semillero'],
        participantes = form['participantes'],
        movilidad = form['movilidad'],
        period_spam = form['period_spam']
    )
    db.session.add(entry)
    db.session.commit()

def _send_to_DB(content:dict):
    entry = db_manager._check_entry(content, ParticipacionEventos)
    if entry:
        db_manager._update_entry(entry, content)
    else:
        _create_entry(content)

