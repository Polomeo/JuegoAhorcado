Juego del Ahorcado programado para consola en Python
----------------------------------------------------

Este juego es un ejercicio realizado para el curso "Python Total", dictado por el profesor Federico Garay en Udemy.

Los requerimientos del proyecto fueron los siguientes:

- El programa elije una palabra secreta
- El programa presenta al jugador la cantidad de letras de la palabra en forma de guiones
- El programa también presenta al jugador un indicador de las vidas restantes
- Se le pide al usuario que ingrese una letra:
- - Si ingresa una letra correspondiente a la palabra, esta se posiciona en lugar del guión
  - Si ingresa una letra erronea, se le resta una vida
  - En ambos casos, si le quedan vidas restantes, se le vuelve a solicitar una letra hasta que se le acaban las vidas, o adivina la palabra.
 
El proyecto tiene algunos agregados propios:
- Si elije una letra que se encuentra más de una vez, esta se posiciona en todos los espacios donde está esa letra en la palabra oculta
- Tiene un pequeño monigote en representación de las vidas restantes
- Luego de cada intento de adivinar, se limpia la consola y muestra la interfaz con el monigote con las vidas restantes y la palabra parcialmente adivinada
