# BuscaMinas
Tipico juego del buscaminas programado con python y usando caracteres como metodo de visualizacion.

Logica inicial desarrollada durante mis ratos libres sin ayuda de tutoriales o guias y optimizada con ayuda de IA.
Al ejecutar el programa, genera las posiciones de las minas siguiendo los limites y cantidad de minas (altura*largo/minas) segun la dificultad de juego que se elija, seguidamente pide al usuario que introduzca si quiere "dar un paso" o "colocar una bandera", a continuacion pedirá unas coordenadas siguiendo los limites del tablero donde el usuario realizara la accion segun el modo en el que se encuentre, una vez introducidas unas coordenadas, se mostrara el tablero revelando cuanta minas hay alrededor de la coordenada seleccionada en la propia casilla,las banderas se mostraran como "P", estas se ponen y quitan excribiendo la misma cordenada, el resto del tablero se oculta con 'X':

<img width="452" alt="Screenshot 2025-06-17 143059" src="https://github.com/user-attachments/assets/864fcc85-11e8-4da9-b2e9-29a1b8c9b8e8" />


Si la coordenada seleccionada no tiene ninguna mina alrededor se mostrara la casilla como '0' y mostrara las casillas alrededor de esta, de manera que si hay otra casilla sin minas cerca, tambien se revelaran las casillas a su alrededor y asi recursivamente.

En caso de marcar todas las casillas sin minas, el juego te felicitara y terminara de ejecutar.
![image](https://github.com/user-attachments/assets/76b252df-0dff-4c20-ada2-108abfa8c2b5)

