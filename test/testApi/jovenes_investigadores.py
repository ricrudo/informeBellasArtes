url = '/investigacion/jovenes_investigadores'
data = {

    'bool_jovenes_investigadores': 'si',

    'convocatoria_1' : 'este es convocatoria _1',
    'estudiantes_1_1' : 'este es estudiantes _1_1',
    'estudiantes_1_2' : 'este es estudiantes _1_2',
    'estudiantes_1_3' : 'este es estudiantes _1_3',
    'programa_1' : 'danza',

    'convocatoria_2' : 'este es convocatoria _2',
    'estudiantes_2_1' : 'este es estudiantes _2_1',
    'estudiantes_2_2' : 'este es estudiantes _2_2',
    'programa_2' : 'musica',

    'convocatoria_10' : 'este es convocatoria _10',
    'estudiantes_10_1' : 'este es estudiantes _10_1',
    'programa_10' : 'danza',

    'period_spam': '2024-2'
    }

datafail = {

    'bool_jovenes_investigadores': 'si',

    'convocatoria_1' : 'este es convocatoria _1',
    'estudiantes_1_1' : '',
    'programa_1' : 'ss',

    'convocatoria_2' : 'este es convocatoria _1',
    'estudiantes_2_1' : 'este es estudiantes _2_1',
    'programa_2' : '',

    'period_spam': '2024-2'
    }
respuesta_espeda = '''el campo estudiantes es obligatorio
ss no es un valor valido
el campo programa es obligatorio
 no es un valor valido
'''
