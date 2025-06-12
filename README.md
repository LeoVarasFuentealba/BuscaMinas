# BuscaMinas
Tipico juego del buscaminas programado con python y usando caracteres como metodo de visualizacion.

Logica inicial desarrollada durante mis ratos libres sin ayuda de tutoriales o guias y optimizada con ayuda de IA
Al ejecutar el programa, genera las posiciones de las minas siguiendo los limites ya especificados del tablero, seguidamente pide al usuario que introduzca si quiere "dar un paso" o "colocar una bandera", seguidamente pedirá unas coordenadas siguiendo los limites del tablero donde el usuario realizara la accion segun el modo en el que se encuentre, una vez introducidas unas coordenadas, se mostrara el tablero revelando cuanta minas hay alrededor de la coordenada seleccionada en la propia casilla seleccionada, el resto del tablero se oculta con 'X':
![Screenshot 2025-06-12 151348](https://github.com/user-attachments/assets/ca5cdd9b-70c7-430d-8647-bb5cacb69656)

Si la coordenada seleccionada no tiene ninguna mina alrededor se mostrara la casilla como '0' y mostrara las casillas alrededor de esta, de manera que si hay otra casilla sin minas cerca, tambien se revelaran las casillas a su alrededor y asi recursivamente.

El juego no esta terminado, pero es funcional en su parte mas importante, falta controlar el fin del juego en caso de ganar y algunos otros retoques.
