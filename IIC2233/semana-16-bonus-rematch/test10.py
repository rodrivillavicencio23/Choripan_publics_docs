import re

texto_precios = "El café cuesta 3000 pesos y el sándwich cuesta 5000 pesos."

# Función que procesará cada coincidencia encontrada
def aplicar_descuento(match):
    # match.group() nos da el string numérico encontrado (ej: "3000")
    precio_actual = int(match.group())
    precio_final = int(precio_actual * 0.90) # Quitamos el 10%
    return str(precio_final)

# Buscamos cualquier bloque de números
patron_numeros = r"\d+"

# Pasamos la función 'aplicar_descuento' SIN paréntesis como segundo argumento
texto_oferta = re.sub(patron_numeros, aplicar_descuento, texto_precios)

print(texto_oferta)
# Salida: El café cuesta 2700 pesos y el sándwich cuesta 4500 pesos.