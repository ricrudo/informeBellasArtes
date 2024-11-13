url = '/docencia/participa_procesos_curriculares'
data = {
    
    'autoevaluacion': 'si',
    'program_misional_autoevaluacion' : 'program',
    'observa_autoevaluacion' : 'va1',

    'acreditacion': 'si',
    'program_misional_acreditacion': 'misional',
    'observa_acreditacion': 'va2',

    'curricular': 'no',
    'program_misional_curricular': 'program',
    'observa_curricular': 'no va3',

    'estudio': 'si',
    'program_misional_estudio': 'misional',
    'observa_estudio': 'va4',

    'disciplinar': 'no',
    'program_misional_disciplinar': 'program',
    'observa_disciplinar': 'no va5',

    'silabos': 'si',
    'program_misional_silabos': 'misional',
    'observa_silabos': 'va6',

    'grado': 'si',
    'program_misional_grado': 'program',
    'observa_grado': 'va7',

    'misional': 'no',
    'program_misional_misional': 'misional',
    'observa_misional': 'no va8',

    'oportuna': 'no',
    'program_misional_oportuna': 'program',
    'observa_oportuna': 'no va9',

    'nuevos': 'si',
    'program_misional_nuevos': 'misional',
    'observa_nuevos': 'va10',

    'facultad': 'si',
    'program_misional_facultad': 'program',
    'observa_facultad': 'va11',

    'period_spam': '2024-2'
    }

datafail = {

    'autoevaluacion': 'si',
    'program_misional_autoevaluacion' : 'aprogram',
    'observa_autoevaluacion' : 'va1',

    'acreditacion': 'si',
    'program_misional_acreditacion': 'smisional',
    'observa_acreditacion': '',

    'period_spam': '2024-2'
    }
respuesta_espeda = '''Se debe indicar obervaciones del proceso acreditacion
aprogram no es un valor valido
'''
