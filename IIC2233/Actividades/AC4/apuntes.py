"""
----------------------------------
Paradigmas de programación:
----------------------------------
Procedimental: Programación líneal siguiendo 
una serie de instrucciones.

Vectorial: enfocado en el cálculo matemático donde existe
un paralelismo implícito en los cálculos.

Declarativa: El computador busca la mejor manera para resolver
el problema declarado por el usuario de la manera más eficiente.

Orientada a objetos: Programación con modelaje en funcionalidades mediante
la interacción con y entre objetos, donde se utilizan todo lo que se desglozan
de estos (atributos, funciones).

Funcional: Programación procedimental de alto nivel. Se aborda la solución
del problema mediante estructura como un conjunto de funciones


Python es un lenguaje MULTIPARADIGMA, o sea, nuestros programas
pueden ser un conjunto de todos estos paradigmas mencionados.

----------------------------------
Programación Funcional - Claves:
----------------------------------
- Dado un valor de entrada se genera el mismo y único valor de salida
- Este valor depende ÚNICAMENTE de los valores de entrada de la función
- Focus en el Output de la función

- Seguridad/certeza de que los valores dentro de la función no cambian
- Scope:  cuando se ejecuta una función no se cambian otros
valores fuera de su ámbito de alcance

-Todo esto para dar - Claridad al código -

----------------------------------
Funciones Puras
----------------------------------

- Funciones que no poseen efectos colaterales (secundarios), pensando en el código.
- Pureza: Grado de dependencia de la función hacia el sistema (contexto en el que se usa)

En resumen, una función pura retorna lo mismo para el mismo input, y no posee efectos
secuntarios.

----------------------------------
Ejemplo:
    """
mi_lista = [1, 2, 3]
# Función impura
def agregar_elemento(número: int) -> None:
    mi_lista.append(número)


"""
Si ejecutamos en reiteradas ocasiones la función se puede observar que
el resultado de la ejecución cambia, pese a que el valor de entrada 
no ha cambiado como parámetro
"""

"""
for i in range(1, 6): #i variable desechable
    agregar_elemento(4)
    print(f'Ejecución {i}: {mi_lista}')
"""


"""Para evitar que la función sea impura, deberemos asegurarnos
que eñ acceso a la lista se haga por medio del input de la función
(ingresar la lista y retornar una copia de esta modificada)"""
mi_lista = [1, 2, 3]
# Función pura
def agregar_elemento(lista: list, número: int) -> list:
    copia_lista = lista.copy()
    copia_lista.append(número)

    return copia_lista


for i in range(1, 6):
    nueva_lista = agregar_elemento(mi_lista, 4)
    print(f'Ejecución {i}: {mi_lista} {nueva_lista}')

"""Ahora la función agregar_elemento SÍ es pura porque:
- Su valor de retorno depende solamente de los valores de entrada
- Como se genera una copia de la lista para modificar, la lista original
no sufre cambios (intacta) y se retorna otra lista modificada a partir de la
lista original, así, se evitaron efectos secundarios

----------------------------------
Consecuencias de la Programación Funcional
----------------------------------
- Ya no se modifican elementos externos a una función
- podemos descartar revisar funciones puras cuando tenemos que un valor
o una estructura cambia inesperadamente.
- El Output solo depende del input
- Chao a los efectos secundarios, no se puede razonar con interaciones
de tipo: for o while
- Código limpio y conciso


Decorador @cache:
- Funciona con las funciones Puras
¿Cómo funciona?

Cuando decoras una función con @functools.cache:

La primera vez que llamas a la función con ciertos argumentos, 
Python ejecuta la función normalmente y guarda (en memoria) el 
resultado asociado a esos argumentos.

Si vuelves a llamar a la función con los mismos argumentos, 
en lugar de volver a ejecutar el código, devuelve el valor 
guardado inmediatamente.

Esto ahorra tiempo de ejecución si la función es costosa 
(por ejemplo, cálculos recursivos, consultas repetidas, etc.).

"""
from functools import cache

@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(40))  # Se calcula rápido gracias al cache


# ---------------------------------------------------
# ---------------------------------------------------
# ---------------------------------------------------


"""
----------------------------------
Funciones Generadoras
----------------------------------

Recuerdo de generadoress (???):
- Nos permiten iterar sobre secuencias de datos
sin la necesidad de almacenarlos en alguna estructura especial,
ahorrando memoria RAM.
- Una vez usado terminada la iteración el generador desaparece.

"""

from typing import Generator

def conteo_decreciente(n: int) -> Generator:
    print(f"Contando en forma decreciente desde {n}")
    while n > 0:
        yield n
        n -= 1

x = conteo_decreciente(4)

"""
Esto se debe a que cuando se invoca la función generadora, esta retorna un generador. Luego, x
es un generador de números desde el 10 hasta el 1.
"""
print(type(x))

"""
Podemos usar el generador directamente en un for, ya que como vimos estos implementan
__iter__ devolviendo self.
"""
for number in x:
 print(number)


"""
También se puede usar next
"""
x = conteo_decreciente(5)
print(next(x))

