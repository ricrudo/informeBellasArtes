

url = '/investigacion/productos_creacion'
data = {
'bool_productos_creacion': 'si',

'tipo_producto_1': 'evento',
'nombre_producto_1' : 'mi evento 1',
'institucion_1' : 'esta',
'alcance_1': 'local',
'fecha_1': '2024-12-10',
'link_1': 'este',
'categoria_1': 'tipo_A',

'tipo_producto_2': 'concierto',
'nombre_producto_2' : 'mi concierto',
'institucion_2' : 'esta ',
'alcance_2': 'regional',
'fecha_2': '2024-12-10',
'link_2': 'este',
'categoria_2': 'no_responde',

'tipo_producto_10': 'salida',
'nombre_producto_10' : 'salida',
'institucion_10' : 'salida',
'alcance_10': 'nacional',
'fecha_10': '2024-12-10',
'link_10': '',
'categoria_10': 'tipo_B',

'period_spam': '2024-2'
}


datafail = {
'bool_productos_creacion': 'si',

'tipo_producto_1': 'evento',
'nombre_producto_1' : 'mi evento 1',
'institucion_1' : 'esta',
'alcance_1': 'locale',
'fecha_1': '2024-12-10e',
'link_1': 'este',
'categoria_1': 'tipo_A',

'tipo_producto_2': 'concierto',
'nombre_producto_2' : 'mi concierto',
'institucion_2' : 'esta ',
'alcance_2': 'regional',
'fecha_2': '2024-12-10',
'link_2': 'este',
'categoria_2': 'no_responde',

'tipo_producto_10': 'salida',
'nombre_producto_10' : 'salida',
'institucion_10' : 'salida',
'alcance_10': 'nacional',
'fecha_10': '2024-12-10',
'link_10': '',
'categoria_10': 'tipoB',

'period_spam': '2024-2'
}
respuesta_espeda = '''El formato de fecha no es valido
locale no es un valor valido
tipoB no es un valor valido
'''

