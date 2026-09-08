# -----------------------------------------------------
# Imports y Modularización
from typing import Generator, List, Tuple
from itertools import groupby, tee, islice

from backend.consultas_g34 import (planetas_por_estadisticas, ganancias_potenciales_por_planeta, 
                           planetas_visitados_por_nave, mineral_por_nave, porcentaje_extraccion,
                           resultado_mision)

from utilidades import (
    Astronauta,
    Nave,
    Tripulacion,
    Planeta,
    Mineral,
    PlanetaMineral,
    Mision,
    MisionMineral,
    radio_planeta)
# -----------------------------------------------------

# -------------------
# ----- Cargas -----
# -------------------

# ---------------------------------
# Carga de Astronautaas
def cargar_astronautas(path: str) -> Generator[Astronauta, None, None]:
    with open(path, "r", encoding="UTF-8") as archivo:
        next(archivo)
        for linea in archivo:
            nueva_linea = linea.strip().split(",")
            astronauta = Astronauta(int(nueva_linea[0]), nueva_linea[1], nueva_linea[2])
            yield astronauta
# ---------------------------------
# Carga de Naves
def cargar_naves(path: str) -> Generator[Nave, None, None]: 
    with open(path, "r", encoding="UTF-8") as archivo:
        next(archivo)
        for linea in archivo:
            nueva_linea = linea.strip().split(",")
            nave = Nave(nueva_linea[0], nueva_linea[1],   
                        nueva_linea[2], int(nueva_linea[3]), 
                        float(nueva_linea[4]), float(nueva_linea[5]))
            yield nave
# ---------------------------------
# Carga de Tripulaciones
def cargar_tripulaciones(path: str) -> Generator[Tripulacion, None, None]:
    with open(path, "r", encoding="UTF-8") as archivo:
        next(archivo)
        for linea in archivo:
            nueva_linea = linea.strip().split(",")
            tripulacion = Tripulacion(
                int(nueva_linea[0]), str(nueva_linea[1]), 
                int(nueva_linea[2]), int(nueva_linea[3]))
            yield tripulacion
# ---------------------------------
# Carga de Planetas
def cargar_planetas(path: str) -> Generator[Planeta, None, None]: 
    with open(path, "r", encoding="UTF-8") as archivo:
        next(archivo)
        for linea in archivo:
            nueva_linea = linea.strip().split(",")
            planeta = Planeta(
                int(nueva_linea[0]), str(nueva_linea[1]), 
                float(nueva_linea[2]), float(nueva_linea[3]),
                str(nueva_linea[4]), str(nueva_linea[5]))
            yield planeta
# ---------------------------------
# Carga de Minerales
def cargar_minerales(path: str) -> Generator[Mineral, None, None]: 
    with open(path, "r", encoding="UTF-8") as archivo:
        next(archivo)
        for linea in archivo:
            nueva_linea = linea.strip().split(",")
            mineral = Mineral(int(nueva_linea[0]), nueva_linea[1], 
                            nueva_linea[2], int(nueva_linea[3]),
                            float(nueva_linea[4]))
            yield mineral
# ---------------------------------
# Carga de Planeta Mineral 
def cargar_planeta_minerales(path: str) -> Generator[PlanetaMineral, None, None]:
    with open(path, "r", encoding="UTF-8") as archivo:
        next(archivo)
        for linea in archivo:
            nueva_linea = linea.strip().split(",")
            planeta_mineral = PlanetaMineral(int(nueva_linea[0]), int(nueva_linea[1]),     
                                float(nueva_linea[2]), float(nueva_linea[3]))
            yield planeta_mineral
# ---------------------------------
# Carga de Mision
def cargar_mision(path: str) -> Generator[Mision, None, None]:
    with open(path, "r", encoding="UTF-8") as archivo:
        next(archivo)
        for linea in archivo:
            nueva_linea = linea.strip().split(",")

            valor_lograda = nueva_linea[5].strip()
            if valor_lograda == "True":
                lograda = True
            elif valor_lograda == "False":
                lograda = False
            else:
                lograda = None
            mision = Mision(int(nueva_linea[0]), nueva_linea[1], nueva_linea[2],
                            int(nueva_linea[3]), int(nueva_linea[4]), lograda)
            yield mision
# ---------------------------------
# Carga de Materiales Mision
def cargar_materiales_mision(path: str) -> Generator[MisionMineral, None, None]:
    with open(path, "r", encoding="UTF-8") as archivo:
        next(archivo)
        for linea in archivo:
            nueva_linea = linea.strip().split(",")
            mision_mineral = MisionMineral(int(nueva_linea[0]), int(nueva_linea[1]), 
                        float(nueva_linea[2]))
            yield mision_mineral
# ----------------------
# Consultas 1 generador
# ----------------------
def naves_de_material(generador_naves: Generator[Nave, None, None],
                    material: str) -> Generator[Nave, None, None]:
    generador_naves = filter(lambda nave: nave.material == material, generador_naves)
    return generador_naves

def misiones_desde_fecha(generador_misiones: Generator[Mision, None, None],
                         fecha: str, inverso: bool) -> Generator[Mision, None, None]:
    if inverso:
        return filter(lambda m: m.fecha <= fecha, generador_misiones)
    else:
        return filter(lambda m: m.fecha >= fecha, generador_misiones)
