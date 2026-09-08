# ---------------------------------------------------------
# ---- Imports y modularización ----
from dccartas import Carta, CartaEstructura, CartaTropa, CartaMixta
# ---------------------------------------------------------

class Jugador:
    def __init__(self, nombre: str, oro_inicial: int = 16):
        self.nombre = nombre
        self.oro = oro_inicial
        self.cartas: list[Carta] = []
        self.coleccion: list[Carta] = []
        self.cementerio: list[Carta] = []
        self.peleas = 0
        self.peleas_ganadas = 0

    # ------------------------------
    # Propiedad de oro
    @property
    def oro(self) -> int:
        return self._oro

    @oro.setter
    def oro(self, valor: int):
        if not isinstance(valor, int):
            raise TypeError("El oro debe ser un número entero")
        if valor < 0:
            raise ValueError("No puedes tener oro negativo >:/ !!")
        self._oro = valor

    # ------------------------------
    # Métodos de gestión de cartas
    def agregar_carta(self, carta: Carta) -> str:
        """
        Agrega carta al mazo activo si hay espacio (max de 5)
        """
        if len(self.cartas) >= 5:
            return "No se puede añadir más cartas al mazo (max de 5)"
        self.cartas.append(carta)
        self.coleccion.append(carta)
        return f"Carta {carta.nombre} añadida al mazo."

    def eliminar_carta(self, carta: Carta) -> str:
        """
        Elimina carta del mazo y la manda al cementerio (manchested united temporada 2024)
        """
        if carta in self.cartas:
            self.cartas.remove(carta)
            self.cementerio.append(carta)
            return f"Carta {carta.nombre} enviada al cementerio."
        return f"La carta {carta.nombre} no estaba en el mazo."

    def revivir_carta(self, indice: int) -> str:
        """Revivir carta desde cementerio (si es que existe)"""
        if len(self.cementerio) == 0:
            return "No hay nada que revivir del cementerio bro,\n" \
            "lo único que hay es el amor que sentía por la que me gustaba . . . \n"
        
        if indice < 0 or indice >= len(self.cementerio):
            return "Índice inválido en el cementerio"
        carta = self.cementerio.pop(indice)
        carta.vida = carta.vida_maxima // 2
        self.cartas.append(carta)
        return f"La carta {carta.nombre} fue revivida con {carta.vida} HP."

    def curar_carta(self, indice: int) -> str:
        """
        Curar carta del mazo al máximo de vida
        """
        if indice < 0 or indice >= len(self.cartas):
            return "Índice inválido en el mazo"
        carta = self.cartas[indice]
        carta.vida = carta.vida_maxima
        return f"La carta {carta.nombre} fue curada a {carta.vida_maxima} HP."

    # ------------------------------
    # Daño recibido
    def recibir_daño(self, daño: int) -> str:
        """Distribuye daño entre cartas defensoras"""
        if not self.cartas:
            return "El jugador no tiene cartas en el mazo"

        daño_restante = daño
        for carta in self.cartas:
            if isinstance(carta, (CartaEstructura, CartaMixta)):
                daño_restante = max(0, daño_restante - carta.vida)
                carta.recibir_daño(daño)
                if daño_restante <= 0:
                    break

        return f"El jugador {self.nombre} recibió {daño} de daño"

    # ------------------------------
    # Representación
    def __len__(self):
        return len(self.cartas)

    def __str__(self):
        info = [
            f"Jugador: {self.nombre}",
            f"Oro: {self.oro}G",
            f"Peleas ganadas: {self.peleas_ganadas}/{self.peleas}",
            "Cartas en mazo:"
        ]
        for i, carta in enumerate(self.cartas):
            if isinstance(carta, CartaTropa):
                info.append(f"[{i}] {carta.nombre} (Tropa): {carta.vida}/{carta.vida_maxima} HP, Ataque {carta.ataque}")

            elif isinstance(carta, CartaEstructura):
                info.append(f"[{i}] {carta.nombre} (Estructura): {carta.vida}/{carta.vida_maxima} HP, Defensa x{carta.multidefensa}")

            elif isinstance(carta, CartaMixta):
                info.append(f"[{i}] {carta.nombre} (Mixta): {carta.vida}/{carta.vida_maxima} HP, Ataque {carta.ataque}, Defensa x{carta.multidefensa}")
        return "\n".join(info)
