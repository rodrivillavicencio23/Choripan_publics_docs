import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl, Qt



class MenuInicial(QWidget):
    def __init__(self, jugador, enemigo):
        super().__init__()
        self.jugador = jugador
        self.enemigo = enemigo
        self.init_ui()

    def init_ui(self):
        # Configuración ventana
        self.setWindowTitle("Menú Inicial")
        self.setGeometry(200, 200, 720, 500)
        self.setWindowIcon(QIcon("icono.png"))  # Ícono personalizado

        # Imagen de fondo escalable
        self.fondo = QLabel(self)
        pixmap = QPixmap("fondo.jpg")  # Imagen en la misma ruta
        self.fondo.setPixmap(pixmap)
        self.fondo.setScaledContents(True)
        self.fondo.setGeometry(0, 0, self.width(), self.height())

        # Layout principal
        layout = QVBoxLayout()

        # Información del jugador y enemigo
        info = QLabel(f"""
        <h1>THE LAST COMPANY</h1>
        <h2><b>Comandante:</b> {self.jugador.comandante}</h2>
        <p><b>Compañía actual:</b> {self.jugador.nombre_compañia}</p>
        <p><b>Comandante enemigo:</b> {self.enemigo.comandante}</p>
        <p><b>Compañía enemiga:</b> {self.enemigo.nombre_compañia}</p>
        """)
        info.setStyleSheet("color: white; font-size: 16px;")
        info.setAlignment(Qt.AlignCenter)
        layout.addWidget(info)

        # Botones del menú
        botones = [
            ("Ir al frente", self.ir_frente),
            ("Revisar Compañía", self.revisar_compania),
            ("Revisar Reserva", self.revisar_reserva),
            ("Desplazar tanques", self.desplazar_tanques),
            ("Adquirir Refuerzos", self.refuerzos),
            ("Abandonar combate", self.salir)
        ]

        for texto, accion in botones:
            btn = QPushButton(texto)
            btn.setStyleSheet("background-color: rgb(20,20,20); color: white; font-size: 12px; padding: 6px;")
            btn.clicked.connect(accion)
            layout.addWidget(btn)

        # Aplicar layout
        self.setLayout(layout)

    def resizeEvent(self, event):
        # Ajustar fondo al tamaño de la ventana
        self.fondo.setGeometry(0, 0, self.width(), self.height())
        super().resizeEvent(event)

    # Métodos simulando acciones
    def ir_frente(self):
        print("Rumbo al frente...")

    def explorar(self):
        print("Explorando frente de batalla...")

    def revisar_compania(self):

        self.ventana_compania = VentanaCompania(self.jugador)
        self.ventana_compania.show()




    def revisar_reserva(self):
        print(self.jugador.revisar_reserva())

    def desplazar_tanques(self):
        print("Desplazando tanques...")

    def refuerzos(self):
        print("Adquiriendo refuerzos...")

    def salir(self):
        print(f"Abandonando combate, gracias por su servicio comandante {self.jugador.comandante}")
        sys.exit(0)


# Simulación de clases jugador/enemigo
class Compañia:
    def __init__(self, comandante, nombre_compañia):
        self.comandante = comandante
        self.nombre_compañia = nombre_compañia
    def revisar_compañia(self):
        return "Detalles de la compañía..."
    def revisar_reserva(self):
        return "Detalles de la reserva..."


class MiBoton(QPushButton):
    # Recibe dos argumentos extra, además de los regulares de QPushButton:
    # - Un nombre para identificar el botón.
    # - Una posición para ubicarse en la ventana.
    def __init__(self, nombre: str, pos: tuple, *args, **kwargs) -> None:
        # Llama al constructor de la clase madre.
        super().__init__(*args, **kwargs)

        # Asigna el nombre a la instancia.
        self.nombre = nombre

        # Crea un contador de instancia inicialmente en 0.
        self.contador = 0

        # Fija su propia geometría
        self.resize(self.sizeHint())
        self.move(*pos)

        # La siguiente línea conecta un clic con el método contar.
        # Entenderemos mejor esta línea en el siguiente notebook
        self.clicked.connect(self.ir_menu_inicial)

    # Agregamos comportamiento al botón, aumenta el contador en cada clic.
    def ir_menu_inicial(self) -> None:
        ventana.close()
        ventana_inicial.show()


class MiVentana(QWidget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.init_gui()
        self.show()
        self.setWindowTitle("Ventana con Imagen de Fondo")
        # self.showMaximized()

    def init_gui(self) -> None:
        # Fija la geometría inicial
        self.setGeometry(720, 500, 720, 500)

        # ---- Imagen de fondo ----
        self.fondo = QLabel(self)
        pixmap = QPixmap("bridge.jpg")  # Imagen en la misma ruta
        self.fondo.setPixmap(pixmap)
        self.fondo.setScaledContents(True)  # Permite escalar la imagen

        
        # ---- Cambiar el ícono de la ventana
        self.setWindowIcon(QIcon("mono.png"))  # Imagen en la misma ruta


        # ---- Etiqueta sobre la imagen ----
        self.label2 = QLabel('Ir al combate. . .', self)
        self.label2.setStyleSheet("""
            color: black;
            font-size: 16px;
            background-color: rgba(255, 255, 255, 255);
        """)
        self.label2.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        # ---- Botón ----
        self.boton_1 = MiBoton("Botón 1", (10, 20), "Ir a formulario", self)
        self.boton_1.setStyleSheet("color: black;")

    def resizeEvent(self, event):
        """Este método se llama automáticamente cuando la ventana cambia de tamaño."""
        self.fondo.setGeometry(0, 0, self.width(), self.height())
        super().resizeEvent(event)


if __name__ == "__main__":
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])
    ventana = MiVentana()
    
    jugador = Compañia("Jugador1", "Alpha")
    enemigo = Compañia("Enemigo1", "Beta")

    ventana_inicial = MenuInicial(jugador, enemigo)
    sys.exit(app.exec())