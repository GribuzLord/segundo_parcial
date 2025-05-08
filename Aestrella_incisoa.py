##a)Implementar la eleccion aleatoria de la forma de vistar a los vecinos (direcciones), ejecutar 4 veces y mostrar en 1 ventana los 4 subplots, mostrar la cantidad de nodos considerados y total de nodos del camino(Energia total)

import numpy as np
import matplotlib.pyplot as plt
import random

# Laberinto 16x16 con 1 representando paredes y 0 caminos
laberinto = np.array([
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,1],
    [1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,1],
    [1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,0,1,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,1,0,1,0,0,0,0,1,0,1],
    [1,1,1,1,1,0,1,0,1,0,1,1,0,1,0,1],
    [1,0,0,0,1,0,0,0,1,0,1,0,0,1,0,1],
    [1,0,1,0,1,1,1,1,1,0,1,0,1,1,0,1],
    [1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
])


# Inicialización de punto inicial y final
punto_inicial = (1, 1)
meta = (9, 14)

# Tipos de movimiento
movimientos_base = [(-1,1), (-1,-1), (-1,0), (0,1), (1,1), (1,0), (1,-1), (0,-1)]


def heuristica(nodo, objetivo):
    return abs(nodo[0] - objetivo[0]) + abs(nodo[1] - objetivo[1])

def A_estrella(laberinto, inicio, meta):
    lista_abierta = [(inicio, 0, heuristica(inicio, meta), [])]
    
    ## nodo, g, f, camino
    filas, columnas = laberinto.shape
    lista_cerrada = np.zeros((filas, columnas))
    considerados = []

    while len(lista_abierta) > 0:
        lista_abierta.sort(key=lambda x: x[2])
        nodo_actual, g_actual, f_actual, camino_actual = lista_abierta[0]
        lista_abierta = lista_abierta[1:]
        considerados += [nodo_actual]

        if nodo_actual == meta:
            return camino_actual + [nodo_actual], considerados

        lista_cerrada[nodo_actual[0], nodo_actual[1]] = 1
        movimientos = movimientos_base.copy()
        random.shuffle(movimientos)

        for direccion in movimientos:
            nueva_pos = (nodo_actual[0] + direccion[0], nodo_actual[1] + direccion[1])

            if (0 <= nueva_pos[0] < filas and 0 <= nueva_pos[1] < columnas and
                laberinto[nueva_pos[0], nueva_pos[1]] == 0 and
                lista_cerrada[nueva_pos[0], nueva_pos[1]] == 0):

                g_nuevo = g_actual + (14 if abs(direccion[0]) == abs(direccion[1]) else 10)
                f_nuevo = g_nuevo + heuristica(nueva_pos, meta)

                reemplazar = True
                for n, g, f, c in lista_abierta:
                    if n == nueva_pos and g <= g_nuevo:
                        reemplazar = False
                        break

                if reemplazar:
                    nuevo_camino = camino_actual + [nueva_pos]
                    lista_abierta = lista_abierta + [(nueva_pos, g_nuevo, f_nuevo, nuevo_camino)]

    return None, considerados

def calcular_energia_total(camino):
    energia = 0
    for i in range(1, len(camino)):
        dx = abs(camino[i][0] - camino[i-1][0])
        dy = abs(camino[i][1] - camino[i-1][1])
        energia += 14 if dx == 1 and dy == 1 else 10
    return energia

# Mostrar resultados de 4 ejecuciones
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle("A* con vecinos aleatorios (4 ejecuciones)", fontsize=16)

for i in range(4):
    camino, considerados = A_estrella(laberinto, punto_inicial, meta)
    energia_total = calcular_energia_total(camino) if camino else 0

    ax = axs[i//2, i%2]
    ax.imshow(laberinto, cmap='binary')

    if considerados:
        x, y = zip(*considerados)
        ax.plot(y, x, 'o', color='blue', markersize=3)

    if camino:
        x, y = zip(*camino)
        ax.plot(y, x, 'o', color='red', markersize=3)

    ax.set_title(f"Intento {i+1}\nConsiderados: {len(considerados)} | Energía total: {energia_total}")
    ax.axis('off')

plt.tight_layout()
plt.subplots_adjust(top=0.88)
plt.show()
