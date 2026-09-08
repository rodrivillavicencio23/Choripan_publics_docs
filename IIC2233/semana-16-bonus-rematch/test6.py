"""
Enunciado:
Extractor de Atributos HTML/XML (Web Scraping Básico)
A veces necesitas extraer información de una página web sin querer importar librerías pesadas como BeautifulSoup.
El desafío: Extrae el contenido de texto y el enlace (href) de todas las etiquetas de anclaje <a> en un bloque de HTML.
Texto de prueba: <a href="https://github.com/perfil">Ver Perfil de GitHub</a>
Resultado esperado: Tu script debería devolver la tupla: ('https://github.com/perfil', 'Ver Perfil de GitHub').
"""
import pyrematch as REmatch

# in process
lista_scripts = ["""<a href="https://github.com/perfil">Ver Perfil de GitHub</a>""",
                 """<a href="https://youtube.com/jotate">Ver Perfil de Youtube de Jotate</a>"""]


patron = r'<a\shref="!link{[^"]+}">!text{[^<]+}</a>'
query = REmatch.reql(patron)

print("=" * 30, "\n Extrayendo datos \n", "=" * 30)

for doc in lista_scripts:
    for match in query.finditer(doc):
        # En REmatch, recuperamos los grupos nombrados con .group('nombre')
        link_encontrado = match.group('link')
        texto_encontrado = match.group('text')
        
        # Representamos el resultado final como la tupla solicitada
        resultado_tupla = (link_encontrado, texto_encontrado)
        print(f"Resultado: {resultado_tupla}")