# -----------------------------------------------------------------------------
# Imports y modularización
from abc import ABC, abstractmethod
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Clase Personaje (Padre 1: nombre y tipo)
# -----------------------------------------------------------------------------
class Personaje(ABC):
    def __init__(self, nombre: str, tipo: str) -> None: 
        self._nombre = nombre
        self._tipo = tipo
        
    # -------------------------------------------------------------------------
    @abstractmethod
    def descripcion(self) -> str:
        pass

    # -------------------------------------------------------------------------
    def __str__(self):
        return f"{self._nombre} | {self._tipo}"

# -----------------------------------------------------------------------------
class Interrogable(ABC):
    def __init__(self):
        self._preguntas_respondidas: set = set()
        self._max_respuestas: dict = {}

    # -------------------------------------------------------------------------
    @abstractmethod
    def puede_responder(self, tipo: str) -> bool:
        pass

    # -------------------------------------------------------------------------
    @abstractmethod
    def responder(self, pregunta: str) -> str:
        pass

# -----------------------------------------------------------------------------
# Clase Sospechoso
# -----------------------------------------------------------------------------
class Sospechoso(Personaje, Interrogable):
    def __init__(self, nombre: str, tipo: str):
        Personaje.__init__(self, nombre, tipo)
        Interrogable.__init__(self)
        self._ubicacion = None
        self._pistas: list = []

    # -------------------------------------------------------------------------
    def mover(self, habitacion):
        self._ubicacion = habitacion
        print(f"{self._nombre} se ha movido a {habitacion}")

    # -------------------------------------------------------------------------
    def max_resp(self, tipo_hab: str) -> int:
        return self._max_respuestas.get(tipo_hab, 0)

    # -------------------------------------------------------------------------
    def puede_responder(self, tipo: str) -> bool:
        return len(self._preguntas_respondidas) < self.max_resp(tipo)

    # -------------------------------------------------------------------------
    def puede_responder_sobre(self, elemento: str) -> bool:
        """
        Verificar si el sospechoso tiene info sobre
        ese elemento Y no la ha respondido antes.
        """
        return (elemento in self._pistas and
                elemento not in self._preguntas_respondidas)
    
    # -------------------------------------------------------------------------
    def responder(self, elemento: str) -> str | None:
        """
        Si puede responder, registra la pregunta y
        retorna el elemento descartado. Si no, retorna None.
        """
        if self.puede_responder_sobre(elemento):
            self._preguntas_respondidas.add(elemento)
            return elemento
        return None

    def descripcion(self) -> str:
        return f"Sospechoso {self._nombre} ubicado en {self._ubicacion}"

    # -------------------------------------------------------------------------
    def guardar(self): # no fue usada
        guardado_pistas = "-"
        if self. _pistas:
            guardado_pistas = ";".join(self._pistas)
        
        return f"{self._nombre},{self._tipo},{guardado_pistas}"

# -----------------------------------------------------------------------------
# Clase Estudiante
# -----------------------------------------------------------------------------
class Estudiante(Sospechoso):
    def __init__(self, nombre: str):
        super().__init__(nombre, "Estudiante")
        self._max_respuestas = {
            "oficina": 1,
            "sala": 2,
            "patio": 3}

    # -------------------------------------------------------------------------
    def max_respuestas(self, tipo_habitacion: str) -> int:
        return self.max_respuestas.get(tipo_habitacion, 0)

    # -------------------------------------------------------------------------
    def descripcion(self) -> str:
        return f"Estudiante {self._nombre}"

# -----------------------------------------------------------------------------
# Clase Crackyudante
# -----------------------------------------------------------------------------
class Ayudante(Sospechoso):
    def __init__(self, nombre: str):
        super().__init__(nombre, "Ayudante")
        self._max_respuestas = {
            "oficina": 2,
            "sala": 3,
            "patio": 1}

    # -------------------------------------------------------------------------
    def max_respuestas(self, tipo_habitacion: str) -> int:
        return self.max_respuestas.get(tipo_habitacion, 0)

    # -------------------------------------------------------------------------
    def descripcion(self) -> str:
        return f"Ayudante {self._nombre}"

# -----------------------------------------------------------------------------
# Clase Profesor
# -----------------------------------------------------------------------------
class Profesor(Sospechoso):
    def __init__(self, nombre: str):
        super().__init__(nombre, "Profesor")
        self._max_respuestas = {
            "oficina": 3,
            "sala": 2,
            "patio": 1}

    # -------------------------------------------------------------------------
    def max_respuestas(self, tipo_habitacion: str) -> int:
        return self.max_respuestas.get(tipo_habitacion, 0)

    # -------------------------------------------------------------------------
    def descripcion(self) -> str:
        return f"Profesor {self._nombre}"


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
