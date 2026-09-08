# -----------------------------------------------------
# Imports y Modularización
from typing import Generator, Tuple
from math import pi
from collections import defaultdict

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


# ----------------------------------
# ----- Consultas 3 generadores -----
# ----------------------------------

# ---------------------------------
# Planetas por estadísticas (3 generadores)
def planetas_por_estadisticas(generador_mineral: Generator[Mineral, None, None], 
                              generador_planeta_mineral: Generator[PlanetaMineral, None, None], 
                              generador_planeta: Generator[Planeta, None, None], 
                              moles_elemento_min: int, 
                              concentracion_molar_min: int, 
                              densidad_min: int) -> Generator[Planeta, None, None]:
    pass
#-------------------------------------------------------------------
# Ganancias potenciales por planeta (3 generadores)
def ganancias_potenciales_por_planeta(generador_minerales: 
                                      Generator[Mineral, None, None], 
                                      generador_planeta_mineral: 
                                      Generator[PlanetaMineral, None, None], 
                                      generador_planetas: 
                                      Generator[Planeta, None, None], 
                                      precios: dict) -> dict:
    
    minerales = list(generador_minerales)
    planetas_mineral = list(generador_planeta_mineral)
    planetas = list(generador_planetas)

    planetas_unicos = list({pm.id_planeta for pm in planetas_mineral})


    def valor_planeta(id_planeta):
        minerales_planeta = list(filter(lambda pm: pm.id_planeta == id_planeta, 
                                        planetas_mineral))

        valores = map(lambda pm: (next(
                    (m for m in minerales if m.id_mineral == 
                    pm.id_mineral and m.nombre in precios),
                    None), pm), minerales_planeta)


        total = sum(map(lambda par: (par[1].cantidad_disponible * par[1].pureza 
                                    * precios[par[0].nombre]
                                    ) if par[0] is not None else 0,valores))
        return total
    resultado = dict(map(lambda p: (p.id_planeta, valor_planeta(p.id_planeta)),
            planetas))

    return resultado

#-------------------------------------------------------------------
# Planetas visitados por nave (3 generadores)
def planetas_visitados_por_nave(
            generador_planetas: Generator[Planeta, None, None], 
            generador_misiones: Generator[Mision, None, None], 
            generador_tripulaciones: 
            Generator[Tripulacion, None, None]
            ) -> Generator[Tuple[str, str|None, int|None], None, None]:
    
    planetas = tuple(generador_planetas)
    misiones = tuple(generador_misiones)
    tripulaciones = tuple(generador_tripulaciones)

    equipo_a_patente = {t.id_equipo: t.patente_nave for t in tripulaciones}
    id_a_nombre_planeta = {p.id_planeta: p.nombre for p in planetas}
    
    patentes_unicas = list({t.patente_nave for t in tripulaciones})   
    nave_a_planetas = defaultdict(set)


    for mision in misiones:
        if mision.lograda is not None:
            patente = equipo_a_patente.get(mision.id_equipo)
            if patente:
                nave_a_planetas[patente].add((id_a_nombre_planeta[mision.id_planeta], 
                                              mision.id_planeta))

    patentes_unicas = set(equipo_a_patente.values())

    for patente in patentes_unicas:
        if nave_a_planetas[patente]:
            for nombre, id_planeta in nave_a_planetas[patente]:
                yield (patente, nombre, id_planeta)
        else:
            yield (patente, None, None)
#-------------------------------------------------------------------
# Mineral por nave (3 generadores)
def mineral_por_nave(generador_tripulaciones: Generator[Tripulacion, None, None], 
                     generador_misiones: Generator[Mision, None, None], 
                     generador_misiones_mineral: 
                     Generator[MisionMineral, None, None]) -> Generator[Tuple[str, float], 
                                                                        None, None]:
    
    misiones_cumplidas = filter(lambda m: m.lograda == True, generador_misiones)
    patente_de_equipo = {}
    for tripu in generador_tripulaciones:
        if tripu.id_equipo not in patente_de_equipo:
            patente_de_equipo[tripu.id_equipo] = tripu.patente_nave
        
    equipo_mision = {}
    for mision in misiones_cumplidas:
        if mision.id_mision not in equipo_mision:
            equipo_mision[mision.id_mision] = mision.id_equipo

    mision_cmineral = {}
    for mision_mineral in generador_misiones_mineral:
        if mision_mineral.id_mision  not in equipo_mision:
            continue
        mision_cmineral[mision_mineral.id_mision] = (mision_cmineral.get(mision_mineral,
                            0.0) + mision_mineral.cantidad)
        
    cantidad_por_patente = {}
    for id_mision, cantidad in mision_cmineral.items():

        equipo = equipo_mision.get(id_mision)
        if equipo == None:
            continue
        patente = patente_de_equipo.get(equipo)
        if patente == None:
            continue
        cantidad_por_patente[patente] = cantidad_por_patente.get(patente, 0.0) + cantidad
    patente_equipo_seteado = set(patente_de_equipo.values())
    for patente in patente_equipo_seteado:
        yield (patente, cantidad_por_patente.get(patente, 0.0))



