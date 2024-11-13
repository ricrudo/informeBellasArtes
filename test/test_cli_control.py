from unittest.mock import patch
import pytest
import cli_control
from pathlib import Path
from time import sleep

def test_user_confirmation_bad_and_y(capfd):
    with patch('builtins.input', side_effect=['s', 'y']):
        assert cli_control.user_confirmation('mensaje de prueba') == True
    response = (f'"s" no es una opcion valida.\n')
    assert capfd.readouterr().out == response

def test_user_confirmation_bad_and_n(capfd):
    with patch('builtins.input', side_effect=['s', 'n']):
        assert cli_control.user_confirmation('mensaje de prueba') == False
    response = (f'"s" no es una opcion valida.\n')
    assert capfd.readouterr().out == response

def test_base_sqlite_new_db(capfd):
    name_db = '0000db_pytest'
    path_db = Path.cwd() / 'appl' / 'interface' / 'dbs' / 'sqlite3' / 'bases_de_datos' / f'{name_db}.db'
    if path_db.exists():
        path_db.unlink()

    # test cuando la base de datos no existe
    with patch('builtins.input', side_effect=[name_db, '2']):
        cli_control.base_db_new_db()
    assert capfd.readouterr().out.split('\n')[-2] == f'la base de datos "{name_db}.db" ha sido creada exitosamente'

    first_creation_time = path_db.stat().st_atime 
    sleep(0.3)

    # test cuando la base de datos existe y se quiere sobreescribir
    with patch('builtins.input', side_effect=[name_db, 'y']):
        cli_control.base_db_new_db()
    second_creation_time = path_db.stat().st_atime 
    assert second_creation_time > first_creation_time
    sleep(0.3)

    # test cuando la base de datos existe y NO se sobreescribe
    with patch('builtins.input', side_effect=[name_db, 'n']):
        cli_control.base_db_new_db()
    third_creation_time = path_db.stat().st_atime 
    assert third_creation_time == second_creation_time

def test_base_db_list(capfd):
    name_db = '0000db_pytest'
    path_db = Path.cwd() / 'appl' / 'interface' / 'dbs' / 'sqlite3' / 'bases_de_datos' / f'{name_db}.db'
    if not path_db.exists():
        with patch('builtins.input', side_effect=[name_db, '2']):
            cli_control.base_db_new_db()
    cli_control.base_db_list()
    captured = capfd.readouterr().out
    assert name_db in captured

def test_select_db(capfd):
    name_db = '0000db_pytest'
    path_db = Path.cwd() / 'appl' / 'interface' / 'dbs' / 'sqlite3' / 'bases_de_datos' / f'{name_db}.db'
    if not path_db.exists():
        with patch('builtins.input', side_effect=[name_db, '2']):
            cli_control.base_db_new_db()
    with patch('builtins.input', side_effect=['d', '1']):
        assert cli_control.select_db() == name_db + '.db'
    captured = capfd.readouterr().out
    assert '"d" no es una opcion valida.' in captured

def test_base_db_del_db():
    name_db = '0000db_pytest'
    path_db = Path.cwd() / 'appl' / 'interface' / 'dbs' / 'sqlite3' / 'bases_de_datos' / f'{name_db}.db'
    if not path_db.exists():
        with patch('builtins.input', side_effect=[name_db, '2']):
            cli_control.base_db_new_db()

    # test para cuando no el usuario decido NO eliminar la base de datos
    with patch('builtins.input', side_effect=['1', 'n']):
        cli_control.base_db_del_db()
    assert path_db.exists()

    # test para cuando no el usuario decido eliminar la base de datos
    with patch('builtins.input', side_effect=['1', 'y']):
        cli_control.base_db_del_db()
    assert not path_db.exists()

def test_base_db_new_tb(capfd):
    name_db = '0000db_pytest'
    path_db = Path.cwd() / 'appl' / 'interface' / 'dbs' / 'sqlite3' / 'bases_de_datos' / f'{name_db}.db'
    if not path_db.exists():
        with patch('builtins.input', side_effect=[name_db, '2']):
            cli_control.base_db_new_db()

    with patch('builtins.input', side_effect=['1', 'tabla1', 'id', 'y', 'name', 'n', 'n']):
        cli_control.base_db_new_tb()
    captured = capfd.readouterr().out
    assert f'la tabla "tabla1" ha sido creada con exito en la base de datos "{name_db}.db".' in captured

def test_select_tb(capfd):
    name_db = '0000db_pytest'
    path_db = Path.cwd() / 'appl' / 'interface' / 'dbs' / 'sqlite3' / 'bases_de_datos' / f'{name_db}.db'
    if not path_db.exists():
        with patch('builtins.input', side_effect=[name_db, '2']):
            cli_control.base_db_new_db()
        with patch('builtins.input', side_effect=['1', 'tabla1', 'id', 'y', 'name', 'n', 'n']):
            cli_control.base_db_new_tb()
   
    # cuando la base de datos tiene tablas
    with patch('builtins.input', side_effect=['d', '1']):
        assert cli_control.select_tb(f'{name_db}.db') == 'tabla1'
    captured = capfd.readouterr().out
    assert '"d" no es una opcion valida.' in captured

    # cuando la base de datos no tiene tablas
    name_db_empty = '0000db_pytesv'
    path_db_empty = Path.cwd() / 'appl' / 'interface' / 'dbs' / 'sqlite3' / 'bases_de_datos' / f'{name_db_empty}.db'
    if not path_db.exists():
        with patch('builtins.input', side_effect=[name_db_empty]):
            cli_control.base_db_new_db()
    with patch('builtins.input', side_effect=['2']):
        cli_control.select_tb(f'{name_db_empty}.db')
    captured = capfd.readouterr().out
    assert f'No existen tablas en "{name_db_empty}.db".' in captured

