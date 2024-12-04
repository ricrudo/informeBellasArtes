from app.interface import db
from app.interface.db.get_Data import getTables
import argparse


def setParser():
    parser = argparse.ArgumentParser(description='Detector de cabeceras')
    # argumentos opcionales
    parser.add_argument('--id_person', help='id de la persona (docente)')
    parser.add_argument('--new_email', help='nuevo email para para el --id_person')

    # argumentos obligatorios positional
    parser.add_argument('action', help='accion a realizar')
    return parser

def change_email(args):
    id_person = args.id_person
    new_email = args.new_email
    if not id_person:
        raise Exception(f'Es necesario el argumento --id_person con un valor')
    if not id_person:
        raise Exception(f'Es necesario el argumento --new_email con un valor')
    table = getTables('section1_1')[0]
    result = db.session.query(table).filter(
        table.id == id_person,
    ).first()  # `first()` devuelve el primer resultado o None si no hay coincidencias
    setattr(result, 'email', new_email.lower())
    db.session.commit()
    db.session.close()
    



def getFunction(function_name):
    functions = {
        'change_email': change_email
    }
    response = functions.get(function_name, None)
    if not response:
        raise Exception(f'{function_name} no es valido.')
    return response
    


def main():
    parser = setParser()
    args = parser.parse_args()
    response = getFunction(args.action)(args)


    

if __name__ == "__main__":
    main()

