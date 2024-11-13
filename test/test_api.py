import click
import requests
from testApi import testIndexes
import re

main_url = 'http://127.0.0.1:5000'

@click.command()
@click.argument('action', type=str)
# los parametros que reciben son el primer parametro de cada uno de las option o argument
def cli(action):
    if action == 'help':showHelp()
    else:
        test = re.search(r'^(\d+)(fallo)*$', action)
        if not test:
            print(f'No existe un test con valor {action}')
            return
        numberTest = int(test.groups()[0])
        fallo = test.groups()[1] == 'fallo'
        try:
            tester(testIndexes[numberTest], fallo)
        except KeyError:
            print(f'{action} no es un text existente')

def showHelp():
    print('Se indica el test como una variable.\nTest disponibles:')
    for key, value in testIndexes.items():
        print(f'{key} - {value.__name__.replace("testApi.","")}')

def tester(origin, fail=False):
    if not fail:
        url = main_url + origin.url
        data = origin.data
        response = requests.post(url, data=data)
        print(response.text)
    else:
        url = main_url + origin.url
        data = origin.datafail
        response = requests.post(url, data=data)
        if response.text == origin.respuesta_espeda:
            print('fallos esperados concuerdan')
        else:
            print('ERROR-'*5)
            print(response.text)
            print('ERROR-'*5)


if __name__ == "__main__":
    cli()

