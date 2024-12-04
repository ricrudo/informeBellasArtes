from app.interface import db
from app.interface.db import section1_1, section2_1
from pathlib import Path
import json

PERIODO_SPAM = '2024-2'

def loadData(path):
    return json.loads(path.read_text())


def saveToDB(dataPtas):
    for cedula, data in dataPtas.items():
        if not data['email']:
            continue
        packagePerson = {
            'name': data['nombre'],
            'admin_role' : False,
            'facultad' : 'Bellas Artes',
            'email' : data['email']
        }
        id_person = section1_1.new_entry_admin(packagePerson)
        index_entry = 0
        for periodo in ['2024-1', '2024-2']:
            if periodo not in data:
                continue
            for materia in data[periodo]['materias']:
                packageMateria = {
                    'user': id_person,
                    'index_entry': index_entry,
                    'materia' : f"{materia['materia']} - {periodo}",
                    'code' : materia['code'],
                    'programa': None,
                    'status_done': None,
                    'observaciones': None,
                    'bool_internacional': None,
                    'internacional': None,
                    'bool_tic': None,
                    'tic': None,
                    'motivos_cancel': None,
                    'period_spam': PERIODO_SPAM

                }
                section2_1._create_entry(packageMateria)
                index_entry += 1

def loadDB():
    path = Path.cwd() / 'parse_pta' / 'TestUser.json'
    dataPtas = loadData(path)
    saveToDB(dataPtas)

def updateTable():
    from app.domain.models import JovenesInvestigadores
    JovenesInvestigadores.__table__.drop(db.engine)
    db.Base.metadata.create_all(db.engine, tables=[JovenesInvestigadores.__table__])

if __name__ == "__main__":
    loadDB()



