from app.interface import db
from app.interface.db import db_manager
from app.domain.models import OtrasRecursos

import json

'''
  '{"tipo_actividad": null, "nombre": null, "programa": null, "asignatura": null, "fecha": null, "finalizado": null, "alcance": null, "impacto": null, "detalles": null}'
'''


def new_entry_user(initform:dict):
    #if not db.is_real_person(id_person):
    #    return 'No existe persona con el id indicado'
    index_used = []
    error = []
    for index_entry, content in initform['section4_17'].items():
        if index_entry == 'activateQuestionsection4_17':
            continue
        index_used.append(int(index_entry))
        if len(content) != 10:
            error.append(f'Error: se han enviado {len(content)} datos. Se esperaban 10 datos.')
            continue
        if not all([x in content for x in (['tipo_actividad', 'nombre', 'programa', 'asignatura', 'fecha', 'finalizado', 'alcance', 'impacto', 'detalles', 'ofertado'])]):
            error.append(f'Los keys no corresponden a los que recibe la base de datos.')
            continue
        if content['tipo_actividad'] != 'actividades':
            content['alcance'] = None
        if content['tipo_actividad'] not in ['creacion', 'design']:
            content['programa'] = None
            content['asignatura'] = None
            content['fecha'] = None
        if content['tipo_actividad'] not in ['participacion', 'capacitacion']:
            content['finalizado'] = None
            content['ofertado'] = None
        content['user'] = initform['user']
        content['period_spam'] = initform['period_spam']
        content['index_entry'] = int(index_entry)
        _send_to_DB(content)
    db_manager._delete_entries(index_used, initform['user'], initform['period_spam'], OtrasRecursos)
    db.session.close()
    if error:
        return error
    return 'ok'

def _create_entry(form:dict):
    entry = OtrasRecursos(
        id_person = form['user'],
        index_entry = form['index_entry'],
        tipo_actividad = form['tipo_actividad'],
        nombre = form['nombre'],
        programa = form['programa'],
        asignatura = form['asignatura'],
        fecha = form['fecha'],
        finalizado = form['finalizado'],
        alcance = form['alcance'],
        impacto = form['impacto'],
        detalles = form['detalles'],
        ofertado = form['ofertado'],
        period_spam = form['period_spam']
    )
    db.session.add(entry)
    db.session.commit()

def _send_to_DB(content:dict):
    entry = db_manager._check_entry(content, OtrasRecursos)
    if entry:
        db_manager._update_entry(entry, content)
    else:
        _create_entry(content)

