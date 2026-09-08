

def saludar(nombre: str) -> str:
    return f"Hola {nombre}"

print(saludar(123))

"""
🔹 Clases utilizadas
1. Alumno (abstracta)

Hereda: ABC (de abc)
Atributos:

nombre: str
numero_alumno: int
libros_pedidos: List[Libro]
major: str (property: para validar existencia en universidad)
minor: str (property: idem)


Métodos:

arrendar_libro(libro: Libro, biblioteca: Biblioteca) -> bool (abstracto)
devolver_libro(libro: Libro, biblioteca: Biblioteca) -> None (común para todos)



2. AlumnoPregrado (concreta)

Hereda: Alumno
Atributos:

ppa: float
limite_libros: int


Métodos:

arrendar_libro(libro: Libro, biblioteca: Biblioteca) -> bool (verifica límite)



3. AlumnoPostgrado (concreta)

Hereda: Alumno
Atributos:

tema_tesis: str


Métodos:

arrendar_libro(libro: Libro, biblioteca: Biblioteca) -> bool (sin límite)



4. Libro (concreta)

Atributos:

titulo: str
autor: str
paginas: int



5. Biblioteca (concreta)

Atributos:

campus: str
libros_disponibles: List[Libro]


Métodos:

disponibilidad(libro: Libro) -> bool
remover_libro(libro: Libro) -> None
agregar_libro(libro: Libro) -> None
"""