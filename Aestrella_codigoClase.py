

import numpy as np
import matplotlib.pyplot as plt

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
movimientos = [(-1,1), (-1,-1), (-1,0), (0,1), (1,1), (1,0), (1,-1), (0,-1)]




def desplegar_laberinto(maze, camino=None, considerados=None):
    plt.imshow(maze, cmap='binary')
    if considerados:
        for i in considerados:
            plt.plot(i[1], i[0], 'o', color='blue')
    if camino:
        for j in camino:
            plt.plot(j[1], j[0], 'o', color='red')
    plt.show()



def heuristica(nodo_actual, objetivo):
    return (abs(objetivo[0] - nodo_actual[0]) + abs(objetivo[1] - nodo_actual[1]))

def A_estrella(laberinto, punto_inicial, meta):
    lista_abierta = [(punto_inicial, 0, heuristica(punto_inicial, meta), [])]
    
    ## nodo, g, f, camino
    filas = np.shape(laberinto)[0]
    columnas = np.shape(laberinto)[1]
    
    lista_cerrada = np.zeros((filas, columnas))
    
    ## Definir una lista que contenga a todos los nodos que se han visitado
    considerados = []

    while len(lista_abierta) > 0:
        ## En la primera iteración, se inicializa
        menor_f = lista_abierta[0][2]
        nodo_actual, g_actual, f_actual, camino_actual = lista_abierta[0]
        indice_menor_f = 0

        ## Hallar el nodo que tenga la menor cantidad de f de los nodos que están en la lista abierta
        for i in range(1, len(lista_abierta)):
            if lista_abierta[i][2] < menor_f:
                menor_f = lista_abierta[i][2]
                nodo_actual, g_actual, f_actual, camino_actual = lista_abierta[i]
                indice_menor_f = i

        ## Eliminación del nodo de menor energía en la lista abierta
        lista_abierta = lista_abierta[:indice_menor_f] + lista_abierta[indice_menor_f+1:]
        ## Guardar los nodos que han sido considerados
        considerados += [nodo_actual]

        if nodo_actual == meta:
            return camino_actual + [nodo_actual], considerados

        ## Marcamos el nodo actual como ya visitado
        lista_cerrada[nodo_actual[0], nodo_actual[1]] = 1

        ##Aqui es donde se debe modificar el inciso a
        ## Evaluar a los nodos vecinos:
        for direccion in movimientos:
            nueva_posicion = (nodo_actual[0] + direccion[0], nodo_actual[1] + direccion[1])

            if ((0 <= nueva_posicion[0] < filas) and (0 <= nueva_posicion[1] < columnas)):
                if (laberinto[nueva_posicion[0], nueva_posicion[1]] == 0 and 
                    lista_cerrada[nueva_posicion[0], nueva_posicion[1]] == 0):

                    ## Estoy en una diagonal
                    if abs(direccion[0]) == abs(direccion[1]):
                        g_nuevo = g_actual + 14
                    else:
                        g_nuevo = g_actual + 10
                    
                    f_nuevo = g_nuevo + heuristica(nueva_posicion, meta)

                    ## Comprobar si cambia de padre o no
                    bandera_padre = False
                    for nodo, g, f, camino in lista_abierta:
                        if nodo == nueva_posicion and g <= g_nuevo:
                            bandera_padre = True
                            break
                    
                    ## Si no hay cambio de padre
                    if bandera_padre == False:
                        lista_abierta += [(nueva_posicion, g_nuevo, f_nuevo, camino_actual + [nueva_posicion])]
    
    return None, considerados

## Ejecutar
camino, considerados = A_estrella(laberinto, punto_inicial, meta)
desplegar_laberinto(laberinto, camino,considerados)