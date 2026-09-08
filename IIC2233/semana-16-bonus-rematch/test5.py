"""
El Sanitizador de Contraseñas (Validación Compleja)
Las validaciones de contraseñas seguras no se pueden hacer con un Regex lineal simple; requieren mirar "hacia adelante".

El desafío: Crea un Regex que valide si una contraseña cumple con:

Al menos 8 caracteres de largo.

Al menos una letra mayúscula.

Al menos una letra minúscula.

Al menos un número.

Al menos un carácter especial (ej: @, $, !, *).

"""

import re

lista_contrasenas = ["hola", "choripanao_xd", "Contrasena@_12", 
                    "1231231231", "Holaaaaa", "H19134139", "WAZAAAAA", "Hh1@",
                    "Quepasaviejo1"]

patron = r"(?=.*[A-Z])(?=.*[a-z])(?=.*[\d])(?=.*[@$\!_]).{8,}$"

for s in lista_contrasenas:
    if re.match(patron, s):
        print(s)
