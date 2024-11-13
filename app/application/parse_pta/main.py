import fitz  # Esta es la librería PyMuPDF
import re
from pathlib import Path

def _set_path(path:str=None)->Path:
    '''
    define el path como objeto Path
    '''
    if path:
        if not isinstance(path, Path):
            path = Path(path)
        return Path(path)
    else:
        return Path.cwd()

def _pdf_filter(path:Path)->list:
    '''
    Si el path es un directorio devuelve una lista con todos los archivos .pdf que esten dentro del el (no recursivo)
    Si es un archivo delvuelve el path como unico elemento de una lista
    '''
    if path.is_file():
        return [path]
    files = []
    for archivo in path.iterdir():
        if archivo.suffix.lower() == ".pdf":
            files.append(archivo)
    return files

def _convert_pdf_txt(archivo:Path)->str:
    '''
    convierte el pdf a texto
    '''
    texto = []
    pdf_document = fitz.open(archivo)
    for pagina_num in range(pdf_document.page_count):
        pagina = pdf_document[pagina_num]
        texto_pagina = pagina.get_text()
        texto.append(texto_pagina)
    pdf_document.close()
    return "\n".join(texto)

def _get_extract_from_str(txt_content:str, patron:re, pos_datos_grupo:int=0)->str:
    '''
    obtiene del txt con regular expresion
    '''
    resultado = patron.search(txt_content[pos_datos_grupo:])
    if resultado:
        return resultado.group(1).strip()

def _get_materias_bloque_from_str(txt_content:str)->str:
    '''
    separa la seccion del texto que esta entre el segundo "Unidad Regional" y "Descargas"
    que corresponde al area que contiene las materias
    '''
    patron_datos_grupo = re.compile(r"Datos del Grupo")
    pos_datos_grupo = re.search(patron_datos_grupo, txt_content).end()
    patron = re.compile(r"Unidad Regional[^\n]*\n(.*?)\nDescargas", re.DOTALL)
    return _get_extract_from_str(txt_content, patron, pos_datos_grupo)

def _separate_str_by_clases(materias_bloque:str)->list:
    '''
    separa el bloque de todas las materias en una lista con la info de cada materia
    '''
    lineas_fragmento = materias_bloque.split("\n")
    materias = []
    bloque_actual = ""
    for linea in lineas_fragmento:
        if re.match(r"\d{3,} - ", linea):
            if bloque_actual:
                materias.append(bloque_actual.strip())
            bloque_actual = linea
        else:
            bloque_actual += "\n" + linea
    if bloque_actual:
        materias.append(bloque_actual.strip())
    return materias

def _get_materias_detallado(materias:str)->dict:
    '''
    parse la informacion de la materia y devuelve en un dict
    el codigo, nombre, grupo, lugar, dia y hora de la materia
    '''
    dict_materias = []
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
                    horarios.append({
                        'dia': list_dias[i],
                        'lugar': coincidencia.group(1),
                        'inicio': coincidencia.group(2),
                        'fin': coincidencia.group(3)
                        })
        info_clase = {
            "class code": codigo,
            "class name": nombre,
            "group": grupo,
            "horarios": horarios
        }
        dict_materias.append(info_clase)
    return dict_materias

def _get_materias(txt_content:str)->list[dict]:
    '''
    corre todas las funciones para que las clases queden almacenadas en una lista de dict
    '''
    materias_bloque = _get_materias_bloque_from_str(txt_content)
    if materias_bloque:
        materias = _separate_str_by_clases(materias_bloque)
        return _get_materias_detallado(materias)

def _get_nombre_pta(txt_content:str)-> str:
    '''
    obtiene el nombre y la cedula del docente
    '''
    patron = re.compile(r"Nombre[^\n]*\n(.*?)\nGesti", re.DOTALL)
    string = _get_extract_from_str(txt_content, patron)
    if string:
        return string.split('\n')

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

    lineas = txt_descarga.split('\n')
    for i in range(0, len(lineas), 3):
        descargas.append({})
        descargas[-1]['tipo de actividad'] = lineas[1]
        descargas[-1]['Descripcion'] = lineas[i+1]
        descargas[-1]['horas'] = int(lineas[i+2])
    return descargas

def _get_descarga(txt_content:str)->dict:
    '''
    corre las funciones para extraer y organizar la info relacionada con la descarga
    '''
    txt_descarga = _descarga_to_str(txt_content)
    return _agrupar_descarga(txt_descarga)

def _parse_pdf(archivo:Path, ptas:dict)->dict:
    '''
    corre todas las funciones necesarias para que la info de un pdf quede en un dict
    '''
    txt_content = _convert_pdf_txt(archivo)
    cedula, name = _get_nombre_pta(txt_content)
    materias = _get_materias(txt_content)
    descargas = _get_descarga(txt_content)
    return cedula, {
            'cedula': cedula,
            'nombre': name,
            'materias': materias,
            'descargas': descargas
            }

def main_parse_pta(path:str=None)->dict:
    '''
    corre todas las funciones necesarias para obtener toda la info de los pta que hayan en una carpeta
    '''
    path = _set_path(path)
    files = _pdf_filter(path)
    ptas = {}
    for archivo in files:
        cedula, content = _parse_pdf(archivo, ptas)
        ptas[cedula] = content
    breakpoint()

if __name__ == '__main__':
    main_parse_pta()

