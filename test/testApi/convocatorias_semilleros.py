

url = '/investigacion/convocatorias_semilleros'
data = {

'bool_convocatorias_semilleros': 'si',

'semillero_1' : 'este es semillero _1',
'tipo_convovatoria_1' : 'interna',
'nombre_1' : 'este es nombre _1',
'proyecto_1' : 'este es proyecto _1',
'participantes_1_1' : 'este es participantes_1_1',
'participantes_1_2' : 'este es participantes_1_2',
'participantes_1_3' : 'este es participantes_1_3',
'participantes_1_4' : 'este es participantes_1_4',
'fecha_1' : '2024-12-10',
'observaciones_1' : 'este es observaciones _1',

'semillero_2' : 'este es semillero _2',
'tipo_convovatoria_2' : 'externa',
'nombre_2' : 'este es nombre _2',
'proyecto_2' : 'este es proyecto _2',
'participantes_2_1' : 'este es participantes_2_1',
'fecha_2' : '2024-12-10',
'observaciones_2' : 'este es observaciones _2',

'semillero_10' : 'este es semillero _10',
'tipo_convovatoria_10' : 'interna',
'nombre_10' : 'este es nombre _10',
'proyecto_10' : 'este es proyecto _10',
'participantes_10_1' : 'este es participantes_10_1',
'participantes_10_2' : 'este es participantes_10_2',
'fecha_10' : '2024-12-10',
'observaciones_10' : 'este es observaciones _10',

'period_spam': '2024-2'
}

datafail = {

'bool_convocatorias_semilleros': 'si',

'semillero_1' : 'este es semillero _1',
'tipo_convovatoria_1' : 'ierna',
'nombre_1' : 'este es nombre _1',
'proyecto_1' : '',
'participantes_1' : '',
'fecha_1' : '2024-12a-10',
'observaciones_1' : '',


'period_spam': '2024-2'
}

respuesta_espeda = '''los campos participante se encuentran en el formato incorrecto
el campo proyecto es obligatorio
el campo participantes es obligatorio
El formato de fecha no es valido
el campo observaciones es obligatorio
ierna no es un valor valido
'''

