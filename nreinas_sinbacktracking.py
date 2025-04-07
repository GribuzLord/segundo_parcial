import numpy as np

def n_reinas(n):
    def imprimir_tablero(tablero):
        tablerito = np.zeros((n, n))
        for fila in range(n):
            if tablero[fila] != -1:
                tablerito[fila, tablero[fila]] = 1
        print(tablerito)
        print()

    tablero = [-1] * n  # Una reina por fila
    fila = 0            # Empezamos en la fila 0

    while fila >= 0:
        tablero[fila] += 1  # Intentamos la siguiente columna en esta fila

        while tablero[fila] < n:
            col = tablero[fila]
            # Verificamos si la reina en (fila, col) es válida
            valida = True
            for i in range(fila):
                if (tablero[i] == col or
                    tablero[i] - i == col - fila or
                    tablero[i] + i == col + fila):
                    valida = False
                    break

            if valida:
                break  # Encontramos una posición válida
            else:
                tablero[fila] += 1  # Intentamos la siguiente columna

        if tablero[fila] < n:
            if fila == n - 1:
                imprimir_tablero(tablero)
                # Buscamos más soluciones, así que retrocedemos
                tablero[fila] = -1
                fila -= 1
            else:
                fila += 1
                tablero[fila] = -1  # Inicializamos la nueva fila
        else:
            # No hay más columnas válidas en esta fila, hacemos backtracking
            tablero[fila] = -1
            fila -= 1

n_reinas(5)
