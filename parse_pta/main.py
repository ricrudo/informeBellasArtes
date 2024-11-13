import pymupdf  # Esta es la librería PyMuPDF
import re
from pathlib import Path
import json
import logging

# Configuración para guardar los logs en un archivo
logging.basicConfig(
    filename='mi_log.log',         # Nombre del archivo de logs
    level=logging.INFO,             # Nivel mínimo de registro
    format='%(asctime)s - %(levelname)s - %(message)s'  # Formato del log
)

ORIGIN_EMAILS = Path.cwd() / 'email_docentes_BA.csv'

def _set_path(path:str=None)->Path:
    '''
    define el path como objeto Path
    '''
    if path:
        return Path("path")
    else:
        return Path.cwd() / 'ptas'

def _pdf_filter(path:Path)->list:
    '''
    devuelve la ruta para los archivos con ext .pdf
    '''
    files = []
    for archivo in path.iterdir():
        if archivo.suffix.lower() == ".pdf":
            files.append(archivo)
    return files

def _convert_pdf_json(archivo:Path)->dict:
    '''
    convierte el pdf a json
    '''
    texto = []
    pdf_document = pymupdf.open(archivo)
    for pagina_num in range(pdf_document.page_count):
        pagina = pdf_document[pagina_num]
        texto_pagina = json.loads(pagina.get_textpage().extractJSON())['blocks']
        texto.extend(texto_pagina)
    pdf_document.close()
    return texto

def _get_extract_from_str(txt_content:str, patron:re, pos_datos_grupo:int=0)->str:
    '''
    obtiene del txt con regular expresion
    '''
    resultado = patron.search(txt_content[pos_datos_grupo:])
    if resultado:
        return resultado.group(1).strip()

