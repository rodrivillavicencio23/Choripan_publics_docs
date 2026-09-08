# Tarea 3: Departamento de las Colecciones del Cosmos 🌌

Por: Agustín Rodrigo Villavicencio Vera
Sección : 3 
Profesora Francisca Ibarra
2025-2
## Consideraciones generales :octocat:

<Descripción de lo que hace y que **_no_** hace la tarea que fue entregada
el día 29 de octubre de 2025>

### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: Según el emoji correspondiente, de la manera más honesta, para cada item fue marcado a su lado el grado de cumplimiento que se espera en la corrección de la tarea:

- ❌ si **NO** se completó lo pedido.
- ✅ si se completó **correctamente** lo pedido.
- 🟠 si el item está **incompleto** o tiene algunos errores.

**⚠️⚠️NO BASTA CON SOLO PONER EL COLOR DE LO IMPLEMENTADO**,
SINO QUE SE DEBERÁ EXPLICAR QUÉ SE REALIZO DETALLADAMENTE EN CADA ITEM.
⚠️⚠️

#### Desarrollo de la Tarea
##### ✅🟠 Test automatizados
A continuación paso una lista de los *tests públicos* que fueron realizados de manera correcta, parcial o no realizados/no cumplen, siguiendo con la idea del *check❌🟠✅* para cada uno, se tiene en cuenta que los *tests públicos y privados* pueden ser distintos y por lo cúal entregar una distinta salida para corroborar que la función que esté evaluando de los mismos resultados de a continuación:

python3 -B -m unittest -v -b tests_publicos.test_000_namedtuples_carga_de_datos ✅

python3 -B -m unittest -v -b tests_publicos.test_000_namedtuples_correctitud ✅

python3 -B -m unittest -v -b tests_publicos.test_00_naves_de_material_carga_de_datos✅

python3 -B -m unittest -v -b tests_publicos.test_00_naves_de_material_correctitud✅

python3 -B -m unittest -v -b tests_publicos.test_01_misiones_desde_fecha_correctitud ✅

python3 -B -m unittest -v -b tests_publicos.test_02_naves_por_intervalo_carga_carga_de_datos✅

python3 -B -m unittest -v -b tests_publicos.test_02_naves_por_intervalo_carga_correctitud✅

python3 -B -m unittest -v -b tests_publicos.test_03_planetas_con_cantidad_de_minerales_carga_datos✅

python3 -B -m unittest -v -b tests_publicos.test_03_planetas_con_cantidad_de_minerales_correctitud ✅

python3 -B -m unittest -v -b tests_publicos.test_04_naves_astronautas_rango_carga_de_datos ✅

python3 -B -m unittest -v -b tests_publicos.test_04_naves_astronautas_rango_correctitud ✅

python3 -B -m unittest -v -b tests_publicos.test_05_cambiar_rango_astronauta_carga_datos✅

python3 -B -m unittest -v -b tests_publicos.test_05_cambiar_rango_astronauta_correctitud✅

python3 -B -m unittest -v -b tests_publicos.test_06_encontrar_planetas_cercanos_correctitud✅

python3 -B -m unittest -v -b tests_publicos.test_07_disponibilidad_por_planeta_carga_de_datos✅

python3 -B -m unittest -v -b tests_publicos.test_07_disponibilidad_por_planeta_correctitud✅

python3 -B -m unittest -v -b tests_publicos.test_08_misiones_por_tipo_planeta_carga_datos✅

python3 -B -m unittest -v -b tests_publicos.test_08_misiones_por_tipo_planeta_correctitud✅

python3 -B -m unittest -v -b tests_publicos.test_10_naves_pueden_llevar_carga_de_datos✅

python3 -B -m unittest -v -b tests_publicos.test_10_naves_pueden_llevar_correctitud✅


##### ---- 3 generadores --- ######

0/6 
python3 -B -m unittest -v -b tests_publicos.test_09_planetas_por_estadisticas_carga_datos❌

1/6
python3 -B -m unittest -v -b tests_publicos.test_09_planetas_por_estadisticas_correctitud❌

python3 -B -m unittest -v -b tests_publicos.test_11_ganancias_potenciales_por_planeta_carga_datos
python3 -B -m unittest -v -b tests_publicos.test_11_ganancias_potenciales_por_planeta_correctitud

python3 -B -m unittest -v -b tests_publicos.test_12_planetas_visitados_por_nave_correctitud ✅

python3 -B -m unittest -v -b tests_publicos.test_12_planetas_visitados_por_nave_carga_de_datos✅

4/6
python3 -B -m unittest -v -b tests_publicos.test_13_mineral_por_nave_correctitud🟠
0/3
python3 -B -m unittest -v -b tests_publicos.test_13_mineral_por_nave_carga_de_datos❌


python3 -B -m unittest -v -b tests_publicos.test_14_porcentaje_extraccion_carga_de_datos❌
python3 -B -m unittest -v -b tests_publicos.test_14_porcentaje_extraccion_correctitud❌

python3 -B -m unittest -v -b tests_publicos.test_15_resultado_mision_carga_datos ✅

python3 -B -m unittest -v -b tests_publicos.test_15_resultado_mision_correctitud 🟠5/6


##### ✅ Ventana de Entrada

Ventana inicial que se ejecuta al iniciar el *main.py*, dirige mediante botones al Menú Principal y para cerrar el programa.
##### 🟠 Ventana Principal	

Corresponde al dicho Menú Principal al que se llega desde Ventana de Entrada y volviendo de Ventana Mapa, cumple con mostrarse, tener los botones para el flujo entre ventanas y solo incluye de manera parcial la función de scroll y de consultas.
##### ❌🟠 Ventana Mapa

Se llega acá mediante su botón asignado de Ventana Principal, solo cuenta con el botón de retorno a dicha ventana, el Mapa Estelar no fue implementado.
##### ✅ Flujo

## Ejecución :computer:
El módulo principal de la tarea para ejecutar la interfaz gráfica  ```main.py```, mientras que para probar los *testcases*  se tiene que ocupar ```consultas.py```, almacenado en la carpeta *backend* de la *T3*.

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```pyqt5```: junto con todos sus sub-módulos para uso de interfaz gráfica.
2. ```collections```: ```defaultdict```
3. ...

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```consultas_g34```: Contiene a las funciones de consultas de 3 y 4 generadores
2. ```frontend\ventana_inicial.py```: Contiene a la clase que define a la ventana inicial de la interfaz
3. ```frontend\ventana_principal.py```: Contiene a la clase que define a la ventana Principal de la interfaz
4.  ```frontend\ventana_mapa.py```: Contiene a la clase que define a la ventana del Mapa estelar de la interfaz
5.  ```main.py```: Archivo principal que inicializa las ventanas de la interfaz del programa y conecta las señales entre estas para moverse de una a otra
## Supuestos y consideraciones adicionales :thinking:


## Consideración:
Las ventanas emergentes pertenecientes a la parte del desarrollo de la interfaz gráfica muestran contenido "decorativo" para que no quede tan vacío o blanco el programa, aunque la mayor parte de funcionalidades pedidas como mapa estelar y la función de scroll para consultas, no funcionen; volviendo con la decoración añadida, inspirada en la saga de Star Wars (en la parte de los títulos y ventana principal) junto con un edit de la portada del Albúm "Un verano sin Ti" del artista Bad Bunny, con esto en cuenta se reservan todos los derechos correspondientes a dichos aspectos.

1. <Descripción 1 y justificación del por qué es válido/a> 


