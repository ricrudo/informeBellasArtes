


url = '/investigacion/evaluacion_tesis'
data = {
'bool_evaluacion_tg' : 'si',

'titulo_1' : 'este es titulo _1',
'estudiantes_1_1' : 'este es estudiantes _1_1',
'estudiantes_1_2' : 'este es estudiantes _1_2',
'estudiantes_1_3' : 'este es estudiantes _1_3',
'estudiantes_1_4' : 'este es estudiantes _1_4',
'estudiantes_1_5' : 'este es estudiantes _1_5',
'estudiantes_1_6' : 'este es estudiantes _1_6',
'estudiantes_1_7' : 'este es estudiantes _1_7',
'estudiantes_1_8' : 'este es estudiantes _1_8',
'estudiantes_1_9' : 'este es estudiantes _1_9',
'nivel_formacion_1' : 'pregrado',
'programa_1' : 'musica',

'titulo_2' : 'este es titulo _2',
'estudiantes_2_1' : 'este es estudiantes _2_1',
'estudiantes_2_2' : 'este es estudiantes _2_2',
'estudiantes_2_3' : 'este es estudiantes _2_3',
'estudiantes_2_4' : 'este es estudiantes _2_4',
'estudiantes_2_5' : 'este es estudiantes _2_5',
'estudiantes_2_6' : 'este es estudiantes _2_6',
'estudiantes_2_7' : 'este es estudiantes _2_7',
'estudiantes_2_8' : 'este es estudiantes _2_8',
'estudiantes_2_9' : 'este es estudiantes _2_9',
'nivel_formacion_2' : 'maestria',
'programa_2' : 'danza',

'titulo_10' : 'este es titulo _10',
'estudiantes_10_1' : 'este es estudiantes _10_1',
'estudiantes_10_2' : 'este es estudiantes _10_2',
'estudiantes_10_3' : 'este es estudiantes _10_3',
'estudiantes_10_4' : 'este es estudiantes _10_4',
'estudiantes_10_5' : 'este es estudiantes _10_5',
'estudiantes_10_6' : 'este es estudiantes _10_6',
'estudiantes_10_7' : 'este es estudiantes _10_7',
'estudiantes_10_8' : 'este es estudiantes _10_8',
'estudiantes_10_9' : 'este es estudiantes _10_9',
'nivel_formacion_10' : 'doctorado',
'programa_10' : 'arte_dramatico',

'period_spam': '2024-2'
}


datafail = {
'bool_evaluacion_tg' : 'si',

'titulo_1' : 'este es titulo _1',
'estudiantes_1_1' : '',
'nivel_formacion_1' : 'pregado',
'programa_1' : 'licenciatua_en_musica',
'status_1' : 'en_poceso',

'period_spam': '2024-2'
}
respuesta_espeda = '''el campo status no existe en la tabla
el campo estudiantes es obligatorio
pregado no es un valor valido
licenciatua_en_musica no es un valor valido
'''



