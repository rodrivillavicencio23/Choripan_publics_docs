# ---------------------------------------------------------
# ---- Imports y modularización ----
from random import random, randint


# ---------------------------------------------------------
# Clase base: Carta
class Carta:
    def __init__(self, nombre: str, vida_maxima: int, vida: int,
                 tipo: str, multidefensa: float,
                 precio: int, prob_especial: float):
        self.nombre = nombre
        self.vida_maxima = vida_maxima
        self.tipo = tipo
        self.multidefensa = multidefensa
        self.precio = precio
        self.prob_especial = prob_especial
        self._vida = 0             
        self.vida = vida            
    # ------------------------------
    # Propiedad de vida
    @property
    def vida(self) -> int:
        """Devuelve la vida actual (entre 0 y vida_maxima)."""
        return self._vida

    @vida.setter
    def vida(self, valor: int):
        """Asigna vida, asegurando que quede en rango válido (>= 0 y <= vida_maxima)."""
        if not isinstance(valor, int):
            raise TypeError("La vida debe ser un número entero")
        if valor < 0:
            self._vida = 0
        elif valor > self.vida_maxima:
            self._vida = self.vida_maxima
        else:
            self._vida = valor

    def recibir_daño(self, daño: int) -> str:
        """Recibe daño desde un objetivo (IA u otra carta)."""
        if daño <= 0:
            return f"{self.nombre} no recibió daño."
        daño_real = int(round(daño * self.multidefensa))
        self.vida -= daño_real
        return f"{self.nombre} recibió {daño_real} de daño. Vida: {self.vida}/{self.vida_maxima}"

    def usar_habilidad_especial(self, *args, **kwargs):
        """Método abstracto para usar habilidad especial (sobrescribir en subclases)"""
        return f"{self.nombre} no tiene habilidad especial pipipi :("

    def __str__(self):
        """Muestra los stats de la carta."""
        return (f"Carta {self.nombre} ({self.tipo}) - "
                f"Vida: {self.vida}/{self.vida_maxima}, "
                f"Precio: {self.precio}")


# ---------------------------------------------------------
# SUBCLASE: Tropa
class CartaTropa(Carta):
    def __init__(self, nombre, vida_maxima, vida,
                 multidefensa, precio, prob_especial,
                 ataque: int, multiataque: float):
        super().__init__(nombre, vida_maxima, vida,
                         "tropa", multidefensa, precio, prob_especial)
        self.ataque = ataque
        self.multiataque = multiataque

    def atacar(self, objetivo):
        """Ataca a un objetivo (IA u otra carta)."""
        daño = int(round(self.ataque * self.multiataque))
        objetivo.vida -= daño
        return f"{self.nombre} atacó causando {daño}. Vida objetivo: {objetivo.vida}"


# ---- TROPAS ESPECIALES ----
class Duende(CartaTropa):
    def usar_habilidad_especial(self, jugador):
        oro_ganado = int(round(self.ataque * self.multiataque))
        jugador.oro += oro_ganado
        return f"{self.nombre} generó {oro_ganado} de oro."


class Peppa(CartaTropa):
    cure_peppa = 0.2

    def atacar(self, objetivo):
        mensaje = super().atacar(objetivo)
        cura = int(round(self.vida_maxima * self.cure_peppa))
        self.vida += cura
        return f"{mensaje} Además, {self.nombre} se curó {cura} HP."


class Montapatos(CartaTropa):
    iniciar_partida = True  # TODO: definir lógica


class Antimuros(CartaTropa):
    def atacar(self, objetivo, mazo):
        mensaje = super().atacar(objetivo)
        if self in mazo:
            mazo.remove(self)
        return f"{mensaje} {self.nombre} se sacrificó y fue eliminado del mazo."


class Caballero(CartaTropa):
    def_cab = 0.1

    def usar_habilidad_especial(self, jugador):
        for carta in jugador.cartas:
            carta.multidefensa += self.def_cab
        return f"{self.nombre} aumentó la defensa de todas las cartas en {self.def_cab}."


class MaldecidorDuende(CartaTropa):
    def usar_habilidad_especial(self, jugador, objetivo):
        jugador.cartas.append(Duende("Duende", 10, 10, 1.0, 3, 0.1, 5, 1.0))
        daño = objetivo.ataque // 2
        objetivo.vida -= daño
        return f"{self.nombre} invocó un Duende y maldijo al rival ({daño} de daño)."


