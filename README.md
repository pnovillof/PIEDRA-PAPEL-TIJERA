1. INTRODUCCIÓN.
Se seleccionó el juego “Piedra, Papel o Tijera”.

Las reglas del juego son: Piedra vence a la tijera,

Tijera vence al papel,

Papel vence a la piedra,

Si ambas elecciones son iguales, empate.

Nuestro objetivo es desarrollar un programa con dos jugadores —usuario y computadora— y el sistema determine automáticamente el resultado las reglas descritas anteriormente.

2. SOFTWARE
Spyder 6.1.3 / Python 3.12.11 64-bit | Qt 5.15.15 | PyQt5 5.15.11 / Windows 11 (AMD64)

3. ESTRUCTURA DEL REPOSITORIO

Código/  Diagramas/  README.md

4. DESCRIPCIÓN DEL FLUJOGRAMA

El flujograma muestra el funcionamiento del juego Piedra, Papel o Tijera. Iniciamos solicitando al usuario (A) que seleccione una opción (1 = Piedra, 2 = Papel, 3 = Tijera), mientras que la computadora (B) genera su elección de manera randomica. Luego, se comparan ambas selecciones mediante estructuras condicionales: si A y B son iguales, se declara empate; en los casos donde la combinación favorece a la computadora, se muestra “Gana Computadora”; y cuando la combinación favorece al usuario, se muestra “Gana Usuario”. Finalmente, el proceso termina.

5. LIBRERIA RANDOM

La librería "random" permite simular comportamientos aleatorios o randomicos dentro del programa. En el desarrollo del juego Piedra, Papel o Tijera, se utiliza para generar la elección aleatoria de la computadora.

random.randint(1, 3)
Esto significa:
Genera un número entero aleatorio entre 1 y 3. Cada vez que ejecutas el programa, la computadora puede elegir un número diferente.

CONTROL DE CAMBIOS.
2026-03-01 - 8:37: Se actualiza el diagrama unifilar para incluir un bucle que permite reiniciar el juego y la función "Resultados", responsable de evaluar y determinar el ganador o si es empate. Además se incorporó un validador de datos de entrada
