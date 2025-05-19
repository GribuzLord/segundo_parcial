import numpy as np
import math




def resolver_sudoku(tablero):
    
    ##Se define el tamaño del tablero y los subcuadros (solo funciona con cuadrados perfectos)
    ##n tamaño del tablero y la otra subcuadors
    n = len(tablero)
    sqrt_n = int(math.sqrt(n))

    
    
    
    
    
    ##Funcion que valida donde colocar cada numero
    
    def es_valido(fila, col, num):
        
        # Num no esta en fila
        if num in tablero[fila]:
            return False
        
        # Num no esta en columna
        for i in range(n):
            if tablero[i][col] == num:
                return False

        # Validar subcuadro (MUCHO OJO):
        
        ##Con las dos lineas de abajo se ubicaa el subcuadro con una division entera (//) y se ubica en la esquina superior izquierda
        inicio_fila = (fila // sqrt_n) * sqrt_n
        inicio_col = (col // sqrt_n) * sqrt_n
        
        ##Recorre el subcuadro para checar que el numero no este en alguna posicion
        ##Checa fila
        for i in range(inicio_fila, inicio_fila + sqrt_n):
            ##Checa columna
            for j in range(inicio_col, inicio_col + sqrt_n):
                ##Confirma que no haya numeros iguales al evaluado
                if tablero[i][j] == num:
                    ##Si hay
                    return False
        ##No hay
        return True




    ##Repite el proceso de arriba para llenar todas las celdas vacias
    def backtrack():
        ##Busca celdas vacias
        for fila in range(n):
            for col in range(n):
                if tablero[fila][col] == 0: ##Encuentra celda vacia
                    
                    ##Prueba los numeros posibles del 1 al 10
                    for num in range(1, n + 1):
                        ##Llama a la funcion de arriba para checar que el numero se pueda poner 
                        if es_valido(fila, col, num):
                            ##Coloca el numero si fue valido
                            tablero[fila][col] = num
                            ##Se pone el numero y se vuelve a llamar la funcion
                            if backtrack():
                                return True
                            ##Si no se cumple vuelve a poner 0 y trata con otro numero
                            tablero[fila][col] = 0
                    ##Ya se probaron todos los numeros y ninguno jaló, se va al nivel anterior
                    return False  # No hay número válido
        return True  # Tablero completo sin celdas vacias pa


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
