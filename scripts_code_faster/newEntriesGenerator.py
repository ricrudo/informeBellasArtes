from new_entries_generator import new_entries_generator
from pathlib import Path


response = ""
origin = Path.cwd().parent / 'app' / 'domain' / 'models.py'
destino = Path.cwd() / 'new_entries_generator' / 'results'
new_entries_generator(origin, destino, copy_to_folder)
