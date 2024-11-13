from pathlib import Path
import re

testApiDir = Path.cwd() / 'testApi'

ommit = [
    '__ini__.py',
    'converter.py'
]


def cleaner(path):
    content = [x.strip() for x in path.read_text().split('\n')]
    new_content = []
    counterData = 0
    urlFound = False
    for line in content:
        if 'import requests' in line:
            continue
        if "main_url = 'http://127.0.0.1:5000'" in line:
            continue
        if re.search(r'^def .+\:$', line):
            continue
        if re.search(r'^response \= requests\.post.+$', line):
            continue
        if re.search(r'if response\.text.+$', line):
            continue
        if re.search(r'else\:$', line):
            continue
        if re.search(r'print\(.+$', line):
            continue
        dataFind = re.search(r'^data( \= .+)$', line)
        if dataFind:
            counterData += 1
            if counterData == 2:
                new_content.append('datafail = {')
            else:
                new_content.append(line)
            continue
        urlFind = re.search(r'^url \= main_url \+ (.+)$', line)
        if urlFind:
            if not urlFound:
                new_content.append(f'url = {urlFind.group(1)}')
                urlFound = True
            continue
        new_content.append(line)
    return "\n".join(new_content)

def createFiles(path, new_content):
    old_content = path.read_text()
    old_path = path.parent / path.name.replace('.py', 'old.py')
    old_path.write_text(old_content)
    path.write_text(new_content)

for file in testApiDir.iterdir():
    if file.suffix == '.py':
        if file.name not in ommit:
            new_content = cleaner(file)
            createFiles(file, new_content)

