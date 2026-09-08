# =============================================================================
# Imports y Modularización
import os
from PyQt6.QtWidgets import (QWidget, QLabel, QVBoxLayout,
                             QHBoxLayout, QPushButton,
                             QScrollArea, QGroupBox, 
                             QGridLayout)
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt, pyqtSignal
# =============================================================================

# =============================================================================
# Ventana Principal 
# =============================================================================
class VentanaSimulacion(QWidget):
    senal_volver_inicio = pyqtSignal()

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.init_gui()
        self.setWindowTitle("DCCORNUCOPIA: SIMULACION DCCORNUCOPIA")

    def init_gui(self) -> None:
        self.setFixedSize(920, 720)

        # ---- IMAGEN DE FONDO ----
        self.fondo = QLabel(self)
        fondo_path = os.path.join("frontend", "images", "gato1.png")
        if os.path.exists(fondo_path):
            self.fondo.setPixmap(QPixmap(fondo_path))
        self.fondo.setScaledContents(True)
        self.fondo.setGeometry(0, 0, 920, 720)

        # ---- ICONO DE LA VENTANA ----
        self.setWindowIcon(QIcon("frontend/images/gato2.png"))

        # ---- LAYOUT PRINCIPAL ----
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        # ---- TÍTULO ----
        self.titulo_label = QLabel(self)
        self.titulo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.titulo_label.setText("DCCORNUCOPIA: SIMULACIÓN")
        self.titulo_label.setStyleSheet("color: white; "
                                        "font-size: 24px; font-weight: bold;")
        
        main_layout.addWidget(self.titulo_label)

        # ---------------------------------------------------------------------
        # BOTÓN Volver Inicio
        # ---------------------------------------------------------------------
        bottom_layout = QHBoxLayout()
        btn = QPushButton("Volver Inicio")
        btn.setFixedSize(220, 40)
        btn.setStyleSheet(
            "border: 2px solid white; "
            "background-color: rgba(20,20,20,0.9); color: white; "
            "font-family: 'Times New Roman'; font-size: 18px; padding: 5px;"
        )
        btn.clicked.connect(self.volver_inicio)
        
        bottom_layout.addStretch()
        bottom_layout.addWidget(btn)
        bottom_layout.addStretch() 

        main_layout.addLayout(bottom_layout)
        
        central_layout = QHBoxLayout()

        # ---------------------------------------------------------------------
        # LADO IZQUIERDO
        # ---------------------------------------------------------------------
        scroll_group = QGroupBox("Resultados Consulta: ")
        scroll_group.setStyleSheet(
            "color: white; background-color: rgba(0,0,0,0.5); "
            "font-weight: bold; border: 1px solid white;"
        )
        
        scroll_layout = QVBoxLayout(scroll_group)
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("background-color: transparent; border: none;")
        
        contenedor = QWidget()
        contenedor.setStyleSheet("background-color: transparent;")
        grid_scroll = QGridLayout(contenedor)
        
        columnas = 3
        for i in range(50):
            label = QLabel(f"ERROR: #{i+1}")
            label.setStyleSheet("color: black; background-color: white; "
                                "font-weight: bold; border: 1px solid gray; "
                                "padding: 10px;")
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            
            fila = i // columnas
            columna = i % columnas
            grid_scroll.addWidget(label, fila, columna)
        
        scroll_area.setWidget(contenedor)
        scroll_layout.addWidget(scroll_area)
        
        central_layout.addWidget(scroll_group, stretch=2) 

        # ---------------------------------------------------------------------
        # LADO DERECHO (Día + botones (no implementados) + Resultados Eventos)
        # ---------------------------------------------------------------------
        info_layout = QVBoxLayout()

        self.titulo_info = QLabel("DÍA: ERROR ##")
        self.titulo_info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.titulo_info.setStyleSheet("color: white; font-size: 18px; "
                                       "font-weight: bold; "
                                       "background-color: rgba(0,0,0,0.5); "
                                       "padding: 5px; ")
        info_layout.addWidget(self.titulo_info)

        scroll_group_2 = QGroupBox("Resultados Eventos: ")
        scroll_group_2.setStyleSheet(
            "color: white; background-color: rgba(0,0,0,0.5); "
            "font-weight: bold; border: 1px solid white; "
        )
        
        scroll_layout_2 = QVBoxLayout(scroll_group_2)
        scroll_area_2 = QScrollArea()
        scroll_area_2.setWidgetResizable(True)
        scroll_area_2.setStyleSheet("background-color: transparent; border: none;")
        
        contenedor_2 = QWidget()
        contenedor_2.setStyleSheet("background-color: rgba(255,255,255,0.1);")
        vbox_scroll_2 = QVBoxLayout(contenedor_2)
        
        for i in range(50):
            lbl_evento = QLabel(f"EventError: ERROR #{i}")
            lbl_evento.setStyleSheet("color: white; padding: 2px;")
            vbox_scroll_2.addWidget(lbl_evento)
            
        vbox_scroll_2.addStretch()
        scroll_area_2.setWidget(contenedor_2)
        scroll_layout_2.addWidget(scroll_area_2)

        info_layout.addWidget(scroll_group_2)

        central_layout.addLayout(info_layout, stretch = 1)
        main_layout.addLayout(central_layout)

        # ---- APLICAR MAIN LAYOUT A LA VENTANA ----
        self.setLayout(main_layout)

    # ---------- ACCIONES ----------
    def volver_inicio(self):
        self.hide()
        self.senal_volver_inicio.emit()

    def hacer_consulta(self):
        pass 
# =============================================================================