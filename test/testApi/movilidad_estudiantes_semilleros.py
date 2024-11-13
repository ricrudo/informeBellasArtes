url = '/investigacion/movilidad_estudiantes_semilleros'
data = {

    'bool_movilidad_estudiantes_semilleros': 'si',

    'semillero_1' : 'este es semillero _1',
    'evento_1' : 'este es evento _1',
    'proyecto_1' : 'este es proyecto _1',
    'lugar_1' : 'este es lugar _1',
    'fecha_1' : '2024-12-10',
    'estudiantes_1_1' : 'este es estudiantes _1_1',
    'estudiantes_1_2' : 'este es estudiantes _1_2',
    'estudiantes_1_3' : 'este es estudiantes _1_3',
    'estudiantes_1_4' : 'este es estudiantes _1_4',

    'semillero_2' : 'este es semillero _2',
    'evento_2' : 'este es evento _2',
    'proyecto_2' : 'este es proyecto _2',
    'lugar_2' : 'este es lugar _2',
    'fecha_2' : '2024-12-10',
    'estudiantes_2_1' : 'este es estudiantes _2_1',
    'estudiantes_2_2' : 'este es estudiantes _2_2',

    'semillero_10' : 'este es semillero _10',
    'evento_10' : 'este es evento _10',
    'proyecto_10' : 'este es proyecto _10',
    'lugar_10' : 'este es lugar _10',
    'fecha_10' : '2024-12-10',
    'estudiantes_10_1' : 'este es estudiantes _10_1',

    'period_spam': '2024-2'
    }

datafail = {

    'bool_movilidad_estudiantes_semilleros': 'si',

    'semillero_1' : '',
    'evento_1' : 'este es evento _1',
    'proyecto_1' : 'este es proyecto _1',
    'lugar_1' : 'este es lugar _1',
    'fecha_1' : '2024-12s-10',
    'estudiantes_1_1' : '',

    'period_spam': '2024-2'
    }
respuesta_espeda = '''el campo semillero es obligatorio
El formato de fecha no es valido
el campo estudiantes es obligatorio
'''
