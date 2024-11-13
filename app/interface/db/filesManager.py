import time
from pathlib import Path
from app.interface.db.get_Data import getTables
from app.interface.db.db_manager import _check_entry
from werkzeug.utils import secure_filename

def saveFile(section, index_entry, initform):
    filenameKey = f"file_{index_entry}_{section}"
    file = initform.get(filenameKey)
    name_file = initform[section][index_entry].get('name_file')
    period_spam = initform.get('period_spam')
    if file and name_file and period_spam:
        destinationFolder = _getDirectory(period_spam, section)
        uniqueName = _getUniqueName(file, destinationFolder)
        file.save(uniqueName)
        return uniqueName.name
    return name_file
           
def _getDirectory(period_spam, section):
    folder = Path.cwd() / 'userFiles'
    if not folder.exists() or not folder.is_dir():
        folder.mkdir()
    folderPeriod = folder / period_spam
    if not folderPeriod.exists() or not folderPeriod.is_dir():
        folderPeriod.mkdir()
    folderSection = folderPeriod / section
    if not folderSection.exists() or not folderSection.is_dir():
        folderSection.mkdir()
    return folderSection

def _getUniqueName(file, destinationFolder):
    while True:
        randomPart = str(time.time()).replace(".", "")
        filename = secure_filename(file.filename)
        uniqueName = destinationFolder / f'{randomPart}___BA{filename}'
        if not uniqueName.exists():
            return uniqueName

def getFile(params, id_person):
    content = {}
    content['user'] = id_person
    content['index_entry'] = params['index_entry']
    content['period_spam'] = params['period_spam']
    table = getTables(params['section'])[0]
    entry = _check_entry(content, table, index_entry=True)
    filename = None
    if hasattr(entry, 'name_file'):
        filename = entry.name_file
    path_file = _getDirectory(params['period_spam'], params['section'])
    if not path_file.exists():
        path_file = None
    return path_file, filename

    
    
