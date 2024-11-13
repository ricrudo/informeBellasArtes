from app.interface import db
from app.interface.db import db_manager, clean_data
from app.domain.models import ConvocatoriasSemilleros

import json

'''
{"semillero": null, "tipo_convovatoria": null, "nombre": null, "proyecto": null, "participantes": [""], "fecha": null, "observaciones": null}
'''


def new_entry_user(initform:dict):
    #if not db.is_real_person(id_person):
    #    return 'No existe persona con el id indicado'
    index_used = []
    error = []
    for index_entry, content in initform['section4_13'].items():
        if index_entry == 'activateQuestionsection4_13':
            continue
        index_used.append(int(index_entry))
        if len(content) != 7:
            error.append(f'Error: se han enviado {len(content)} datos. Se esperaban 7 datos.')
            continue
        if not all([x in content for x in (['semillero', 'tipo_convovatoria', 'nombre', 'proyecto', 'participantes', 'fecha', 'observaciones'])]):
            error.append(f'Los keys no corresponden a los que recibe la base de datos.')
            continue
        participantes = clean_data.getActualParticipant(content['participantes'])
        content['participantes'] = json.dumps(participantes)
        content['user'] = initform['user']
        content['period_spam'] = initform['period_spam']
        content['index_entry'] = int(index_entry)
        _send_to_DB(content)
    db_manager._delete_entries(index_used, initform['user'], initform['period_spam'], ConvocatoriasSemilleros)
    db.session.close()
    if error:
        return error
    return 'ok'

def _create_entry(form:dict):
    entry = ConvocatoriasSemilleros(
        id_person = form['user'],
        index_entry = form['index_entry'],
        semillero = form['semillero'],
        tipo_convovatoria = form['tipo_convovatoria'],
        nombre = form['nombre'],
        proyecto = form['proyecto'],
        participantes = form['participantes'],
        fecha = form['fecha'],
        observaciones = form['observaciones'],
        period_spam = form['period_spam']
    )
    db.session.add(entry)
    db.session.commit()

def _send_to_DB(content:dict):
    entry = db_manager._check_entry(content, ConvocatoriasSemilleros)
    if entry:
        db_manager._update_entry(entry, content)
    else:
        _create_entry(content)

