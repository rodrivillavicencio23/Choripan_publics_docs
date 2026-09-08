import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl, Qt


class CampoFormulario(QHBoxLayout):

    # Heredamos de Layout Horizontal para colocar cada campo.
    def __init__(self, texto: str, *args, **kwargs) -> None:
        # Llama al constructor de la clase madre.
        super().__init__(*args, **kwargs)

        # Crea la etiqueta y cuadro correspondientes.
        label = QLabel(f"{texto}: ")
        
        campo = QLineEdit("")

        # Los coloca dentro del Layout.
        self.addStretch(1)
        self.addWidget(label)
        self.addWidget(campo)
        self.addStretch(1)
        label.setStyleSheet("color: black; background: rgb(255,255,0,200)")

class Formulario(QWidget, ):
    def __init__(self, *args, **kwargs) -> None:
        
        super().__init__(*args, **kwargs)
        # Fija datos de ventana.
        self.setWindowTitle("Formulario")
        self.setStyleSheet("background-color: rgb(255,255,255,255);")
        self.setGeometry(200, 200, 720, 500)

        # ---- Reproductor de música ----
        self.player = QMediaPlayer()
        url = QUrl.fromLocalFile("otro_atardecer.mp3")  # Archivo en la misma carpeta
        self.player.setMedia(QMediaContent(url))
        self.player.setVolume(30)  # Volumen (0-100)
        self.player.play()  # Reproducir al abrir la ventana


        # ---- Ajuste de Fondo ----
        self.fondo = QLabel(self)
        self.fondo.setGeometry(0, 0, 720, 500)  # Ocupa toda la ventana
        pixmap = QPixmap("tillas.jpg")  # Imagen en la misma ruta
        self.fondo.setPixmap(pixmap)
        self.fondo.setScaledContents(True)  # Ajusta la imagen al tamaño del QLabel

        # ---- Cambiar el ícono de la ventana
        self.setWindowIcon(QIcon("puma.png"))  # Imagen en la misma ruta


        self.boton_2 = BotonVolverInicio("Botón 2", (40, 20), "Volver", self)
        # Crea contenedor vertical para colocar los campos.
        contenedor = QVBoxLayout()

        # Coloca cada campo que creamos.
        contenedor.addLayout(CampoFormulario("Nombre"))
        contenedor.addLayout(CampoFormulario("Apellido"))
        contenedor.addLayout(CampoFormulario("Dirección"))
        contenedor.addLayout(CampoFormulario("Correo"))
        contenedor.addLayout(CampoFormulario("Usuario"))
        contenedor.addLayout(CampoFormulario("Contraseña"))
        contenedor.addWidget(BotonSubmit("Botón subir info", (360, 40), "Subir Datos", self))
        # ---- Botón de subir info ----


        # Fijamos el Layout completo.
        self.setLayout(contenedor)


    def resizeEvent(self, event):
        """Este método se llama automáticamente cuando la ventana cambia de tamaño."""
        self.fondo.setGeometry(0, 0, self.width(), self.height())
        super().resizeEvent(event)
    
    

class BotonVolverInicio(QPushButton):

    def __init__(self, nombre: str, pos: tuple, *args, **kwargs) -> None:
        # Llama al constructor de la clase madre.
        super().__init__(*args, **kwargs)
        self.setStyleSheet("color: black;")
        # Asigna el nombre a la instancia.
        self.nombre = nombre

        # Fija su propia geometría
        self.resize(self.sizeHint())
        self.move(*pos)

        self.clicked.connect(self.volver_formulario)

    # Agregamos comportamiento al botón, aumenta el contador en cada clic.
    def volver_formulario(self) -> None:
        ventana_formulario.close()
        # ventana.show()


# -----------------------------------------------
class BotonSubmit(QPushButton):

    def __init__(self, nombre: str, pos: tuple, *args, **kwargs) -> None:
        # Llama al constructor de la clase madre.
        super().__init__(*args, **kwargs)

        # Asigna el nombre a la instancia.
        self.nombre = nombre
        self.setFixedSize(100, 32) # Establece un tamaño fijo en píxeles
        self.setStyleSheet("color: black;")
        self.move(*pos)

        self.clicked.connect(self.subir_info)
        
    # Agregamos comportamiento al botón
    def subir_info(self) -> None:
        print("se subio la info")
        ventana_formulario.close()
        # ventana.close()


if __name__ == "__main__":
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])
    ventana_formulario = Formulario()
    
    sys.exit(app.exec())