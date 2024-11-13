from pathlib import Path
import re

categoria = 'docencia'

string_raw = """
class Part_ProcesosCurriculares(db.Base):
    '''
    3.1 PARTICIPACIÓN EN PROCESOS CURRICULARES
    '''
    __tablename__ = 'participa_procesos_curriculares'

    id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True)
    id_person = sqla.Column(sqla.Integer, sqla.ForeignKey('persons.id'))
    # responde a la pregunta nombre del proceso
        # autoevaluacion = 1
        # acreditacion = 2
        # curricular = 3
        # estudio = 4
        # disciplinar = 5
        # silabos = 6
        # grado = 7
        # misional = 8
        # oportuna = 9
        # nuevos = 10
        # facultad = 11
    name_proceso = sqla.Column(sqla.Integer, nullable=False)
    # response a la pregunta: Programa o misional
        # programa = 1
        # misional = 2
    programa_misional = sqla.Column(sqla.Integer, nullable=False)
    # Respuesta a la pregunta: Observaciones sobre el proceso
    observaciones = sqla.Column(sqla.Text, nullable=False)
    # path para los archivos adjuntos que se suban
    path_files = sqla.Column(sqla.Text)
    period_spam = sqla.Column(sqla.VARCHAR(10), nullable=False)
"""




omit = [
    r'^class .+$',
    r'^\d+?\.\d+? [A-Z].+$',
    r'^id \= sqla.Column.+$',
    r'^id_person \= sqla.Column.+$',
    r'^period_spam \= sqla.Column.+$',
    r'^#.*$',
    r"^'{3}$"
]

string = []

for line in string_raw.split('\n'):
    passing = False
    counter = 0
    if not line:
        continue
    while counter < len(omit) and not passing:
        if re.search(omit[counter], line.strip()):
            passing = True
        counter += 1
    if passing:
        continue
    tablename = re.search("^__tablename__.*?\=.*?'(.*)'$", line.strip())
    if tablename:
        nombre_tabla = tablename.group(1).strip()
        continue
    string.append(line)

if not nombre_tabla:
    print('no se encuentra el nombre de la tabla')
    exit()

if not string:
    print('no se recogio ningun dato de la tabla')
    exit()

final = []
tab = " "*4

for question in ['_1', '_2','_10', '_3', '_4'][:3]:
    counter = 0
    for line in string:
        if 'period_spam' in line or not line:
            continue
        content = line.strip().split(" = ")[0]
        if 'sqla.Date' in line:
            final.append(f"{tab}'{content}{question}' : '2024-12-10'")
        elif 'sqla.Text' in line:
            final.append(f"{tab}'{content}{question}' : 'este es {content} {question}'")
        elif 'sqla.VARCHAR' in line:
            final.append(f"{tab}'{content}{question}' : 'varchar'")
        elif 'sqla.Integer' in line:
            final.append(f"{tab}'{content}{question}' : 'integer'")
        if counter == 0:
            final[-1] = '\n' + final[-1]
        counter += 1
final.append(f"\n{tab}'period_spam': '2024-2'")

string_final = ",\n".join(final)

template=f"url = '/{categoria}/{nombre_tabla}'"+'''
data = {

    'bool_''' +f"{nombre_tabla}'" +''': 'si',
$$$preguntas$$$
    }

datafail = {

    'bool_''' +f"{nombre_tabla}'" +''': 'si',
$$$preguntas$$$
    }
respuesta_espeda = '''+"'''\n'''\n"

file_final = template.replace('$$$preguntas$$$', string_final)
print(file_final)
destino = Path.cwd() / 'testApi' / f'{nombre_tabla}weak.py'
destino.write_text(file_final)