#-------------------------------------------------------------------
# Porcentaje extracción (3 generadores)
def porcentaje_extraccion(generador_tripulacion: Generator[Tripulacion, None, None], 
                          generador_mision_mineral: Generator[MisionMineral, None, None], 
                          generador_planeta_mineral: 
                          Generator[PlanetaMineral, None, None], 
                          mision : Mision) -> Tuple[float, float]:
    if not mision.lograda:
        return (0.0, 0.0)

    tripulaciones = list(generador_tripulacion)
    misiones_mineral = list(generador_mision_mineral)
    planetas_mineral = list(generador_planeta_mineral)

    minerales_mision = list(filter(lambda mm: mm.id_mision == mision.id_mision, misiones_mineral))
    minerales_planeta = list(filter(lambda pm: pm.id_planeta == mision.id_planeta, planetas_mineral))

    total_extraido = sum(map(lambda mm: mm.cantidad, minerales_mision))
    total_planeta = sum(map(lambda pm: pm.cantidad_disponible * pm.pureza, minerales_planeta))

    if total_planeta == 0:
        return (0.0, 0.0)

    porcentaje_extraido = (total_extraido / total_planeta) * 100

    tripulantes_en_mision = list(filter(lambda t: t.id_equipo == mision.id_equipo, tripulaciones))
    n_tripulantes = len(tripulantes_en_mision) if tripulantes_en_mision else 1

    porcentaje_por_tripulante = porcentaje_extraido / n_tripulantes

    return (porcentaje_extraido, porcentaje_por_tripulante)
#-------------------------------------------------------------------
# Resultado mision (4 generadores :D)
def resultado_mision(mision: Mision, 
                    generador_naves: Generator[Nave, None, None], 
                    generador_planeta_mineral: Generator[PlanetaMineral, None, None],
                    generador_tripulaciones: Generator[Tripulacion, None, None], 
                    generador_mision_mineral: Generator[MisionMineral, None, None]) -> Mision:
    
    tripulacion_mision = filter(lambda t: t.id_equipo == mision.id_equipo, 
                                generador_tripulaciones)
    patente = next(map(lambda t: t.patente_nave, tripulacion_mision), None)
    if not patente:
        return mision._replace(lograda=False)

    nave = next(filter(lambda n: n.patente == patente, generador_naves), None)
    if not nave:
        return mision._replace(lograda=False)

    minerales_mision = list(filter(lambda mm: mm.id_mision == mision.id_mision, 
                                   generador_mision_mineral))
    minerales_planeta = list(filter(lambda pm: pm.id_planeta == mision.id_planeta, 
                                    generador_planeta_mineral))

    mineral_gatochico = next(filter(lambda mm: mm.id_mineral == 1, minerales_mision), None)
    if mineral_gatochico and mineral_gatochico.cantidad <= nave.capacidad_minerales:
        return mision._replace(lograda=True)

    def mineral_disponible(mm):
        pm = next(filter(lambda p: p.id_mineral == mm.id_mineral, minerales_planeta), None)
        if pm is None:
            return False
        disponible_puro = pm.cantidad_disponible * pm.pureza
        return mm.cantidad <= disponible_puro

    todos_disponibles = all(map(mineral_disponible, minerales_mision))
    capacidad_total = sum(map(lambda mm: mm.cantidad, minerales_mision))
    lograda = todos_disponibles and (capacidad_total <= nave.capacidad_minerales)
    return mision._replace(lograda=lograda)