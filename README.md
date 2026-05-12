# TP2 - Búsqueda en el espacio de estados

Este repositorio contiene el prototipo desarrollado para el TP2 de Inteligencia Artificial.

El programa simula la búsqueda del punto correcto de montaje de un brazo robotizado, partiendo desde una posición inicial teórica B hasta encontrar la posición real A.

## Métodos implementados

- Búsqueda exhaustiva: primero en anchura.
- Búsqueda heurística: método A*.

## Lenguaje utilizado

Python.

## Archivo principal

El archivo principal del prototipo es `main.py`.

## Explicación general

La búsqueda exhaustiva explora las posiciones posibles sin usar información adicional, revisando ambos sentidos hasta encontrar la meta.

La búsqueda heurística A* utiliza la función f(n) = g(n) + h(n), donde g(n) representa el costo recorrido y h(n) representa la distancia estimada hasta la meta.

En la ejecución del prototipo, la búsqueda exhaustiva evalúa 13 posiciones, mientras que la búsqueda heurística A* evalúa 7 posiciones.

## Relación con la situación problemática

El prototipo representa de forma simplificada el problema del brazo robotizado que debe encontrar el punto correcto de montaje cuando el block del motor no se encuentra en la posición esperada. Para eso, se modela el problema como una búsqueda en el espacio de estados, donde la posición inicial es B y la posición objetivo es A.
