# =============================================================================
# Imports y Modularización
from backend.nodo_ligado import NodoLigado
from typing import Generator
from functools import reduce
from backend.helpers import minutos_totales, formato_hh_mm, printear_lista
from utils import (HabitatObjeto, Juguete, JugueteHabitat, 
                   JugueteObjeto, JugueteRecurso, 
                   ObjetoRecurso, PeriodoDia, RecursoRecurso)
# =============================================================================

# =============================================================================
# CARGAS
# =============================================================================
def cargar_juguete(path: str) : # -> Generator[Juguete]

    with open(path, "r", encoding="UTF-8") as archivo:
        try: 
            for linea in archivo:
                n_linea = linea.strip()
                if not n_linea:
                    continue
                m_linea = n_linea.split(",")
                tupla_procesada = tuple([int(x) for x in m_linea[2].split(";")])
                juguete = Juguete(
                                int(m_linea[0]), 
                                m_linea[1],
                                tupla_procesada,
                                m_linea[3])
                yield juguete
        except (TypeError, ValueError):
            return f"Tipo de archivo NO VÁLIDO [ERROR]"
# =============================================================================
def cargar_juguete_habitat(path: str): # -> Generator[JugueteHabitat]
    # id_juguete , id_habitat , tiempo_espera , ids_periodo_dia
    with open(path, "r", encoding="UTF-8") as archivo:
        for linea in archivo:
            n_linea = linea.strip()
            if not n_linea:
                continue
            m_linea = n_linea.split(",")
            ids_periodo_dia = tuple(int(x) for x in m_linea[3].split(";"))

            juguete_habitat = JugueteHabitat(
                            int(m_linea[0]),
                            int(m_linea[1]),
                            m_linea[2],
                            ids_periodo_dia
                            )
            yield juguete_habitat
# =============================================================================
def cargar_habitat_objeto(path: str): # -> Generator[HabitatObjeto]
    with open(path, "r", encoding="UTF-8") as archivo:
        for linea in archivo:
            n_linea = linea.strip()
            if not n_linea:
                continue
            m_linea = n_linea.split(",")
            tuplas_procesadas = tuple((tuple(int(x) for x in tup.split(":") if x != ""))
                                      for tup in m_linea[1].split(";") if tup != "")        
            habitat_objeto = HabitatObjeto(
                            int(m_linea[0]), # id_habitat int
                            tuplas_procesadas)        
            yield habitat_objeto
# =============================================================================
def cargar_objeto_recurso(path: str): # -> Generator[ObjetoRecurso]
    with open(path, "r", encoding="UTF-8") as archivo:
        for linea in archivo:
            n_linea = linea.strip()
            if not n_linea:
                continue
            m_linea = n_linea.split(",")

            tuplas_procesadas = tuple((tuple(int(x) for x in tup.split(":")))
                                      for tup in m_linea[1].split(";"))

            yield ObjetoRecurso(int(m_linea[0]),
                                tuplas_procesadas)
# =============================================================================
def cargar_recurso_recurso(path: str): # -> Generator[RecursoRecurso]
    with open(path, "r", encoding="UTF-8") as archivo:
        for linea in archivo:
            n_linea = linea.strip()
            if not n_linea:
                continue
            m_linea = n_linea.split(",")
            tuplas_procesadas = tuple((tuple(int(x) for x in tup.split(":")))
                                      for tup in m_linea[1].split(";"))
            
            yield RecursoRecurso(int(m_linea[0]),
                                tuplas_procesadas,
                                int(m_linea[2]))
# =============================================================================
def cargar_juguete_recurso(path: str): # -> Generator[JugueteRecurso]
    # id_juguete, id_recurso, tiempo_espera, cantidad 
    with open(path, "r", encoding="UTF-8") as archivo:
        for linea in archivo:
            n_linea = linea.strip()
            if not n_linea:
                continue
            m_linea = n_linea.split(",")

            juguete_recurso = JugueteRecurso(
                            int(m_linea[0]), 
                            int(m_linea[1]),
                            m_linea[2],
                            int(m_linea[3]))
            yield juguete_recurso
# =============================================================================
def cargar_juguete_objeto(path: str): # -> Generator[JugueteObjeto]
    with open(path, "r", encoding="UTF-8") as archivo:
        for linea in archivo:
            n_linea = linea.strip().split(",")
            juguete_objeto = JugueteObjeto(
                            int(n_linea[0]), 
                            int(n_linea[1]))
            yield juguete_objeto
# =============================================================================
def cargar_periodo_dia(path: str): # > Generator[PeriodoDia]
    with open(path, "r", encoding="UTF-8") as archivo:
        for linea in archivo:
            n_linea = linea.strip().split(",")
            periodo_dia = PeriodoDia(
                            int(n_linea[0]), 
                            n_linea[1],
                            n_linea[2])
            yield periodo_dia

