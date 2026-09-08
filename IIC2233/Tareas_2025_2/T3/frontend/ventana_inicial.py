# ------------------------------
# Imports y Modularización
import os
from PyQt5.QtWidgets import (QWidget, QLabel, QVBoxLayout, QSizePolicy,
                            QHBoxLayout, QPushButton, QApplication)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, pyqtSignal
# ------------------------------

# ------------------------------
# Ventana Inicial
# ------------------------------
class VentanaIni(QWidget):
    senal_abrir_menu = pyqtSignal()
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.init_gui()
        self.show()
        self.setWindowTitle("DCCOSMOS: INICIO")

    def init_gui(self) -> None:
        # 🔹 Ventana con tamaño fijo
        self.setFixedSize(720, 480)

        # ---- Imagen de fondo ----
        self.fondo = QLabel(self)
        fondo_path = os.path.join("frontend", "sprites", "death_star.jpg")
        pixmap = QPixmap(fondo_path)
        self.fondo.setPixmap(pixmap)
        self.fondo.setScaledContents(True)
        self.fondo.setGeometry(0, 0, 720, 480)  # ajustado manualmente al tamaño fijo

        # ---- Ícono de la ventana ----
        self.setWindowIcon(QIcon("frontend/sprites/mono.jpg"))

        # ---- Layout principal ----
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(30, 30, 30, 30)
        main_layout.setSpacing(5)

        # ---------- IMAGEN DE TÍTULO ----------
        self.titulo_label = QLabel(self)
        self.titulo_label.setAlignment(Qt.AlignCenter)

        titulo_path = os.path.join("frontend", "sprites", "dcccosmos.png")
        if os.path.exists(titulo_path):
            titulo_pixmap = QPixmap(titulo_path)
            self.titulo_label.setPixmap(titulo_pixmap)
            self.titulo_label.setScaledContents(False)  # sin autoescalado
        else:
            self.titulo_label.setText("TÍTULO DEL PROGRAMA (placeholder)")
            self.titulo_label.setStyleSheet("color: white; font-size: 18px;")

        main_layout.addWidget(self.titulo_label, alignment=Qt.AlignCenter)
        main_layout.addStretch(1)


        # ---------- FILA DE BOTONES ----------
        h_layout = QVBoxLayout()
        info = QLabel(f"""
        <h1>Bienvenido</h1>
        """)

        info.setStyleSheet("color: white; font-size: 16px;")
        info.setAlignment(Qt.AlignCenter)
        h_layout.addWidget(info)
        botones = [
            ("Ir al Menú Principal", self.ir_menu_principal),
            ("Salir del Programa", self.cerrar_programa),
        ]
        h_layout.addStretch(1)
        for texto, accion in botones:
            btn = QPushButton(texto)
            btn.setStyleSheet(
                "background-color: rgba(20,20,20,0.9); color: white; "
                "font-size: 30px; padding: 10px;"
            )
            btn.clicked.connect(accion)
            h_layout.addWidget(btn)

        h_layout.addStretch(1)
        main_layout.addLayout(h_layout)

        # ---- Aplicar layout principal ----
        self.setLayout(main_layout)

    # ---------- Acciones de botones ----------
    def ir_menu_principal(self):
        self.hide()  # Oculta la ventana actual
        self.senal_abrir_menu.emit()  # Emite señal al main

    def cerrar_programa(self):
        QApplication.instance().quit()


if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaIni()
    ventana.show()
    app.exec_()