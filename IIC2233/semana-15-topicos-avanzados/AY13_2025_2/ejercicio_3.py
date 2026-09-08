import re

archivos = ["main.py", "readme.md", "juego.PY", "test.pyc", "dccasino.py"]
patron = r"[\w]+\.(py)$" #TODO: Escribir la expresión regular solicitada.
print([a for a in archivos if re.match(patron, a)])