from pathlib import Path
import json

path = Path("/home/Ubuntu_2023/Documents/Documents/PythonProjects/BellasArtes2/parse_pta/ptas_analizados2024-2.json")

data = json.loads(path.read_text())

yo = data.get('CC 16079469')

yo_save = Path.cwd() / 'TestUser1.json'

yo_save.write_text(json.dumps({'CC 16079469':yo}))
