import re

urls = [
    "https://iic2233.uc.cl",
    "http://example123.com",
    "ftp://server.com",
    "https://mi-sitio_web.cl",
    "https://bad@url.com"
]

patron = r"^https?://[\w-]+(\.[\w-]+)+$" #TODO: Escribir la expresión regular solicitada.

print([u for u in urls if re.match(patron, u)])