class SkeletonSquad(CartaTropa):
    prob_larry_god = 0.1
    prob_larry_mid = 0.1

    def atacar(self, objetivo):
        daño = int(round(self.ataque * self.multiataque))
        if random() < self.prob_larry_god:
            daño *= 5
        objetivo.vida -= daño
        return f"{self.nombre} atacó causando {daño}. Vida objetivo: {objetivo.vida}"

    def recibir_daño(self, daño):
        if random() < self.prob_larry_mid:
            self.vida = 0
            return f"{self.nombre} murió instantáneamente."
        return super().recibir_daño(daño)


class Barbaros(CartaTropa):
    prob_barb = 0.1
    power_up_barb = 0.1

    def usar_habilidad_especial(self, objetivo):
        mensaje = super().atacar(objetivo)
        if self.vida > 0 and random() < self.prob_barb:
            plus = int(self.ataque * self.power_up_barb)
            self.ataque += plus
            return f"{mensaje} {self.nombre} ganó {plus} de ataque permanente."
        return mensaje


class EspirituFuego(CartaTropa):
    prob_fire = 0.1

    def recibir_daño(self, daño):
        if random() < self.prob_fire:
            self.vida = 0
            return f"{self.nombre} se autodestruyó."
        return super().recibir_daño(daño)


class Globo(CartaTropa):
    prob_globo = 0.2
    daño_bomba = 100

    def usar_habilidad_especial(self, objetivo):
        if random() < self.prob_globo:
            objetivo.vida -= self.daño_bomba
            return f"{self.nombre} lanzó una bomba causando {self.daño_bomba} de daño."
        return f"{self.nombre} no activó su bomba."


# ---------------------------------------------------------
# SUBCLASE: Estructura
class CartaEstructura(Carta):
    def __init__(self, nombre, vida_maxima, vida,
                 multidefensa, precio, prob_especial=0.0):
        super().__init__(nombre, vida_maxima, vida,
                         "estructura", multidefensa, precio, prob_especial)

    def atacar(self, objetivo):
        return f"{self.nombre} es una estructura y no puede atacar."


# ---- ESTRUCTURAS ----
class Canon(CartaEstructura):
    canon_ability = 0.1
    canon_decrease = 0.1

    def usar_habilidad_especial(self, objetivo):
        objetivo.multidefensa *= (1 - self.canon_ability)
        objetivo.multidefensa += self.canon_decrease
        return f"{self.nombre} redujo la defensa del rival."


class TorreDie(CartaEstructura):
    die_prob = 0.2

    def usar_habilidad_especial(self, objetivo):
        if random() < self.die_prob:
            return f"{self.nombre} bloqueó el ataque de {objetivo.nombre}."
        return f"{self.nombre} no logró bloquear."


class RecolectorAgua(CartaEstructura):
    def usar_habilidad_especial(self, jugador):
        if jugador.mazo:
            carta = jugador.mazo[randint(0, len(jugador.mazo) - 1)]
            jugador.cartas.append(carta)
            return f"{self.nombre} duplicó la carta {carta.nombre}."


class Horno(CartaEstructura):
    def usar_habilidad_especial(self, jugador):
        if self.vida == 0:
            carta = EspirituFuego("Espíritu", 5, 5, 1.0, 2, 0.1, 3, 1.0)
            jugador.cartas.append(carta)
            return f"{self.nombre} generó un {carta.nombre}."


class TorreBomba(CartaEstructura):
    daño_bomba = 100

    def usar_habilidad_especial(self, objetivo):
        if self.vida == 0:
            objetivo.vida -= self.daño_bomba
            return f"{self.nombre} explotó causando {self.daño_bomba} de daño."


class CuartelDuendes(CartaEstructura):
    def usar_habilidad_especial(self, jugador):
        jugador.cartas.append(Duende("Duende", 10, 10, 1.0, 3, 0.1, 5, 1.0))
        jugador.cartas.append(Duende("Duende", 10, 10, 1.0, 3, 0.1, 5, 1.0))
        return f"{self.nombre} generó 2 duendes."


# ---------------------------------------------------------
# Carta Mixta
class CartaMixta(CartaTropa, CartaEstructura):
    def __init__(self, tropa: CartaTropa, estructura: CartaEstructura):
        super().__init__(tropa.nombre + "-" + estructura.nombre,
                         tropa.vida_maxima + estructura.vida_maxima,
                         tropa.vida + estructura.vida,
                         (tropa.multidefensa + estructura.multidefensa) / 2,
                         tropa.precio + estructura.precio,
                         (tropa.prob_especial + estructura.prob_especial) / 2,
                         tropa.ataque,
                         tropa.multiataque)
        self.tropa = tropa
        self.estructura = estructura
