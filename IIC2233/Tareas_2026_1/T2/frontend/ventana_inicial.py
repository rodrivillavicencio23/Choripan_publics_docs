# =============================================================================
# Imports y Modularización
import os
import sys
from PyQt6.QtWidgets import (QWidget, QLabel, QVBoxLayout, QSizePolicy,
                            QHBoxLayout, QPushButton, QApplication, QFileDialog)
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt, pyqtSignal
from random import choice
# =============================================================================

# =============================================================================
# Ventana Inicial
# =============================================================================
class VentanaIni(QWidget):
    senal_abrir_indice = pyqtSignal()
    senal_abrir_simulacion = pyqtSignal()
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.init_gui()
        self.show()
        self.setWindowTitle("DCCORNUCOPIA : INICIO")
        self.setStyleSheet("background-color: rgb(86,86,86);")

    def init_gui(self) -> None:
        # ---- VENTANA CON TAMANO FIJO ----
        self.setFixedSize(720, 720)

        # ---- IMAGEN DE FONDO ----
        self.fondo = QLabel(self)
        lista_fondos = ("gato1.png", "gato2.png", "gato3.png")
        gato_fondo = choice(lista_fondos)

        fondo_path = os.path.join("frontend", "images", gato_fondo)
        pixmap = QPixmap(fondo_path)
        self.fondo.setPixmap(pixmap)
        self.fondo.setScaledContents(True)
        self.fondo.setGeometry(0, 0, 720, 720)

        # ---- ICONO DE LA VENTANA ----
        self.setWindowIcon(QIcon("frontend/images/gato1.png"))

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(30, 30, 30, 30)
        main_layout.setSpacing(5)

        # ---- TITULO ----
        self.titulo_label = QLabel(self)
        self.titulo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.titulo_label.setText("DCCornucopia")
        self.titulo_label.setStyleSheet(
            "border: 2px solid rgb(255,255,255);"
            "color: white; font-size: 20px;")

        main_layout.addWidget(self.titulo_label)
        main_layout.addStretch(1)

        # ---- FILA DE BOTONES ----
        h_layout = QVBoxLayout()
        info = QLabel()
        info.setText("Seleccione:")
        info.setStyleSheet(
                "border: 2px solid rgb(255,255,255);"
                "color: white; font-size: 20px;")
        
        info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        h_layout.addWidget(info)
        botones = [
            ("Indice de Juguetes", self.ir_indice_juguetes),
            ("Seleccion de carpetas", self.elegir_carpeta),
            ("Simulación", self.ir_simulacion),
            ("Salir del Programa", self.cerrar_programa),

        ]
        h_layout.addStretch(1)
        for texto, accion in botones:
            btn = QPushButton(texto)
            btn.setStyleSheet(
                "border: 2px solid rgb(255,255,255);"
                "background-color: rgba(20,20,20,0.9); color: white; "
                "font-family: Times New Roman; font-size: 30px; padding: 10px; "
            )
            btn.clicked.connect(accion)
            h_layout.addWidget(btn)
            #h_layout.addStretch(1)

        h_layout.addStretch(1)
        main_layout.addLayout(h_layout)

        # ---- Aplicar layout principal ----
        self.setLayout(main_layout)

    # ---------- Acciones de botones ----------
    def ir_indice_juguetes(self):
        print("Botón INDICE JUGUETE")
        self.hide() 
        self.senal_abrir_indice.emit()

    def ir_simulacion(self):
        print("Botón SIMULACIÓN PRESIONADO")
        self.hide() 
        self.senal_abrir_simulacion.emit()

    # ---------- ELEGIR CARPETA ----------
    def elegir_carpeta(self):
        ruta = QFileDialog.getExistingDirectory(self, "Selecciona carpeta: ")
        if ruta:
            print(f"Carpeta seleccionada: {ruta}")

    def cerrar_programa(self):
        QApplication.instance().quit()

# =============================================================================
# =============================================================================
# =============================================================================