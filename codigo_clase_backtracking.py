import numpy as np

def n_reinas(n):
    def resolvedor(tablero, fila):
        if fila == n:
            imprimir_tablero(tablero, n)
            return True

        for col in range(n):
            validez = True
            for i in range(fila):
                if (tablero[i] == col or 
                    tablero[i] - i == col - fila or 
                    tablero[i] + i == col + fila):
                    validez = False
                    break

            if validez:
                tablero[fila] = col
                imprimir_tablero(tablero, n)
                if resolvedor(tablero, fila + 1):
                    return True
                print(f"Backtracking: Retirando la reina de la fila {fila}, columna {col}")
                tablero[fila] = -1

        return False

    def imprimir_tablero(tablero, n):
        tablerito = np.zeros((n, n))
        for i in range(n):
            if tablero[i] != -1:
                tablerito[i, tablero[i]] = 1
        print(tablerito)
        print()  # Separador para ver mejor cada tablero

    tablero = [-1] * n
    if not resolvedor(tablero, 0):
        print("No hay solucion")

n_reinas(5)
