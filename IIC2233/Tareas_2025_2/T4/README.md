# Tarea 4: DCCasino: Gambling 151 🌃 🟩⬛🟩⬛🟩
En "colaboración" (...) con el Ferxoo llega el mejor programa de apuestas en localhost para computadores, quédate en banca rota mientras escuchas las rolas más populares del Feid como "Normal", "Feliz cumpleaños Ferxoo", "Ferxoo151" y el tema que inspiró toda la "belleza" del  programa, [California](https://www.youtube.com/watch?v=Qvm9QQ7laKk&list=RDQvm9QQ7laKk); A apostar se ha dicho!.

Por: Agustín Rodrigo Villavicencio Vera

Sección : 3 

Profesora Francisca Ibarra

2025-2
## Consideraciones generales :octocat:

<Descripción de lo que hace y que **_no_** hace la tarea que fue entregada
el día 25 de noviembre de 2025>

### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: Según el emoji correspondiente, de la manera más honesta, para cada item fue marcado a su lado el grado de cumplimiento que se espera en la corrección de la tarea:

- ❌ si **NO** se completó lo pedido.
- ✅ si se completó **correctamente** lo pedido.
- 🟠 si el item está **incompleto** o tiene algunos errores.

**⚠️ADEMÁS DE COLOCAR CON SU RESPECTIVO COLOR TAMBIEN SE MENCIONA LA FUNCIONALIDAD DE DICHO ÍTEM⚠️**

#### Desarrollo de la Tarea
##### ✅🟠 Tareas / ítems realizados o no
A continuación se muestra un listado descriptivo de cada uno de los ítems solicitados en la tarea, desde la muestra de interfaz gráfica y sus implementaciones de cliente y servidor.

#### Cliente
Al iniciar desde /T4 con py client/main.py :

##### ✅ Ventana de Entrada

Ventana inicial que se ejecuta para cada usuario independiente al ejecutar la línea de arriba en la terminal, aparece la interfaz para ingresar nombre de usuario, donde evalua si el usuario existe para recuperar su saldo, si el usuario es nuevo para crearlo y otorgarle un saldo inicial o en caso de que no se ingrese nombre el sistema no dejará entrar a la ventana principal hasta que se cumpla alguno de los dos primeros casos mencionados. dirige mediante botones al Menú Principal (con la consideración anterior) o para cerrar el programa (sin haberlo jugado).
##### ✅🟠 Ventana Principal	

Corresponde al dicho Menú Principal (...) al que se llega desde Ventana de Entrada y volviendo de los menús de juego, cuenta con la información del usuario que ingreso desde ventana inicial, mostrando el nombre y saldo del usuario (si es que tenía o es nuevo), con los botones para dirigirse a cada juego y para retroceder a la ventana principal.
##### ❌🟠 Ventanas de Juego

Desarrollo de los juegos no implementados, solo incluyen una lista de los usuarios que están conectados en ese instante en la misma ventana.


##### 🟠 Flujo

Como se indico arriba, el programa cumple con el flujo entre ventanas para cada usuario, sin embargo, las restricciones para entrar en dichos juegos (que no se realizó) no fue implementado.


## Ejecución :computer:
Para ejecutar el programa, primero se tiene correr el servidor, hay que ubicarse en la carpeta de la tarea *T4*, luego moverse a *server* y colocar en la terminal *py main.py*.

Una vez hecho lo anterior, desde otra terminal, en la misma carpeta *T4*, se tiene que correr el comando *py client/main.py* por cada uno de los usuarios que se vayan a conectar a la aplicación.


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```pyqt5```: junto con todos sus sub-módulos para uso de interfaz gráfica.
2. ```collections```: ```defaultdict```
3. ```datetime```: Para obtener la fecha exacta de cuando el usuario creo su "user" por primera vez
4. ```json```:para trabajar con datos con formato JSON

### Estructura de carpetas del trabajo
A continuación se muestra la estructura de carpetas y archivos que conforman el trabajo realizado:
T4  : Carpeta de la tarea **

|-/client

|---/Assets

|---|---/(carpetas de imagenes de cada juego)

|---/backend

|---|---connection_handler.py

|---/frontend

|---|---/sprites

|---|---client.py

|---|---ventana_aviator.py

|---|---ventana_blackjack.py

|---|---ventana_inicial.py

|---|---ventana_principal.py

|---|---main.py 

|---main.py

|-/server

|---/data

|---|---(archivos csv de registros de usuario y ganancias)

|---conexion.json

|---main.py

|---parametros.py

|-.gitignore

|-README.md


## Supuestos y consideraciones adicionales :thinking:

Las ventanas emergentes pertenecientes a la parte del desarrollo de la interfaz gráfica, títulos y algunos mensajes cuentan con referencias e inspiración a los álbumes "Mor, no le temas a la oscuridad" y "Ferxoo 151" del artista español Feid o Ferxoo, he aquí el porqué todas las ventanas cuentan con ese verde oscuro y fluorescente caracteristico de dichos álbumes y del artista. Por temas obvios, no puedo atribuir derechos de autor a dicho artista, cabe igual mencionar que los backgrounds fueron hechos con ayuda de *gemini_ai* con algunos cambios de estilo hechos con la aplicación *[Krita](https://krita.org/es/)*, mientras que las fuentes de los títulos fueron hechas con la ayuda de *[Da font Es](https://www.dafont.com/es/edo-sz.font?text=ferxxo)*, siendo así, doy los agradecimientos y créditos pertinentes a dichas aplicaciones/ sitios webs.




