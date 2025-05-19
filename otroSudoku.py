import numpy as np
import math




def resolver_sudoku(tablero):
    
    ##Se define el tamaño del tablero y los subcuadros (solo funciona con cuadrados perfectos)
    n = len(tablero)
    sqrt_n = int(math.sqrt(n))

    
    
    
    
    
    ##Funcion que valida donde colocar cada numero
    
    def es_valido(fila, col, num):
        
        # Validar fila
        if num in tablero[fila]:
            return False
        
        # Validar columna
        for i in range(n):
            if tablero[i][col] == num:
                return False

        # Validar subcuadro
        inicio_fila = (fila // sqrt_n) * sqrt_n
        inicio_col = (col // sqrt_n) * sqrt_n
        for i in range(inicio_fila, inicio_fila + sqrt_n):
            for j in range(inicio_col, inicio_col + sqrt_n):
                if tablero[i][j] == num:
                    return False
        return True





    def backtrack():
        for fila in range(n):
            for col in range(n):
                if tablero[fila][col] == 0:
                    for num in range(1, n + 1):
                        if es_valido(fila, col, num):
                            tablero[fila][col] = num
                            if backtrack():
                                return True
                            tablero[fila][col] = 0
                    return False  # No hay número válido
        return True  # Tablero completo


    ##Se entregan las respuestas
    if backtrack():
        print("Solución encontrada:")
        print(np.array(tablero))
    else:
        print("No hay solución válida")



tablero_inicial = np.array([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0], ##Un 1 despues del 6
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
])

resolver_sudoku(tablero_inicial)
