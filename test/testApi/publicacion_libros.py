

url = '/investigacion/publicacion_libros'
data = {
'bool_publicaciones_libros': 'si',

'titulo_1' : 'este es titulo _1',
'autores_1' : 'este es autores _1',
'editorial_1' : 'este es editorial _1',
'fecha_1' : '2024-12-10',
'issn_1' : 'este es issn _1',

'titulo_2' : 'este es titulo _2',
'autores_2' : 'este es autores _2',
'editorial_2' : 'este es editorial _2',
'fecha_2' : '2024-12-10',
'issn_2' : 'este es issn _2',

'titulo_10' : 'este es titulo _10',
'autores_10' : 'este es autores _10',
'editorial_10' : 'este es editorial _10',
'fecha_10' : '2024-12-10',
'issn_10' : 'este es issn _10',

'period_spam': '2024-2'
}

datafail = {
'bool_publicaciones_libros': 'si',

'titulo_1' : 'este es titulo _1',
'autores_1' : 'este es autores _1',
'editorial_1' : 'este es editorial _1',
'fecha_1' : '2024-12-10s',
'issn_1' : 'este es issn _1',

'titulo_2' : 'este es titulo _2',
'autores_2' : 'este es autores _2',
'editorial_2' : 'este es editorial _2',
'fecha_2' : '2024-12-10',
'issn_2' : '',

'titulo_10' : 'este es titulo _10',
'autores_10' : 'este es autores _10',
'editorial_10' : 'este es editorial _10',
'fecha_10' : '2024-12-10',
'issn_10' : 'este es issn _10',

'period_spam': '2024-2'
}
respuesta_espeda = '''El formato de fecha no es valido
el campo issn es obligatorio
'''

