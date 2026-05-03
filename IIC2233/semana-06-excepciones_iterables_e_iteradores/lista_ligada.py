from typing import Any
from abc import ABC, abstractmethod


class Vagon:
    """
    Esta clase representa un nodo de una lista ligada
    """
    
    def __init__(self, carga: Any = None) -> None:
        """
        Inicializa la estructura del nodo
        """
        self.carga = carga
        self.siguiente = None  # Al crear un nodo, 
                               # la referencia al siguiente nodo comienza vacía

    def __repr__(self) -> str:
        return f"Nodo[{self.carga}]"
    

class EstructuraSecuencialNodal(ABC):
    """
    Clase abstracta que representa una estructura secuencial
    en base a Nodos
    """

    # Todas nuestras estructuras secuenciales poseen:
    #   una cabeza y una cola que inicialmente estan vacías
    #   un largo
    #   un nodo inicial al cual referenciar
    @abstractmethod
    def __init__(self) -> None:
        self.cabeza = None
        self.largo = 0

    @abstractmethod
    def agregar(valor: Any) -> None:
        pass

    @abstractmethod
    def obtener(posicion: int) -> Any:
        pass

    @abstractmethod
    def insertar(valor: Any, posicion: int) -> None:
        pass

    def __len__(self) -> int:
        contador = 0
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            nodo_actual = nodo_actual.siguiente
            contador += 1
        self.largo = contador
        return self.largo

# ===================================================================
# Lista ligada
# ===================================================================
class ListaLigada(EstructuraSecuencialNodal):
    """
    Clase que representa una lista ligada
    """

    def __init__(self) -> None:
        """
        Inicializa una lista ligada vacía,
        con una referencia nula a su cabeza y cola
        """
        super().__init__()
        # Como nuestra LL parte vacía, hacemos que la referencia
        # a su cola sea igual que a su cabeza
        self.cola = self.cabeza

    def agregar(self, valor: Any) -> None:
        """
        Agrega un nodo al final de la cola, similar a lista.append
        """
        # Inicializamos el nuevo nodo
        nuevo = Vagon(valor)

        # Si la lista está vacía (no hay cabeza)
        if self.cabeza is None:
            # El nuevo nodo es la cabeza y cola de la lista
            self.cabeza = nuevo
            self.cola = self.cabeza
        else:
            # Agregamos el nuevo nodo como sucesor del nodo cola actual
            self.cola.siguiente = nuevo
            # Actualizamos la referencia al nodo cola
            self.cola = self.cola.siguiente
        self.largo += 1

    def obtener(self, posicion: int) -> Any:
        """
        Busca el valor del nodo que está en la posición indicada,
        partiendo de 0
        """
        # Revisamos que la posición sea válida
        if posicion < 0:
            print(f'---No es posible obtener el valor en dicha posición---')
            return None
        
        # Empezamos en la cabeza (nodo inicial en esta estructura)
        nodo_actual = self.cabeza

        # Recorremos secuencialmente la lista ligada siguiendo los punteros
        # al nodo siguiente
        for _ in range(posicion):
            # Revisamos que no se haya llegado al final de la lista
            if nodo_actual is not None:
                nodo_actual = nodo_actual.siguiente

        # Si buscamos una posición mayor a la longitud de la lista ligada
        if nodo_actual is None:
            return None  # Retorna "nada"
        return nodo_actual.valor

    def insertar(self, valor: Any, posicion: int) -> None:
        """
        Inserta un valor nuevo en una posición arbitraria
        """
        # Revisamos que la posición sea válida
        if posicion < 0:
            print(f'---No es posible insertar el valor en dicha posición---')
            return None
        
        # Inicializamos el nuevo nodo
        nodo_nuevo = Vagon(valor)
        # Empezamos en la cabeza (nodo inicial en esta estructura)
        nodo_actual = self.cabeza

        # Caso particular: insertar en la cabeza
        if posicion == 0:
            # Actualizamos la cabeza
            nodo_nuevo.siguiente = self.cabeza
            self.cabeza = nodo_nuevo
            # Caso más particular. Si la lista estaba vacía,
            # actualizamos la cola
            if nodo_nuevo.siguiente is None:
                self.cola = nodo_nuevo
            # Terminamos de ejecutar la función
            self.largo += 1
            return

        # Buscamos el nodo predecesor
        for _ in range(posicion - 1):
            if nodo_actual is not None:
                nodo_actual = nodo_actual.siguiente

        # Si encontramos el predecesor, actualizamos las referencias
        if nodo_actual is not None:
            # Si no lo hacemos en este orden perdemos la referencia
            # al resto de la lista ligada
            nodo_nuevo.siguiente = nodo_actual.siguiente
            nodo_actual.siguiente = nodo_nuevo
            # Caso particular: si es que insertamos en la última posición
            if nodo_nuevo.siguiente is None:
                self.cola = nodo_nuevo
            self.largo += 1
        else:
            print(f'---No es posible insertar el valor en dicha posición---')
            return None

    def __repr__(self) -> str:
        """
        Forma una representación de la lista
        """
        string = ""
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            string = f"{string}{nodo_actual.carga} → "
            nodo_actual = nodo_actual.siguiente
        return string
    

ll = ListaLigada()
print(ll)
ll.agregar(2)
print(ll)
ll.agregar(3)
print(ll)
ll.agregar("2T Coal")
print(ll)
ll.agregar(7)
print(ll)
ll.agregar("50 Golden Ingots")
print(ll)
print(f'Largo de Lista Ligada: {len(ll)}')