# ---------------------------------
# Naves por intervalo de carga (1 generador)
def naves_por_intervalo_carga(generador_naves: Generator[Nave, None, None], 
                            cargas: tuple[float, float]) -> Generator[Nave, None, None]:
    generador_naves = filter(lambda nave: 
                        cargas[0] <= nave.capacidad_minerales <= cargas[1], 
                        generador_naves)
    return generador_naves
# ---------------------------------
# Planetas con cantidad de minerales (1 generador)
def planetas_con_cantidad_de_minerales(generador_planeta_mineral: 
                                       Generator[PlanetaMineral, None, None], 
                                       id_mineral: int, cantidad_minima: int) -> List[int]:
    
    filtrados = filter(lambda pm: pm.id_mineral == id_mineral and 
        pm.cantidad_disponible * pm.pureza >= cantidad_minima,
        generador_planeta_mineral)
    return list(map(lambda pm: pm.id_planeta, filtrados))
# ---------------------------------
# Naves astronautas rango (1 generador)
def naves_astronautas_rango(generador_tripulacion: Generator[Tripulacion, None, None], 
                        rango: int, 
                        minimo_astronautas: int) -> Generator[Tuple[str, Generator], None, None]:
    
    minimo_astronautas = max(minimo_astronautas, 1)
    for patente, grupo in groupby(generador_tripulacion, key=lambda t: t.patente_nave):
        filtrados = filter(lambda t: t.rango >= rango, grupo)

        g1, g2 = tee(filtrados)
        cantidad = sum(1 for _ in g1)
        if cantidad >= minimo_astronautas:
            generador_ids = map(lambda t: t.id_astronauta, g2)
            yield (patente, generador_ids)
# ---------------------------------
# Cambiar rango astronauta (1 generador) 
def cambiar_rango_astronauta(generador_tripulacion: Generator[Tripulacion, None, None], 
                        id_astronauta: int, 
                        rango_astronauta: int) -> Generator[Tripulacion, None, None]:
    generador_tripulacion = map(
        lambda t: t._replace(rango=rango_astronauta) if t.id_astronauta == id_astronauta else t,
        generador_tripulacion)   
    return generador_tripulacion
# ---------------------------------
# Encontrar planetas cercanos (1 generador) 
def encontrar_planetas_cercanos(generador_planetas: Generator[Planeta, None, None], x1: int, 
                                y1: int, x2: int, y2: int, 
                                cantidad: int | None = None) -> Generator[Planeta, None, None]:
    
    generador_planetas = filter(lambda p: p.coordenada_x >= x1 
                                and p.coordenada_y >= y1, generador_planetas) 

    generador_planetas = filter(lambda p: x2 >= p.coordenada_x and 
                                y2 >= p.coordenada_y, generador_planetas)    
    if cantidad is not None:
        generador_planetas = islice(generador_planetas, cantidad)
    return generador_planetas
# ----------------------------------
# ----- Consultas 2 generadores -----
# ----------------------------------

# ---------------------------------
# Disponibilidad por planeta (2 generadores) 
def disponibilidad_por_planeta(generador_planeta_mineral: Generator[PlanetaMineral, None, None],
                               generador_planetas: Generator[Planeta, None, None], 
                               id_mineral: int) -> Generator[Tuple[str, int, float], None, None]:

    gen_pm1, _ = tee(generador_planeta_mineral)
    minerales_filtrados = list(filter(lambda pm: pm.id_mineral == id_mineral, gen_pm1))

    for planeta in generador_planetas:

        coincide = filter(lambda pm: pm.id_planeta == planeta.id_planeta, minerales_filtrados)
        cantidades = map(lambda pm: pm.cantidad_disponible, coincide)
        cantidad = next(cantidades, 0.0)
        yield (planeta.nombre, planeta.id_planeta, cantidad)
# ---------------------------------
# Misiones por tipo planeta (2 generadores) 
def misiones_por_tipo_planeta(generador_misiones: Generator[Mision, None, None],
                              generador_planetas: Generator[Planeta, None, None], 
                              tipo: str) -> Generator[Mision, None, None]:
    
    planetas_filtrados = filter(lambda planeta: planeta.tipo == tipo, generador_planetas)
    id_valido = list(map(lambda x: x.id_planeta,planetas_filtrados))
    for y in generador_misiones:
        if y.lograda is not None and y.id_planeta in id_valido:
            yield y
# ---------------------------------
# Naves pueden llevar (2 generadores)       
def naves_pueden_llevar(generador_naves: Generator[Nave, None, None], 
                        generador_planeta_mineral: Generator[PlanetaMineral, None, None], 
                        id_planeta: int) -> Generator[tuple[str, int, float], None, None]:
    
    generador_f_planeta_mineral = list(filter(lambda pm: pm.id_planeta == id_planeta,
                                generador_planeta_mineral))
    if not generador_f_planeta_mineral:
        yield
    naves_l = tuple(generador_naves)

    for planeta in generador_f_planeta_mineral:
        for nav in naves_l:
            if planeta.cantidad_disponible > 0:
                porcentaje_n = min(100, (nav.capacidad_minerales /
                                        planeta.cantidad_disponible)*100)
            else:
                porcentaje_n = 0.0
            yield (nav.patente, planeta.id_mineral, porcentaje_n)

# ------------------------------------------------------------------------------