import sys
from PyQt5.QtWidgets import *

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

class Formulario(QWidget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # Fija datos de ventana.
        self.setWindowTitle("Formulario")
        self.setGeometry(200, 200, 720, 500)

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
        contenedor.addWidget(BotonSubmit("Botón subir info", (70, 40), "Subir Datos", self))
        # ---- Botón de subir info ----


        # Fijamos el Layout completo.
        self.setLayout(contenedor)

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
        self.clicked.connect(self.ir_formulario)

    # Agregamos comportamiento al botón, aumenta el contador en cada clic.
    def ir_formulario(self) -> None:
        ventana.close()
        ventana_formulario.show()



class BotonVolverInicio(QPushButton):

    def __init__(self, nombre: str, pos: tuple, *args, **kwargs) -> None:
        # Llama al constructor de la clase madre.
        super().__init__(*args, **kwargs)

        # Asigna el nombre a la instancia.
        self.nombre = nombre

        # Fija su propia geometría
        self.resize(self.sizeHint())
        self.move(*pos)

        self.clicked.connect(self.volver_formulario)

    # Agregamos comportamiento al botón, aumenta el contador en cada clic.
    def volver_formulario(self) -> None:
        ventana_formulario.close()
        ventana.show()


# -----------------------------------------------
class BotonSubmit(QPushButton):

    def __init__(self, nombre: str, pos: tuple, *args, **kwargs) -> None:
        # Llama al constructor de la clase madre.
        super().__init__(*args, **kwargs)

        # Asigna el nombre a la instancia.
        self.nombre = nombre

        # Fija su propia geometría
        self.resize(self.sizeHint())
        self.move(*pos)

        self.clicked.connect(self.subir_info)

    # Agregamos comportamiento al botón, aumenta el contador en cada clic.
    def subir_info(self) -> None:
        print("se subio la info")
        ventana_formulario.close()
        ventana.close()

class MiVentana(QWidget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.init_gui()
        self.show()

    def init_gui(self) -> None:
        # Fija la geometría de la ventana principal
        self.setGeometry(720, 500, 120, 120)
        self.setMaximumHeight(120)
        self.setMaximumWidth(120)

        # Instancia dos botones de nuestra clase, con atributos extra
        # de los que QPushButton está acostumbrado: nombre y posición.

        # ---- Botón ir al formulario ----
        self.boton_1 = MiBoton("Botón 1", (10, 20), "Ir a formulario", self)



if __name__ == "__main__":
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])
    ventana = MiVentana()
    ventana_formulario = Formulario()
    sys.exit(app.exec())
