# Tarea 2: DCCornucopia (???)⚡🐁⭕

Nombre Alumno: Agustín Rodrigo Villavicencio Vera
N.° de estudiante: 25663712 
Sección: 2
Profesor: Pablo Araneda

# Actualizaciones Tarea ⚡🐁⭕
Last Update: 15-05-26
## Evaluación personal de las Secciones
Explicación: A partir de los siguientes emojis se explicará el avance logrado desde mi punto de vista y el código real:
- ❌ si **NO** no se completó lo pedido
- ✅ si se completó **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores

#### Carga de datos✅:
Desde ```consultas.py``` se pueden ejecutar todas las funciones de lectura de archivos de todos los tamaños establecidos.

#### Consultas con datos de archivos ✅🟠:
Desde ```consultas.py``` se realizan la mayor parte de las consultas que solo ocupan datos de lectura y generadores.

#### Carga de ejecución y simulación ❌:
Sección NO realizada, ninguna de las funciones que implican simulación y/o lista ligada.

#### Interfaz Gráfica e Interacción ✅❌🟠:
Al ejecutar ```main.py```, se podrá navegar entre las 3 interfaces gráficas solicitadas, sin embargo, estas no cuentan con la implementación de la simulación de DCCornucopia, se cumplen la mayoría de elementos mínimos, en particular faltan los botones de control de simulación.

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```, desde este módulo se inicia la ventana principal, tanto por terminal como por un editor de código. NO se debe crear ningún módulo aparte, se espera solamente que la carpeta sprite esté dentro de la carpeta /frontend para la visualización de los juguetes en la ventana de .


1. ```/sprites``` en ```/frontend```


Respecto a los testcases de la parte de ```consultas.py```, todos los completados permiten su ejecución desde la carpeta raíz de la tarea (/T2), basándose en los test públicos.

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```PyQt6.QtWidgets```: ```QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QScrollArea, QFileDialog, QGroupBox, QLineEdit, QGridLayout```

2. ```PyQt6.QtGui```: ```QPixmap, QIcon``` 

3. ```PyQt6.QtCore```: ```Qt, pyqtSignal``` 

Todo el módulo de ```PyQt6``` debe instalarse por terminal, tanto en la misma IDE de codificación o en la ruta raíz.

```pip install pyqt6```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```helpers.py```: Contiene métodos de conversión de strings del tipo "hh:mm" y viceversa.


## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Ninguno por mencionar.

## Otros comentarios
Sin comentarios adicionales.

## Material Rescatado (STACKOVERFLOW/INTERNET)

### Converting a column of minutes to hours and minutes in Python
https://stackoverflow.com/questions/51565978/converting-a-column-of-minutes-to-hours-and-minutes-in-python

### PyQt - assign to a button the ability to choose a directory
https://stackoverflow.com/questions/41587541/pyqt-assign-to-a-button-the-ability-to-choose-a-directory