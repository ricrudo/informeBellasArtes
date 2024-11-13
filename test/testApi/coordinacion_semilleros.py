

url = '/investigacion/coordinacion_semilleros'
data = {

'bool_coord_semillero': 'si',

'semillero_1' : 'este es semillero _1',
'total_integrantes_1' : '10',
'nuevos_integrantes_1' : '2',
'grupo_1' : 'sam',
'programa_1' : 'musica',
'update_sia_1' : 'si',

'semillero_2' : 'este es semillero _2',
'total_integrantes_2' : '2',
'nuevos_integrantes_2' : '2',
'grupo_2' : 'art',
'programa_2' : 'danza',
'update_sia_2' : 'si',

'semillero_10' : 'este es semillero _10',
'total_integrantes_10' : '50',
'nuevos_integrantes_10' : '2',
'grupo_10' : 'fel',
'programa_10' : 'danza',
'update_sia_10' : 'no',

'period_spam': '2024-2'
}

datafail = {

'bool_coord_semillero': 'si',

'semillero_1' : '',
'total_integrantes_1' : '',
'nuevos_integrantes_1' : '',
'grupo_1' : 'este es grupo _1',
'programa_1' : 'varchar',

'period_spam': '2024-2'
}

respuesta_espeda = '''el campo semillero es obligatorio
el campo total_integrantes es obligatorio
el campo nuevos_integrantes es obligatorio
el campo update_sia no se indica en el formulario
este es grupo _1 no es un valor valido
varchar no es un valor valido
'''

