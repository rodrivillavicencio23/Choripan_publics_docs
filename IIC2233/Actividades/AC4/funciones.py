from functools import reduce
from itertools import product
from typing import Generator

from utilidades import Pelicula, Genero


# ----------------------------------------------------------------------------
# Parte I: Cargar dataset
# ----------------------------------------------------------------------------

def cargar_peliculas(ruta: str) -> Generator:
    """
    Cargar archivos
    """
    # Ruta ya se pasa con la dirección a la carpeta
    with open(ruta, "r", encoding="UTF-8") as archivo:
        next(archivo)
        for linea in archivo:
            nueva_linea = linea.strip().split(",")
            pelicula = Pelicula(int(nueva_linea[0]), nueva_linea[1], nueva_linea[2],int(nueva_linea[3]), float(nueva_linea[4]))
            yield pelicula

# ----------------------------------------------------------------------------
# Parte II: Consultas sobre generadores
# ----------------------------------------------------------------------------


def obtener_directores(generador_peliculas: Generator) -> Generator:
    """
    Retorna un generador con el nombre de todos los directores.
    """
    generador_directores = map(lambda movie: movie.director, generador_peliculas)
    return generador_directores


def obtener_str_titulos(generador_peliculas: Generator) -> str:
    """
    Genera un str con todos los títulos de las películas separados por ", ".
    """
    titulos = map(lambda movie: movie.titulo if type(movie) != str else "", generador_peliculas)
    try:
        titulos = reduce(lambda movie1, movie2: f"{movie1}, {movie2}", titulos)
    except TypeError:
        return ""
    else:
        return titulos


def filtrar_peliculas(
    generador_peliculas: Generator,
    director: str | None = None,
    rating_min: float | None = None,
    rating_max: float | None = None,
) -> filter:
    """
    Filtra los elementos del generador de Películas según lo indicado en el input.
    """
    # Esto está bien, confía, esto me retorna el generador de pelis filtradas
    if director != None:
        generador_peliculas = filter(lambda movie: movie.director == director, generador_peliculas)
    if rating_min != None:
        generador_peliculas = filter(lambda movie: movie.rating >= rating_min, generador_peliculas)
    if rating_max != None:
        generador_peliculas = filter(lambda movie: movie.rating <= rating_max, generador_peliculas)
    
    return generador_peliculas


def filtrar_titulos(
    generador_peliculas: Generator,
    director: str,
    rating_min: float,
    rating_max: float
) -> Generator:
    """
    Genera un str con todos los títulos de las películas separados
    por ", ". Solo se consideran las películas que tengan el mismo
    director que el indicado, tengan un rating igual o mayor al
    rating_min y un rating igual o menor al rating_max.
    """
    return "COMPLETAR"


def filtrar_peliculas_por_genero(
    generador_peliculas: Generator,
    generador_generos: Generator,
    genero: str | None = None,
) -> Generator:
    """
    Crea un generador con todas las combinaciones posibles entre
    el generador de películas y el generador de géneros.
    Después, filtra las pares obtenidos y mantiene únicamente
    los que presentan el mismo id de película.
    Finalmente, retorna una lista con todos los pares pertenecientes
    a la categoría indicada.
    """
    return "COMPLETAR"
