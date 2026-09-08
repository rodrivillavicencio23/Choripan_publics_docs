import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class MiFormulario(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Formulario con Botón Ajustado')

        # Crear el botón
        self.boton = QPushButton('Mi Botón', self)

        # Opción 1: Usar setFixedSize para fijar un tamaño (ancho, alto)
        self.boton.setFixedSize(100, 32) # Establece un tamaño fijo en píxeles

        # Opción 2: Usar setGeometry para fijar posición y tamaño (x, y, ancho, alto)
        # self.boton.setGeometry(50, 50, 100, 32)

        # Opción 3: Usar un diseño (layout) para un ajuste automático
        layout = QVBoxLayout()
        layout.addWidget(self.boton)
        self.setLayout(layout)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MiFormulario()
    sys.exit(app.exec_())
