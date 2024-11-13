'''
Este pretende ser una app CLI para manejar tareas en el servidor relacionadas con actualizacion, creacion y mantenimiento de la base de datos, recopilacion de informacion, etc
'''

from click_shell import shell
from rich.console import Console
from pathlib import Path
from datetime import datetime

console = Console(highlight=False)


@shell(prompt="cli_control > ", intro='''Este es la aplicación CLI para la app del informe docente de profesores de la Facultad de Bellas Artes de la Universidad del Atlántico.

Por favor ingrese el comando. Si quiere ver la lista de comando ingrese "help"''')
def cli_program():
    pass

@cli_program.command()
def help():
    op_DB = {
    "base de datos": {
        "db-new-db": "Instrucciones sobre como crear una nueva base de datos",
        "db-new-db-force": "Forzar la creación de una base de datos a partir de los modelos que estan en app/domain/models.py",
        "db-list": "muestra el nombre de las bases de datos creadas, con sus tablas y columnas en cacada tabla",
        "db-del-db": "eliminar una base de datos"},
    "tablas": {
        "db-new-tb": "crea una nueva tabla en la base de datos",
        "db-new-tbs-from-template": "crea todos las tablas para una base de datos desde una plantilla",
        "db-info-tb": "muestra la informacion de las colummnas que contiene una tabla",
        "db-mod-tb": "modifica las estructura de una tabla",
        "db-template-from-tb": "crea una plantilla para una tabla a partir de una tabla ya existente",
        "db-del-tb": "elimina una tabla en la base de datos"},
    "data": {
        "db-new-entry": "crea una nueva entrada en la base de datos",
        "db-get-all-entries": "muestra la informacion de una entrada en la base de datos",
        "db-mod-entry": "modifica una entrada en la base de datos",
        "db-del-entry": "elimina una entrada en la base de datos"},
    'otras opciones': {
        "db-type": "consultar el tipo de base de datos utilizada",
        "db-type-ch": "cambiar el tipo de base de datos utilizada"
        }
    }

    format_op_DB = "\n\n".join([f'{" "*3}Operaciones con {k}' + "\n" + "\n".join([f'{"".join([" "*6, k2, ":"]):<34}{v2}' for k2, v2 in v.items()]) for k, v in op_DB.items()])
    print(f'''Esta es la lista de comando disponibles
help: obtener la lista de comandos

BASES DE DATOS
{format_op_DB}
''')

@cli_program.command()
def db_new_db():
    console.print("""
[bold blue]CREACION DE UNA BASE DE DATOS[/bold blue]

El sistema esta diseñado para que por defecto funcione con una base de datos llamada:
    [bold red]'bellasartes_test'[/bold red]

Si se quiere especificar una base de datos distinta (lo cual es recomendable cuando se este en producción) se debe colocar en las variables de entorno con:
    [bold red]export NAME_DB="nombre_base_de_datos"[/bold red]

Si la base de datos ya existe automaticamente no hará nada.

Para forzar la creación de una base de datos nueva corra db-new-db-force. Este comando automaticamente guardará una copia de la base con el nombre:
    [bold red]nombre_db_.sqlite.(date).old[/bold red]
""")

@cli_program.command()
def db_new_db_force():
    from app.interface import db
    from app.domain import models

    name_db = Path.cwd() / db.engine.url.database

    if name_db.exists():
        name_db.rename(f'{name_db.as_posix()}.{datetime.now().isoformat()}.old')
    db.Base.metadata.create_all(db.engine)



if __name__ == "__main__":
    cli_program()

