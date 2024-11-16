from pathlib import Path
import json

p1 = json.loads(Path("/home/Ubuntu_2023/Documents/Documents/PythonProjects/BellasArtes2/parse_pta/ptas_analizados2024-1.json").read_text())
p2 = json.loads(Path("/home/Ubuntu_2023/Documents/Documents/PythonProjects/BellasArtes2/parse_pta/ptas_analizados2024-2.json").read_text())
pd = Path("/home/Ubuntu_2023/Documents/Documents/PythonProjects/BellasArtes2/parse_pta/ptas_analizados2024_all.json")
pddict = {}

print("Profesores que no tiene PTA 2024-2")
for cedula, content in p1.items():
    pddict[cedula] = content
    if cedula in p2:
        pddict[cedula].update(p2[cedula])
    else:
        print(f"{content['nombre']}")

print("\nProfesores que no tiene PTA 2024-1")
for cedula, content in p2.items():
    if cedula not in p1:
        pddict[cedula] = content
        print(f"{content['nombre']}")


pd.write_text(json.dumps(pddict))
