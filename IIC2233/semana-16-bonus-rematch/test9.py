import re

texto = "El cliente usó la tarjeta 1234-5678-9012-3456-5444 para pagar."

# Buscamos 3 bloques de 4 dígitos seguidos de un guion
patron = r"\d{4}-\d{4}-\d{4}-"
# Lo reemplazamos por texto plano
texto_censurado = re.sub(patron, "XXXX-XXXX-XXXX-", texto)

print(texto_censurado)
# Salida: El cliente usó la tarjeta XXXX-XXXX-XXXX-3456 para pagar.