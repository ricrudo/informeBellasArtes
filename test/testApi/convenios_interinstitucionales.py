

url = '/investigacion/convenios_productos_redes'
data = {
'bool_conve_inter': 'si',

'convenio_1' : 'este es convenio _1',
'producto_1' : 'este es producto _1',
'grupo_1' : 'sam',
'impacto_1' : 'este es impacto _1',

'convenio_2' : 'este es convenio _2',
'producto_2' : 'este es producto _2',
'grupo_2' : 'fel',
'impacto_2' : 'este es impacto _2',

'convenio_10' : 'este es convenio _10',
'producto_10' : 'este es producto _10',
'grupo_10' : 'vid',
'impacto_10' : 'este es impacto _10',

'period_spam': '2024-2'
}

datafail = {
'bool_conve_inter': 'si',

'convenio_1' : '',
'producto_1' : 'este es producto _1',
'grupo_1' : 'este es grupo _1',
'impacto_1' : 'este es impacto _1',

'convenio_2' : 'este es convenio _2',
'producto_2' : '',
'grupo_2' : 'este es grupo _2',
'impacto_2' : 'este es impacto _2',

'convenio_10' : 'este es convenio _10',
'producto_10' : 'este es producto _10',
'grupo_10' : '',
'impacto_10' : 'este es impacto _10',

'period_spam': '2024-2'
}
respuesta_espeda = '''el campo convenio es obligatorio
este es grupo _1 no es un valor valido
el campo producto es obligatorio
este es grupo _2 no es un valor valido
el campo grupo es obligatorio
 no es un valor valido
'''

