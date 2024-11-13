from click_shell import shell
from pathlib import Path
from new_entries_generator import new_entries_generator

@shell(prompt="script_code_faster > ", intro='''Conjunto de script que automatizan
la creación de ciertos archivos. 
Si quiere ver la lista de comando ingrese "help"''')
def cli_program():
    pass

@cli_program.command()
def help():
    print('''Esta es la lista de comando disponibles
help: obtener la lista de comandos
new_entries_generator: ingresar nuevo usuario
''')

@cli_program.command()
def new_entries_generator():
    response = ""
    while not response and response.lower() not in ['y', 'n']:
        response = input('Desea copiar los archivos a la app?: ')
    if response.lower() == 'y':
        copy_to_folder = Path.cwd().parent / 'app' / 'interface' / 'db'
    else:
        copy_to_folder = None
    origin = Path.cwd().parent / 'app' / 'domain' / 'models.py'
    destino = Path.cwd() / 'new_entries_generator' / 'results'
    breakpoint()
    new_entries_generator(origin, destino, copy_to_folder)

if __name__ == "__main__":
    cli_program()
