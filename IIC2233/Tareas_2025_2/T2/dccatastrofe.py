# ---------------------------------------------------------
# dccatastrofe.py
# ---- Imports y modularización ----
import os
from copy import deepcopy
from random import random, randint
from jugador import Jugador
from dccartas import CartaTropa, CartaEstructura, CartaMixta
# ---------------------------------------------------------

# Clase IA (el "amigo" de mi compadrito Ignacio Pizarro, desde la comuna de Peñaflor)
class InteligenciaArtificial:
    def __init__(self, nombre: str, vida: int, ataque: int,
                 multi_defensa: float, multi_ataque: float,
                 prob_especial: float):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.multi_defensa = multi_defensa
        self.multi_ataque = multi_ataque
        self.prob_especial = prob_especial

    def atacar(self) -> int:
        """Devuelve el daño de ataque."""
        daño = int(round(self.ataque * self.multi_ataque))
        return daño

    def recibir_daño(self, daño: int) -> str:
        """Recibe daño externo y actualiza su vida."""
        daño_real = int(round(daño * self.multi_defensa))
        if daño_real >= self.vida:
            self.vida = 0
            return f"La IA {self.nombre} ha muerto."
        self.vida -= daño_real
        return f"Vida de la IA {self.nombre}: {self.vida}"

    def usar_habilidad_especial(self, *args, **kwargs):
        """Método genérico (sobrescribir en subclases)."""
        return f"{self.nombre} no tiene habilidad especial definida."


# ---------------------------------------------------------
# Subclases IA
class CatGpt(InteligenciaArtificial):
    def usar_habilidad_especial(self, jugador: Jugador) -> str:
        """
        Reduce multiplicadores de todas las cartas del jugador
        """
        for carta in jugador.cartas:
            if isinstance(carta, (CartaTropa, CartaMixta)):
                carta.multiataque = 0.65
                carta.multidefensa = 0.65
            elif isinstance(carta, CartaEstructura):
                carta.multidefensa = 0.65
        return f"{self.nombre} redujo los multiplicadores de todas las cartas a 0.65 (q locura)!"


class CowPilot(InteligenciaArtificial):
    def usar_habilidad_especial(self, jugador: Jugador) -> str:
        """
        Reemplazar dos cartas distintas del mazo activo
        por copias idénticas
        """
        if len(jugador.cartas) < 3:
            return f"{self.nombre} no pudo activar su habilidad (se necesitan más o igual que 3 cartas en el mazo)"
        # Elegir tres posiciones distintas
        indices = list(range(len(jugador.cartas)))
        i, j, k = [indices.pop(randint(0, len(indices) - 1)) for _ in range(3)]

        carta_base = jugador.cartas[k]  # carta que se va a duplicar

        # Clonar la carta (copias nuevas para que no sea la misma referencia)
        
        copia1 = deepcopy(carta_base)
        copia2 = deepcopy(carta_base)

        # Reemplazar en las posiciones i y j
        jugador.cartas[i] = copia1
        jugador.cartas[j] = copia2

        return (
            f"{self.nombre} plagió al jugador: "
            f"las cartas en posiciones {i} y {j} fueron reemplazadas "
            f"por copias de {carta_base.nombre}."
        )



class Crok(InteligenciaArtificial):
    def usar_habilidad_especial(self, jugador: Jugador) -> str:
        """
        Provoca que dos cartas se "rebelen" y no ataquen/defiendan por 3 rondas.
        (Pendiente de implementar contador de rondas en Jugador o Engine).
        """
        if len(jugador.cartas) < 2:
            return f"{self.nombre} intentó rebelar cartas, pero no había suficientes."
        # TODO: marcar estado de "rebelde" en las cartas
        return f"{self.nombre} rebeló a dos cartas por 3 rondas"


class DeepSheep(InteligenciaArtificial):
    def usar_habilidad_especial(self, jugador: Jugador) -> str:
        """
        Problema: en el menú de la tarea,
        todas las cartas del jugador mostrarán falsamente la misma vida
        (la de la carta con vida más alta).
        """
        if not jugador.cartas:
            return f"{self.nombre} no encontró cartas para aplicar su efecto."
        vida_max = max(carta.vida for carta in jugador.cartas)
        for carta in jugador.cartas:
            carta.vida = vida_max
        return f"{self.nombre} alteró la visualización de las vidas de las cartas."


class Gemibee(InteligenciaArtificial):
    def usar_habilidad_especial(self, *_):
        """Aumenta ataque y defensa permanentemente en 0.1."""
        self.multi_ataque += 0.1
        self.multi_defensa += 0.1
        return f"{self.nombre} aumentó sus multiplicadores en +0.1."


# ---------------------------------------------------------
# Leer IA sdegún dificultad indicada por el usuario
def leer_ia(dificultad: str) -> InteligenciaArtificial:
    """Carga una IA desde archivo CSV según la dificultad."""

    if dificultad == "facil":
        archivo = "ias_facil.csv"
    elif dificultad == "normal":
        archivo = "ias_normal.csv"
    elif dificultad == "dificil":
        archivo = "ias_dificil.csv"
    else:
        archivo = "ias_facil.csv"

    ruta = os.path.join("data", archivo)

    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo[1:]:
            carta = linea.strip().split(",  ")
            nombre = carta[0]
            vida  = int(carta[1])
            ataque = int(carta[2])
            multi_def = float(carta[3])
            multi_ataq = float(carta[4])
            prob = float(carta[5])
            valores = [nombre, vida, ataque, multi_def, multi_ataq, prob]
            if nombre == "CatGPT":
                return CatGpt(*valores)
            elif nombre == "CowPilot":
                return CowPilot(*valores)
            elif nombre == "Crok":
                return Crok(*valores)
            elif nombre == "DeepSheep":
                return DeepSheep(*valores)
            elif nombre == "Gemibee":
                return Gemibee(*valores)

    raise ValueError(f"No se encontró IA para dificultad dada  - {dificultad} -")
