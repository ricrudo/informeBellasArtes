

url = '/investigacion/patentes_derechos_autor'
data = {
'bool_patentes': 'si',

'tipo_producto_1' : 'artisticas',
'registro_1' : 'este es registro _1',
'fecha_1' : '2024-12-10',

'tipo_producto_2' : 'audiovisuales',
'registro_2' : 'este es registro _2',
'fecha_2' : '2024-12-10',

'tipo_producto_3' : 'musicales',
'registro_3' : 'este es registro _3',
'fecha_3' : '2024-12-10',

'tipo_producto_4' : 'software',
'registro_4' : 'este es registro _4',
'fecha_4' : '2024-12-10',

'tipo_producto_10' : 'otro',
'registro_10' : 'este es registro _10',
'fecha_10' : '2024-12-10',

'period_spam': '2024-2'
}

datafail = {
'bool_patentes': 'si',

'tipo_producto_1' : 'artisticas',
'registro_1' : 'este es registro _1',
'fecha_1' : '2024--10',

'tipo_producto_2' : 'audiovisules',
'registro_2' : 'este es registro _2',
'fecha_2' : '2024-12-10',


'period_spam': '2024-2'
}
respuesta_espeda = '''El formato de fecha no es valido
audiovisules no es un valor valido
'''

