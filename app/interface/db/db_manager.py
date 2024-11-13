from app.interface import db

def _check_entry(content:dict, table, index_entry=True):
    # Realiza la consulta
    if index_entry:
        result = db.session.query(table).filter(
            table.id_person == content['user'],
            table.index_entry == content['index_entry'],
            table.period_spam == content['period_spam']
        ).first()  # `first()` devuelve el primer resultado o None si no hay coincidencias
    else:
        result = db.session.query(table).filter(
            table.id_person == content['user'],
            table.period_spam == content['period_spam']
        ).first()  # `first()` devuelve el primer resultado o None si no hay coincidencias
    return result  # Devuelve el resultado encontrado o None

def _update_entry(entry, content:dict):
    change = False
    for key in content.keys():
        if key in ['user', 'index_entry', 'period_spam']:
            continue
        if hasattr(entry, key):
            if getattr(entry, key) != content[key]:
                change = True
                setattr(entry, key, content[key])
    if change:
        db.session.commit()

def _delete_entries(index_used:list, user, period_spam, table):
    result = db.session.query(table).filter(
        table.id_person == user,
        table.period_spam == period_spam
    ).all()
    change = False
    for entry in result:
        if entry.index_entry not in index_used:
            change = True
            db.session.delete(entry)
    if change:
        db.session.commit()

