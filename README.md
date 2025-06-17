# BuscaMinas
Tipico juego del buscaminas programado con python y usando caracteres como metodo de visualizacion.

Logica inicial desarrollada durante mis ratos libres sin ayuda de tutoriales o guias y optimizada con ayuda de IA
Al ejecutar el programa, genera las posiciones de las minas siguiendo los limites ya especificados del tablero, seguidamente pide al usuario que introduzca si quiere "dar un paso" o "colocar una bandera", seguidamente pedirá unas coordenadas siguiendo los limites del tablero donde el usuario realizara la accion segun el modo en el que se encuentre, una vez introducidas unas coordenadas, se mostrara el tablero revelando cuanta minas hay alrededor de la coordenada seleccionada en la propia casilla,las banderas se mostraran como "P", estas se ponen y quitan excribiendo la misma cordenada, el resto del tablero se oculta con 'X':

<img width="452" alt="Screenshot 2025-06-17 143059" src="https://github.com/user-attachments/assets/864fcc85-11e8-4da9-b2e9-29a1b8c9b8e8" />


Si la coordenada seleccionada no tiene ninguna mina alrededor se mostrara la casilla como '0' y mostrara las casillas alrededor de esta, de manera que si hay otra casilla sin minas cerca, tambien se revelaran las casillas a su alrededor y asi recursivamente.

El juego no esta terminado, pero es funcional en su parte mas importante, falta controlar el fin del juego en caso de ganar y algunos otros retoques.