def test_select_db_and_tb():
    name_db = '0000db_pytest'
    path_db = Path.cwd() / 'appl' / 'interface' / 'dbs' / 'sqlite3' / 'bases_de_datos' / f'{name_db}.db'
    if not path_db.exists():
        with patch('builtins.input', side_effect=[name_db, '2']):
            cli_control.base_db_new_db()
        with patch('builtins.input', side_effect=['1', 'tabla1', 'id', 'y', 'name', 'n', 'n']):
            cli_control.base_db_new_tb()
    with patch('builtins.input', side_effect=['1', '1']):
        assert cli_control.select_db_and_tb() == (f'{name_db}.db', 'tabla1')

def test_get_db_info_tb():
    name_db = '0000db_pytest'
    path_db = Path.cwd() / 'appl' / 'interface' / 'dbs' / 'sqlite3' / 'bases_de_datos' / f'{name_db}.db'
    if not path_db.exists():
        with patch('builtins.input', side_effect=[name_db, '2']):
            cli_control.base_db_new_db()
        with patch('builtins.input', side_effect=['1', 'tabla1', 'id', 'y', 'name', 'n', 'n']):
            cli_control.base_db_new_tb()

    # test sin argumentos
    with patch('builtins.input', side_effect=['1', '1']):
        assert cli_control.get_db_info_tb() == (f'{name_db}.db', 'tabla1' , {'Columna_0': {'name':'id', 'data_type':'', 'not_null':False, 'default_value':'', 'PK':False}, 'Columna_1':{'name':'name', 'data_type':'', 'not_null':False, 'default_value':'', 'PK':False}})

    # test con argumento name_db 
    with patch('builtins.input', side_effect=['1']):
        assert cli_control.get_db_info_tb(f'{name_db}.db') == (f'{name_db}.db', 'tabla1' , {'Columna_0': {'name':'id', 'data_type':'', 'not_null':False, 'default_value':'', 'PK':False}, 'Columna_1':{'name':'name', 'data_type':'', 'not_null':False, 'default_value':'', 'PK':False}})

    # test con argumentos name_db y name_tb
    assert cli_control.get_db_info_tb(f'{name_db}.db', 'tabla1') == (f'{name_db}.db', 'tabla1' , {'Columna_0': {'name':'id', 'data_type':'', 'not_null':False, 'default_value':'', 'PK':False}, 'Columna_1':{'name':'name', 'data_type':'', 'not_null':False, 'default_value':'', 'PK':False}})

def test_print_db_info_tb(capfd):
    dict_tb = {'Columna_0': {'name':'id', 'data_type':'', 'not_null':False, 'default_value':'', 'PK':False}, 'Columna_1':{'name':'name', 'data_type':'', 'not_null':False, 'default_value':'', 'PK':False}}
    cli_control.print_db_info_tb(dict_tb)
    captured = capfd.readouterr().out
    assert captured == f'''{" "*2}Columna_0:\n{" "*4}{"name:":<16}id\n{" "*4}{"data_type:":<16}\n{" "*4}{"not_null:":<16}False\n{" "*4}{"default_value:":<16}\n{" "*4}{"PK:":<16}False\n{" "*2}Columna_1:\n{" "*4}{"name:":<16}name\n{" "*4}{"data_type:":<16}\n{" "*4}{"not_null:":<16}False\n{" "*4}{"default_value:":<16}\n{" "*4}{"PK:":<16}False\n'''

def test_db_info_tb(capfd):
    name_db = '0000db_pytest'
    path_db = Path.cwd() / 'appl' / 'interface' / 'dbs' / 'sqlite3' / 'bases_de_datos' / f'{name_db}.db'
    if not path_db.exists():
        with patch('builtins.input', side_effect=[name_db, '2']):
            cli_control.base_db_new_db()
        with patch('builtins.input', side_effect=['1', 'tabla1', 'id', 'y', 'name', 'n', 'n']):
            cli_control.base_db_new_tb()
    with patch('builtins.input', side_effect=['1', '1']):
        cli_control.base_db_info_tb()
    captured = capfd.readouterr().out
    assert f'''Info tabla "tabla1" en la base de datos "{name_db}.db":\n{" "*2}Columna_0:\n{" "*4}{"name:":<16}id\n{" "*4}{"data_type:":<16}\n{" "*4}{"not_null:":<16}False\n{" "*4}{"default_value:":<16}\n{" "*4}{"PK:":<16}False\n{" "*2}Columna_1:\n{" "*4}{"name:":<16}name\n{" "*4}{"data_type:":<16}\n{" "*4}{"not_null:":<16}False\n{" "*4}{"default_value:":<16}\n{" "*4}{"PK:":<16}False\n''' in captured





def test_db_del_tb():
    pass




