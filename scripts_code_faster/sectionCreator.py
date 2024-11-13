import json
from pathlib import Path

template = '{"programa_add": null, "materia_add": null, "code_add": null, "observaciones_add": null, "contenidos_especiales_add": null}'

name_section = 'section2_2'
especial_data = ''
base_de_datos = 'MisionalDocenciaAdicionales'



##############################

json_template = json.loads(template)

len_template = str(len(json_template))

template_keys = [x for x in json_template.keys()]

content_template = str(template_keys)

if especial_data:
    list_data = f"content['{especial_data}'] = json.dumps(content['{especial_data}'])"
else:
    list_data = ''

fields = ''
for x in template_keys:
    fields += f"\n        {x} = form['{x}'],"

fields = fields[1:].strip()

section_template = Path('/home/Ubuntu_2023/Documents/Documents/PythonProjects/BellasArtes2/scripts_code_faster/section_template.py')

content = section_template.read_text()

content = content.replace('**base_de_datos**', base_de_datos)
content = content.replace('**template**', template)
content = content.replace('**name_section**', name_section)
content = content.replace('**len_template**', len_template)
content = content.replace('**content_template**', content_template)
content = content.replace('**list_data**', list_data)
content = content.replace('**fields**', fields)

destino = Path(f'/home/Ubuntu_2023/Documents/Documents/PythonProjects/BellasArtes2/app/interface/db/{name_section}.py')

destino.write_text(content)



