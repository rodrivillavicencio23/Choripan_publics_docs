"""
Parseador de Archivos Markdown (Conversión de Formatos)

Los editores de texto modernos leen archivos .md y los transforman a HTML usando expresiones regulares para renderizarlos en la pantalla.

El desafío: Diseña un script que traduzca la sintaxis de negrita y enlaces de Markdown a etiquetas HTML.

Texto de prueba: Hola, esto es texto en negrita y este es un [enlace a Google](https://google.com).

Resultado esperado: Hola, esto es <strong>texto en negrita</strong> y este es un <a href="https://google.com">enlace a Google</a>.
"""

import pyrematch as REmatch



patron = r'<a\shref="!link{[^"]+}">!text{[^<]+}</a>'

query = REmatch.rql(patron)
