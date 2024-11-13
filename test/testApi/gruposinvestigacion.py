

url = '/investigacion/part_grupos_investigacion'
data = {
'grupo_1': 'sam',
'linea_investiga_1': 'linea1',
'programa_1': 'danza',
'actividades_1' : 'actividades1',

'grupo_2': 'tei',
'linea_investiga_2': 'linea2',
'programa_2': 'arte_dramatico',
'actividades_2' : 'actividades2',

'grupo_10': 'vid',
'linea_investiga_10': 'linea3',
'programa_10': 'artes_plasticas',
'actividades_10' : 'actividades3',

'grupo_4': 'fel',
'linea_investiga_4': 'linea4',
'programa_4': 'licenciatura_en_musica',
'actividades_4' : 'actividades4',
'period_spam': '2024-2'
}


datafail = {
'grupo_1': 'grupo1',
'linea_investiga_1': '',
'programa_1': 'danza',
'actividades_1' : 'actividades1',

'grupo_2': 'grupo2',
'linea_investiga_2': 'linea2',
'programa_2': 'arte_dramatico',
'actividades_2' : 'actividades2',

'grupo_10': 'grupo3',
'linea_investiga_10': 'linea3',
'programa_10': 'artes_plasticase',
'actividades_10' : 'actividades3',

'grupo_4': 'grupo4',
'linea_investiga_4': 'linea4',
'programa_4': 'licenciatura_en_musica',
'actividades_4' : '',
'period_spam': '2024-2'
}
respuesta_espeda = '''el campo linea_investiga es obligatorio
grupo1 no es un valor valido
grupo2 no es un valor valido
grupo3 no es un valor valido
artes_plasticase no es un valor valido
grupo4 no es un valor valido
'''