# =============================================================================
# CONSULTAS (85% aprox (??))
# =============================================================================
#COMPLETO
def ahora_es(generador_perio_dia: Generator, minutos: int) -> tuple:

    periodos = list(generador_perio_dia)
    duracion_ciclo = reduce(lambda acumulado, p: acumulado + minutos_totales(p.duracion), periodos, 0)
    dia_actual = minutos // duracion_ciclo
    minuto_actual_en_ciclo = minutos % duracion_ciclo
    minutos_recorridos = 0
    for periodo in periodos:
        if minuto_actual_en_ciclo < (minutos_recorridos + minutos_totales(periodo.duracion)):
            tiempo_restante = (minutos_recorridos + minutos_totales(periodo.duracion)) - minuto_actual_en_ciclo
            print(tiempo_restante)    
            return (dia_actual, formato_hh_mm(minuto_actual_en_ciclo), 
                    periodo.nombre, formato_hh_mm(minutos_recorridos),
                    formato_hh_mm(minutos_recorridos + minutos_totales(periodo.duracion)))
        minutos_recorridos += minutos_totales(periodo.duracion)
    return 

# INCOMPLETO
def recursos_a_partir_de_recurso(generador_recurso_recurso: Generator,
                                 id_recurso: int) -> Generator:
    
    todos = list(generador_recurso_recurso)

    def calcular_contribucion(id_base):
        pendientes = [(id_base, frozenset(), 1)]
        resultados = {}
        while pendientes:
            actual, afins_acum, cant_acum = pendientes.pop()
            for rr in todos:
                cant_de_actual = next(
                    (sub[1] for sub in rr.recursos if sub[0] == actual), None
                )
                if cant_de_actual is None:
                    continue

                nuevas_afins = afins_acum | {rr.id_afinidad}
                nueva_cant = cant_acum * cant_de_actual
                if rr.id_recurso not in resultados:
                    resultados[rr.id_recurso] = (nuevas_afins, nueva_cant)
                else:
                    afins_prev, cant_prev = resultados[rr.id_recurso]
                    resultados[rr.id_recurso] = (
                        afins_prev | nuevas_afins,
                        cant_prev + nueva_cant
                    )
                pendientes.append((rr.id_recurso, nuevas_afins, nueva_cant))

        print(resultados)
        return resultados

    contribuciones = calcular_contribucion(id_recurso)

    resultados_ordenados = sorted(((id_res, tuple(sorted(afins)), cant)
            for id_res, (afins, cant) in contribuciones.items()),
            key=lambda x: x[0])
    yield from resultados_ordenados
    
# -----------------------------------------------------------------------------
# COMPLETADO
def juguetes_producen(generador_juguete_recurso: Generator, id_recurso: int) : # -> Generator
    juguetes_p = filter(lambda x: x.id_recurso == id_recurso, generador_juguete_recurso)
    juguetes_id = map(lambda x: x.id_juguete, juguetes_p)
    resultado_sort_unico = sorted(set(juguetes_id))

    yield from resultado_sort_unico
# -----------------------------------------------------------------------------
# COMPLETADO
def juguetes_productivos(generador_juguete_recurso: Generator,
                         minimo: float | None = None) : # -> Generator
    if minimo is not None:
        filtrado = filter(lambda x: 
                        (x.cantidad / minutos_totales(x.tiempo_espera)) > minimo, 
                        generador_juguete_recurso)
        yield from map(lambda x: x.id_juguete, filtrado)
    else:
        max_prod = -1.0
        maximos = []

        for x in generador_juguete_recurso:
            prod_actual = x.cantidad / minutos_totales(x.tiempo_espera)
            if prod_actual > max_prod:
                max_prod = prod_actual
                maximos = [x.id_juguete]
            elif prod_actual == max_prod:
                
                maximos.append(x.id_juguete)
        yield from maximos
# -----------------------------------------------------------------------------
# COMPLETADO
def habitats_de_interes(generador_juguete: Generator,
                        generador_juguete_habitat: Generator) -> Generator:
    
   
    list_gen_jug_hab = list(generador_juguete_habitat)
    ides_juguetes_presentes = set(map(lambda x: x.id_juguete, generador_juguete))

    conjunto_jug_habitat = set()
    for elem in list_gen_jug_hab:
        if elem.id_juguete not in ides_juguetes_presentes:
            conjunto_jug_habitat.add(elem.id_habitat)

    yield from sorted(conjunto_jug_habitat)
# -----------------------------------------------------------------------------
# En proceso 
def cadena_creacion(generador_juguete_recurso: Generator, 
                    generador_recurso_recurso: Generator,
                    id_recurso: int) -> dict:
    pass