def _get_materias_detallado(materias:str)->dict:
    '''
    parse la informacion de la materia y devuelve en un dict
    el codigo, nombre, grupo, lugar, dia y hora de la materia
    '''
    dict_materias = []
    if materias == ['No se encontraron registros']:
        logging.warning('No se encontraron registros de clases.')
        return None
    for materia in materias:
        codigo = _get_extract_from_str(materia, re.compile(r"(\d+) -"))
        nombre = _get_extract_from_str(materia, re.compile(r" - (.+)"))
        grupo = _get_extract_from_str(materia, re.compile(r"\n(.+)"))
        horarios = []
        if 'Domingo\n' in materia:
            list_dias = ['Lunes','Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
            dias = materia.split('Domingo\n')[1].split('\n')
            for i, dia in enumerate(dias):
                if dia != '-':
                    patron = re.compile(r"(.*) (\d{4}) - (\d{4})")
                    coincidencia = re.search(patron, dia)
                    if coincidencia:
                        horarios.append({
                            'dia': list_dias[i],
                            'lugar': coincidencia.group(1),
                            'inicio': coincidencia.group(2),
                            'fin': coincidencia.group(3)
                            })
        elif 'No existe horario gestionado' in materia:
            logging.warning(f'No se encontraron registros de horario para la materia "{nombre}".')
            horarios = None
        info_clase = {
            "class_code": codigo,
            "class_name": nombre,
            "group": grupo,
            "horarios": horarios
        }
        dict_materias.append(info_clase)
    return dict_materias


def _descarga_to_str(txt_content:str)->str:
    '''
    extra la parte del texto que está entre "Total Semanal" y "Total"
    '''
    patron = re.compile(r"Total Semanal[^\n]*\n(.*?)\nTotal", re.DOTALL)
    return _get_extract_from_str(txt_content, patron)

def _agrupar_descarga(txt_descarga:str)->list[str]:
    '''
    toma el bloque de texto de descarga y lo separa en una lista conteniendo cada una de las descargas como str
    '''
    descargas = []
    if not txt_descarga:
        return descargas

    lineas = txt_descarga.split('\n')
    tipo = False
    for line in lineas:
        if not tipo:
            descargas.append({})
            descargas[-1]['tipo_de_actividad'] = line
            descargas[-1]['Descripcion'] = []
            tipo = True
        else:
            if not line.isdigit():
                descargas[-1]['Descripcion'].append(line)
            else:
                descargas[-1]['Descripcion'] = " ".join(descargas[-1]['Descripcion'])
                descargas[-1]['horas'] = int(line)
                tipo = False
    if tipo:
        descargas[-1]['Descripcion'] = " ".join(descargas[-1]['Descripcion'])
    return descargas

def _get_descarga(content, indexPos, archivo)->dict:
    '''
    corre las funciones para extraer y organizar la info relacionada con la descarga
    '''
    if not content[indexPos]['lines'][0]['spans'][0]['text'] == 'Descargas':
        while indexPos < len(content):
            if 'Descargas' in content[indexPos]['lines'][0]['spans'][0]['text']:
                break
            indexPos += 1
    indexPos += 1
    if not content[indexPos]['lines'][0]['spans'][0]['text'] == 'Tipo Actividad':
        logging.error(f'{archivo} no encuentra "Descargas->Tipo Actividad" con el indexPos')
        return 'error'
    indexPos += 1
    descarga = []
    while len(content[indexPos]['lines']) > 2:
        tipo_actividad = ''
        for span in content[indexPos]['lines'][0]['spans']:
            tipo_actividad += span['text']
        descripcion = ''
        for line in content[indexPos]['lines'][1:]:
            for span in line['spans']:
                descripcion += span['text']
        descarga.append({'tipo_actividad':tipo_actividad, 'descripcion': descripcion})
        indexPos += 1
    return descarga

def checkFile(content):
    for entry in content:
        if entry['lines'][0]['spans'][0]['text'] == 'Responsabilidad y Vinculación Docente IES':
            return True

def checkPeriodo(content, archivo, periodoSpam):
    indexPos = 0
    while indexPos < len(content):
        for line in content[indexPos]['lines']:
            for span in line['spans']:
                if '2024 -' in span['text']:
                    if periodoSpam not in span['text']:
                        logging.warning(f'{archivo.name} no coincide el periodo')
                    return indexPos
        indexPos += 1
    logging.warning(f'{archivo.name} parece tener fecha de periodo')

def _get_nombre_pta(content:str, indexPos)-> str:
    '''
    obtiene el nombre y la cedula del docente
    '''
    while indexPos < len(content):
        if 'Documento' in content[indexPos]['lines'][0]['spans'][0]['text']:
            cedula = content[indexPos+1]['lines'][0]['spans'][0]['text']
            nombre = content[indexPos+1]['lines'][1]['spans'][0]['text']
            return cedula, nombre
        indexPos += 1
    
def _get_materias_sections(content:list, indexPos:int, archivo)->list:
    sections = []
    while indexPos < len(content):
        if 'Lunes' in content[indexPos]['lines'][0]['spans'][0]['text']:
            materia = ''
            for index, line in enumerate(content[indexPos-1]['lines']):
                if not materia:
                    materia += line['spans'][0]['text']
                elif line['spans'][0]['text'] in  ['NORMAL', 'VIRTUAL', 'DIRIGIDO']:
                    break
                else:
                    materia += line['spans'][0]['text']
            if sections and materia in sections[-1]:
                while True:
                    residuo = sections[-1].pop(-1)
                    if residuo == materia:
                        break
            sections.append([x.strip() for x in materia.split("-")])
        elif 'Descargas' in content[indexPos]['lines'][0]['spans'][0]['text']:
            return sections, indexPos
        elif len(sections) > 0:
            for line in content[indexPos]['lines']:
                foundGroup = False
                for span in line['spans']:
                    if 'Grupo' in span['text']:
                        foundGroup = True
                    if span['text'] != '-' and foundGroup:
                        sections[-1].append(span['text'])
        indexPos += 1

def _format_materias(sections:list, archivo:Path)->list:
    result = []
    for section in sections:
        code = section[0]
        name = []
        grupo = []
        flagGrupo = False
        for part in section[1:]:
            if not flagGrupo:
                if 'Grupo' in part:
                    flagGrupo = True
                    name = " ".join(name)
                    grupo.append(part)
                else:
                    name.append(part)
            else:
                if part not in grupo:
                    grupo.append(part)
        grupo = "".join(grupo)
        entry = {
            'code': code,
            'materia': f"{name} - {grupo}"
        }
        result.append(entry)
    return result

def _get_clases(content:list, indexPos:int, archivo:Path)->list[dict]:
    '''
    corre todas las funciones para que las clases queden almacenadas en una lista de dict
    '''
    sections, indexPos = _get_materias_sections(content, indexPos, archivo)
    if sections:
        materias = _format_materias(sections, archivo)
        return materias, indexPos
    return [], indexPos

def _load_email():
    data = {}
    for line in ORIGIN_EMAILS.read_text().split("\n"):
        name, email = line.split(',')
        if '@' in email:
            while '  ' in name:
                name = name.replace("  ", " ")
            data[name.strip()] = email.strip()
    return data

def compare_name(name, emails):
    for nameEmail, email in emails.items():
        if len(nameEmail) == len(name):
            diff = 0
            for letter in range(len(name)):
                if name[letter] != nameEmail[letter]:
                    diff += 1
            if diff < 3:
                return email

def _get_email(name):
    emails = _load_email()
    name = name.upper().strip()
    email = emails.get(name, None)
    if email is not None:
        return email
    email = compare_name(name, emails)
    if email is not None:
        return email
    name = name.replace("Á", "A").replace("É", "E").replace("Í", "I").replace("Ó", "O").replace("Ú", "U")
    email = emails.get(name, None)
    if email is not None:
        return email
    email = compare_name(name, emails)
    if email is not None:
        return email
    name = name.replace("Ñ", "N")
    email = emails.get(name, None)
    if email is not None:
        return email
    email = compare_name(name, emails)
    if email is not None:
        return email
    logging.error(f'No se encontro email para {name}')
    return email

    

def _parse_pdf(archivo:Path, periodoSpam)->dict:
    '''
    corre todas las funciones necesarias para que la info de un pdf quede en un dict
    '''
    content = _convert_pdf_json(archivo)
    if not checkFile(content):
        logging.error('Hubo un problema con el archivo. Es posible que el formato del archivo sea diferente.')
        return None, None
    indexPos = checkPeriodo(content, archivo, periodoSpam)
    cedula, name = _get_nombre_pta(content, indexPos)
    email = _get_email(name)
    materias, indexPos = _get_clases(content, indexPos, archivo)
    descargas = _get_descarga(content, indexPos, archivo)
    return cedula, {
            'cedula': cedula,
            'nombre': name,
            'email': email,
            'materias': materias,
            'descargas': descargas
            }


def main_parse_pta(periodoSpam, path:str=None, modelo=False)->dict:
    '''
    corre todas las funciones necesarias para obtener toda la info de los pta que hayan en una carpeta
    '''
    if not modelo:
        path = _set_path(path)
        files = _pdf_filter(path)
        ptas = {}
        position = set()
        for index, archivo in enumerate(files):
            logging.info(f'Trabajando en "{archivo.name}"...')
            cedula, content = _parse_pdf(archivo, periodoSpam)
            ptas[cedula] = content
        destino = Path.cwd() / 'ptas_analizados.json'
        destino.write_text(json.dumps(ptas))
    else:
        archivo = Path.cwd() / 'LUCIO SEBASTIAN CASTRO.pdf'
        #archivo = Path.cwd() / 'LOU ANTONIO GÓMEZ ROBINSON.pdf'
        ptas = {}
        cedula, content = _parse_pdf(archivo, periodoSpam)
        ptas[cedula] = content
    print(f'{len(ptas)} PTAs han sido analizados. Revise "mi_log.log" para ver información adicional.')


main_parse_pta('2024 - 2', modelo=False)
