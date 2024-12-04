import pymupdf  # Esta es la librería PyMuPDF
import re
from pathlib import Path
import json
import logging

# Configuración para guardar los logs en un archivo
logging.basicConfig(
    filename='mi_log.log',         # Nombre del archivo de logs
    level=logging.WARNING,             # Nivel mínimo de registro
    format='%(asctime)s - %(levelname)s - %(message)s'  # Formato del log
)

class Pta_analyzer:

    ORIGIN_EMAILS = Path.cwd() / 'email_docentes_BA.csv'

    def __init__(self, periodoSpam, path:str=None):
        self.periodoSpam = periodoSpam.replace(" ", "")
        self.path = self._set_path(path)
        self.files = self._pdf_filter()
        self.ptas = {}
        self.persons = []
        self.list_emails = self._load_email()

    def _set_path(self, path:str=None)->Path:
        '''
        define el path como objeto Path
        '''
        if path:
            return Path.cwd() / path
        else:
            return Path.cwd() / 'PTA_BA_2024-1'

    def _pdf_filter(self)->list:
        '''
        devuelve la ruta para los archivos con ext .pdf
        '''
        files = []
        for archivo in self.path.iterdir():
            if archivo.suffix.lower() == ".pdf":
                files.append(archivo)
        return files

    def _load_email(self):
        data = {}
        for i, line in enumerate(self.ORIGIN_EMAILS.read_text().split("\n"), 1):
            try:
                name, email = line.split(',')
                if '@' in email:
                    while '  ' in name:
                        name = name.replace("  ", " ")
                    data[name.strip()] = email.strip().lower()
            except:
                logging.warning(f'No fue posible obtener email en la linea {i} del archivo {self.ORIGIN_EMAILS.name}')
        return data

    def get_all_users(self):
        '''
        corre todas las funciones necesarias para obtener toda la info de los pta que hayan en una carpeta
        '''
        for index, archivo in enumerate(self.files):
            logging.info(f'Trabajando en "{archivo.name}"...')
            p = Person(archivo, self.list_emails, self.periodoSpam)
            self.persons.append(p)
            cedula, content = p.getMainData()
            #cedula, content = _parse_pdf(archivo)
            self.ptas[cedula] = content
        filename = f'ptas_analizados{self.periodoSpam}.json'.replace(" ", "")
        destino = Path.cwd() / filename
        destino.write_text(json.dumps(self.ptas))

    def get_one_user(self, archivo):
        '''
        corre todas las funciones necesarias para obtener la info de un pta indicado en archivo
        '''
        archivo = Path(archivo)
        #archivo = Path.cwd() / 'LOU ANTONIO GÓMEZ ROBINSON.pdf'
        p = Person(archivo, self.list_emails, self.periodoSpam)
        self.persons.append(p)
        cedula, content = p.getMainData()
        #cedula, content = _parse_pdf(archivo)
        self.ptas[cedula] = content
        print(json.dumps(self.ptas, indent=2))

    