# -----------------------------------------------------------------------------
# COMPLETADO
def juguetes_a_aparecer(generador_juguete_habitat: Generator, 
                        generador_periodo_dia: Generator,
                        id_habitat: int, momento_dia: int = 0) -> Generator:
    
    lista_periodos = list(generador_periodo_dia)
    duracion_dia = sum(minutos_totales(p.duracion) for p in lista_periodos)
    inicios = []
    acum = 0
    for periodo in lista_periodos:
        inicios.append(acum)
        acum += minutos_totales(periodo.duracion)

    def get_periodo_idx_en_minuto(minuto_en_ciclo):
        for i, periodo in enumerate(lista_periodos):
            fin = inicios[i] + minutos_totales(periodo.duracion)
            if minuto_en_ciclo < fin:
                return i
        return len(lista_periodos) - 1

    def calcular_tiempo_real(ids_periodo_dia, tiempo_espera_minutos):
        momento_llegada = momento_dia + tiempo_espera_minutos
        minuto_en_ciclo = momento_llegada % duracion_dia

        idx = get_periodo_idx_en_minuto(minuto_en_ciclo)

        if lista_periodos[idx].id_periodo_dia in ids_periodo_dia:
            return tiempo_espera_minutos

        minutos_extra = inicios[idx] + minutos_totales(
                                        lista_periodos[idx].duracion) - minuto_en_ciclo
        
        idx_siguiente = (idx + 1) % len(lista_periodos)

        while lista_periodos[idx_siguiente].id_periodo_dia not in ids_periodo_dia:
            minutos_extra += minutos_totales(lista_periodos[idx_siguiente].duracion)
            idx_siguiente = (idx_siguiente + 1) % len(lista_periodos)

        return tiempo_espera_minutos + minutos_extra

    filtrados = (jug_hab for jug_hab in generador_juguete_habitat 
                if jug_hab.id_habitat == id_habitat)
    
    juguetes_validos = []
    for jug_hab in filtrados:
        tiempo_espera = minutos_totales(jug_hab.tiempo_espera)
        tiempo_real = calcular_tiempo_real(jug_hab.ids_periodo_dia, tiempo_espera)
        juguetes_validos.append((jug_hab.id_juguete, tiempo_real))

    yield from sorted(juguetes_validos, key=lambda x: (x[1], x[0]))
# -----------------------------------------------------------------------------
# NO COMENZADO
def juguetes_autosuficientes(generador_juguete: Generator,
                             generador_juguete_objeto: Generator,
                             generador_objeto_recurso: Generator,
                             generador_juguete_recurso: Generator,
                             generador_recurso_recurso: Generator) -> Generator:
    pass
# -----------------------------------------------------------------------------
# NO COMENZADO
def habitat_eventualmente_creables(generador_juguete: Generator,
                                   generador_juguete_recurso: Generator,
                                   generador_recurso_recurso: Generator,
                                   generador_objeto_recurso: Generator,
                                   generador_habitat_objeto: Generator) -> Generator:
    pass

# =============================================================================
# Parte 3: No completada 
# =============================================================================

def avanzar_produccion(generador_juguete_recurso: Generator,
                       generador_juguete_objeto: Generator,
                       JugueteProductor: NodoLigado | None,
                       objetos: set,
                       minutos: int = 1) -> Generator:
    pass


def crear_recursos(generador_juguete_recurso: Generator,
                   generador_juguete_objeto: Generator) -> Generator:
    pass


def agregar_recursos(recurso: NodoLigado | None, nuevos_recursos: tuple) -> object:
    pass


def por_aparecer(generador_juguete: Generator, Habitat: NodoLigado | None, generador_juguete_habitat: Generator,
                 generador_periodo_dia: Generator, momento_dia: int = 0) -> Generator:
    pass


def habitat_creables(generador_juguete: Generator, generador_juguete_recurso: Generator,
                     generador_recurso_recurso: Generator, generador_objeto_recurso: Generator,
                     generador_habitat_objeto: Generator, Recurso: NodoLigado | None) -> Generator:
    pass


def manejo_habitat(gen_juguete: Generator,
                   gen_juguete_habitat: Generator,
                   gen_habitat_objeto: Generator,
                   gen_objeto_recurso: Generator,
                   gen_recurso_recurso: Generator,
                   gen_periodo_dia: Generator,
                   tiempo_inicial: int = 0) -> Generator:
    pass


# Simulación

def simular(generador_juguete: Generator, generador_juguete_habitat: Generator,
            generador_habitat_objeto: Generator, generador_objeto_recurso: Generator,
            generador_recurso_recurso: Generator, generador_juguete_recurso: Generator,
            generador_juguete_objeto: Generator, generador_periodo_dia: Generator) -> Generator:
    pass
