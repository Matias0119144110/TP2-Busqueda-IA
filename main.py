from collections import deque
import heapq

# ------------------------------------------------------------
# Simulación del problema
# ------------------------------------------------------------
# B representa la posición inicial teórica del robot.
# A representa la nueva posición real del punto de montaje.
# En una planta real, A no sería conocido directamente:
# el robot lo detectaría mediante sensores, palpado o relieve.
B = 0
A = 6

LIMITE_IZQUIERDO = -10
LIMITE_DERECHO = 10


def es_meta(posicion):
    """
    Verifica si la posición actual coincide con el punto real de montaje.
    """
    return posicion == A


def generar_sucesores(posicion):
    """
    Genera los movimientos posibles del robot.
    En este caso, el robot puede moverse una unidad a la izquierda
    o una unidad a la derecha sobre la línea horizontal H.
    """
    sucesores = []

    izquierda = posicion - 1
    derecha = posicion + 1

    if izquierda >= LIMITE_IZQUIERDO:
        sucesores.append(izquierda)

    if derecha <= LIMITE_DERECHO:
        sucesores.append(derecha)

    return sucesores


# ------------------------------------------------------------
# 1) Búsqueda exhaustiva: primero en anchura
# ------------------------------------------------------------
def busqueda_exhaustiva(inicio):
    """
    Búsqueda exhaustiva no informada.
    Este recorre ordenadamente el espacio de estados sin usar una busqueda heurística.
    """

    cola = deque()
    cola.append((inicio, [inicio]))

    visitados = set()
    visitados.add(inicio)

    pasos = 0

    while cola:
        posicion_actual, camino = cola.popleft()
        pasos += 1

        print(f"[Exhaustiva] Palpando posición: {posicion_actual}")

        if es_meta(posicion_actual):
            return camino, pasos

        for sucesor in generar_sucesores(posicion_actual):
            if sucesor not in visitados:
                visitados.add(sucesor)
                cola.append((sucesor, camino + [sucesor]))

    return None, pasos


# ------------------------------------------------------------
# 2) Búsqueda heurística: A*
# ------------------------------------------------------------
def heuristica(posicion):
    """
    Estima qué tan lejos está una posición del objetivo.
    En este prototipo usamos la distancia absoluta hasta A.
    En un caso real, esta estimación podría surgir de sensores,
    relieve de la superficie o visión artificial.
    """
    return abs(A - posicion)


def busqueda_heuristica_a_estrella(inicio):
    """
    Búsqueda heurística A*.
    Usa la función f(n) = g(n) + h(n).
    g(n): costo recorrido desde el inicio.
    h(n): estimación de distancia hasta la meta.
    """

    cola_prioridad = []
    heapq.heappush(cola_prioridad, (heuristica(inicio), 0, inicio, [inicio]))

    visitados = set()
    pasos = 0

    while cola_prioridad:
        f, costo, posicion_actual, camino = heapq.heappop(cola_prioridad)
        pasos += 1

        print(f"[Heurística A*] Evaluando posición: {posicion_actual} | f={f}, g={costo}, h={heuristica(posicion_actual)}")

        if es_meta(posicion_actual):
            return camino, pasos

        if posicion_actual in visitados:
            continue

        visitados.add(posicion_actual)

        for sucesor in generar_sucesores(posicion_actual):
            if sucesor not in visitados:
                nuevo_costo = costo + 1
                nueva_f = nuevo_costo + heuristica(sucesor)
                heapq.heappush(
                    cola_prioridad,
                    (nueva_f, nuevo_costo, sucesor, camino + [sucesor])
                )

    return None, pasos


# ------------------------------------------------------------
# Ejecución del prototipo
# ------------------------------------------------------------
print("PROTOTIPO: BÚSQUEDA DEL PUNTO DE MONTAJE DEL ROBOT")
print("Posición inicial B:", B)
print("Posición real de montaje A:", A)
print()

print("----- BÚSQUEDA EXHAUSTIVA -----")
camino_exhaustivo, pasos_exhaustivo = busqueda_exhaustiva(B)

print("\nResultado búsqueda exhaustiva:")
print("Camino encontrado:", camino_exhaustivo)
print("Cantidad de posiciones evaluadas:", pasos_exhaustivo)

print("\n----- BÚSQUEDA HEURÍSTICA A* -----")
camino_heuristico, pasos_heuristico = busqueda_heuristica_a_estrella(B)

print("\nResultado búsqueda heurística:")
print("Camino encontrado:", camino_heuristico)
print("Cantidad de posiciones evaluadas:", pasos_heuristico)