class Person:

    def __init__(self, archivo, list_emails, periodoSpam):
        self.archivo = archivo
        self.list_emails = list_emails
        self.periodoSpam = periodoSpam
        self._parse_pdf()

    def _convert_pdf_json(self)->dict:
        '''
        convierte el pdf a json
        '''
        texto = []
        pdf_document = pymupdf.open(self.archivo)
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

    def _get_descarga(self, indexPos)->dict:
        '''
        corre las funciones para extraer y organizar la info relacionada con la descarga
        '''
        if not self.content[indexPos]['lines'][0]['spans'][0]['text'] == 'Descargas':
            while indexPos < len(self.content):
                if 'Descargas' in self.content[indexPos]['lines'][0]['spans'][0]['text']:
                    break
                indexPos += 1
        indexPos += 1
        if not self.content[indexPos]['lines'][0]['spans'][0]['text'] == 'Tipo Actividad':
            logging.error(f'{self.archivo} no encuentra "Descargas->Tipo Actividad" con el indexPos')
            return 'error'
        indexPos += 1
        descarga = []
        while len(self.content[indexPos]['lines']) > 2:
            tipo_actividad = ''
            for span in self.content[indexPos]['lines'][0]['spans']:
                tipo_actividad += span['text']
            descripcion = ''
            for line in self.content[indexPos]['lines'][1:]:
                for span in line['spans']:
                    descripcion += span['text']
            descarga.append({'tipo_actividad':tipo_actividad, 'descripcion': descripcion})
            indexPos += 1
        return descarga

    def checkFile(self):
        for entry in self.content:
            if entry['lines'][0]['spans'][0]['text'] == 'Responsabilidad y Vinculación Docente IES':
                return True

    def _checkPeriodo(self):
        indexPos = 0
        while indexPos < len(self.content):
            for line in self.content[indexPos]['lines']:
                for span in line['spans']:
                    if self.periodoSpam in span['text'].replace(" ", ""):
                        return indexPos
            indexPos += 1
        logging.error(f'{self.archivo.name} parece no tener fecha de periodo')

    def _get_nombre_pta(self, indexPos)-> str:
        '''
        obtiene el nombre y la cedula del docente
        '''
        while indexPos < len(self.content):
            if 'Documento' in self.content[indexPos]['lines'][0]['spans'][0]['text']:
                cedula = self.content[indexPos+1]['lines'][0]['spans'][0]['text']
                nombre = self.content[indexPos+1]['lines'][1]['spans'][0]['text']
                return cedula, nombre
            indexPos += 1
        return None, None
        
    def _get_materias_sections(self, indexPos:int)->list:
        sections = []
        while indexPos < len(self.content):
            if 'Lunes' in self.content[indexPos]['lines'][0]['spans'][0]['text']:
                materia = ''
                for index, line in enumerate(self.content[indexPos-1]['lines']):
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
            elif 'Descargas' in self.content[indexPos]['lines'][0]['spans'][0]['text']:
                return sections, indexPos
            elif len(sections) > 0:
                for line in self.content[indexPos]['lines']:
                    foundGroup = False
                    for span in line['spans']:
                        if 'Grupo' in span['text']:
                            foundGroup = True
                        if span['text'] != '-' and foundGroup:
                            sections[-1].append(span['text'])
            indexPos += 1

    def _format_materias(self, sections:list)->list:
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

    def _get_clases(self, indexPos:int)->list[dict]:
        '''
        corre todas las funciones para que las clases queden almacenadas en una lista de dict
        '''
        sections, indexPos = self._get_materias_sections(indexPos)
        if sections:
            materias = self._format_materias(sections)
            return materias, indexPos
        return [], indexPos


    def _compare_name(self, name):
        for nameEmail, email in self.list_emails.items():
            if len(nameEmail) == len(name):
                diff = 0
                for letter in range(len(name)):
                    if name[letter] != nameEmail[letter]:
                        diff += 1
                if diff < 3:
                    return email

    def _get_email(self):
        name = self.name.upper().strip()
        email = self.list_emails.get(name, None)
        if email is not None:
            return email
        email = self._compare_name(name)
        if email is not None:
            return email
        name = name.replace("Á", "A").replace("É", "E").replace("Í", "I").replace("Ó", "O").replace("Ú", "U")
        email = self.list_emails.get(name, None)
        if email is not None:
            return email
        email = self._compare_name(name)
        if email is not None:
            return email
        name = name.replace("Ñ", "N")
        email = self.list_emails.get(name, None)
        if email is not None:
            return email
        email = self._compare_name(name)
        if email is not None:
            return email
        logging.error(f'No se encontro email para {name}')
        return email

    def createMateria(self, code, name):
        return {
        'code': code,
        'materia': f"{name}"
        }

    
    def getMateriasPtaOldVersion(self):
        start = {}
        end = {}
        result = []
        for item in range(len(self.content)):
            for line in range(len(self.content[item]['lines'])):
                for span in range(len(self.content[item]['lines'][line]['spans'])):
                    texto = self.content[item]['lines'][line]['spans'][span].get('text')
                    if 'Materia' in texto:
                        start = {'i': item, 'l': line, 's':span}
                    elif 'Descargas' in texto:
                        end = {'i': item, 'l': line, 's':span}
                    if start and not end and item > start['i'] and line == 0:
                        if texto == 'No se encontraron registros':
                            return 'No se encontraron registros'
                        if texto == 'No existe horario gestionado':
                            continue
                        if '-' in texto:
                            code, *name = texto.split(" - ")
                            if code.isdigit():
                                if len(name) == 1:
                                    result.append(self.createMateria(code, name[0]))
                                elif len(name) == 2 and name[1]:
                                    result.append(self.createMateria(code, " - ".join(name)))
                                elif self.content[item]['lines'][line+1]['spans'][span].get('text') not in ['NORMAL']:
                                    name.append(self.content[item]['lines'][line+1]['spans'][span].get('text'))
                                    result.append(self.createMateria(code, " - ".join(name)))
                                else:
                                    logging.warning(f'Parece haber una anomalía en las materias del archivo {self.archivo.name}: {texto}')
                            else:
                                logging.warning(f'Parece haber una anomalía en las materias del archivo {self.archivo.name}: {texto}')
                        else:
                            logging.warning(f'Parece haber una anomalía en las materias del archivo {self.archivo.name}: {texto}')
        if not result:
            logging.warning(f'No registra materias {self.archivo.name}')
        return result

    def _parse_pdf(self)->dict:
        '''
        corre todas las funciones necesarias para que la info de un pdf quede en un dict
        '''
        self.content = self._convert_pdf_json()
        if not self.checkFile():
            logging.error('Hubo un problema con el archivo. Es posible que el formato del archivo sea diferente.')
            return
        indexPos = self._checkPeriodo()
        if not indexPos:
            indexPos = 0
        self.cedula, self.name = self._get_nombre_pta(indexPos)
        if not self.name:
            logging.error('Hubo un problema con el archivo. Es posible obtener el nombre.')
        if not self.cedula:
            logging.error('Hubo un problema con el archivo. Es posible obtener la cedula.')
        self.email = self._get_email()
        self.materias, indexPos = self._get_clases(indexPos)
        if not self.materias:
            self.materias = self.getMateriasPtaOldVersion()
        if not self.materias:
            logging.error('No se lograron encontrar materias')
        if self.materias == 'No se encontraron registros':
            self.materias = []
        self.descargas = self._get_descarga(indexPos)

    def getMainData(self):
        return self.cedula, {
                'cedula': self.cedula,
                'nombre': self.name,
                'email': self.email,
                f'{self.periodoSpam}' : {
                    'materias': self.materias,
                    'descargas': self.descargas
                    }
                }



analyzer1 = Pta_analyzer('2024-1', 'PTA_BA_2024-1')
analyzer1.get_all_users()
analyzer2 = Pta_analyzer('2024-2', 'PTA_BA_2024-2')
analyzer2.get_all_users()
