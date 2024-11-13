from pathlib import Path

old = 'new_entry_gruposinvestigacion'
new = 'new_entry_user'

root = Path('/home/Ubuntu_2023/Documents/Documents/PythonProjects/BellasArtes2/app/interface/db')

for item in root.iterdir():
    if 'section' in item.name and '.py' == item.suffix:
        content = item.read_text()
        if old in content:
            print(item)
            content = content.replace(old,new)
            item.write_text(content)


