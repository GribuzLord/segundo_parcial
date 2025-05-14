import numpy as np

def es_valido(tablero, fila, col, num):
    # Verifica fila y columna
    if num in tablero[fila, :] or num in tablero[:, col]:
        return False
    
    # Verifica cuadro 3x3
    inicio_fila = (fila // 3) * 3
    inicio_col = (col // 3) * 3
    subcuadro = tablero[inicio_fila:inicio_fila+3, inicio_col:inicio_col+3]
    
    if num in subcuadro:
        return False

    return True

def resolver_sudoku(tablero):
    for fila in range(9):
        for col in range(9):
            if tablero[fila, col] == 0:
                for num in range(1, 10):
                    if es_valido(tablero, fila, col, num):
                        tablero[fila, col] = num
                        if resolver_sudoku(tablero):
                            return True
                        tablero[fila, col] = 0  # Backtrack
                return False  # No hay número válido, se activa el backtracking
    return True  # Se resolvió correctamente

# Tablero
sudoku = np.array([
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

if resolver_sudoku(sudoku):
    print("Sudoku resuelto:")
    print(sudoku)
else:
    print("No se pudo resolver el Sudoku.")




# A A A | B B B | C C C 0
# A A A | B B B | C C C 1
# A A A | B B B | C C C 2
# ------+-------+------
# D D D | E E E | F F F 3
# D D D | E E E | F F F 4
# D D D | E E E | F F F 5
# ------+-------+------
# G G G | H H H | I I I 6
# G G G | H H H | I I I 7
# G G G | H H H | I I I 8
# 0 1 2   3 4 5   6 7 8

##(1,1)

##(4,4)

##(7,8)

# def mostrar_subcuadro(tablero, fila, col):
#     inicio_fila = (fila // 3) * 3
#     inicio_col = (col // 3) * 3
#     subcuadro = tablero[inicio_fila:inicio_fila+3, inicio_col:inicio_col+3]

#     print(f"Celda ({fila}, {col}) está en el subcuadro que empieza en ({inicio_fila}, {inicio_col})")
#     print("Subcuadro:")
#     print(subcuadro)

# mostrar_subcuadro(sudoku, 4, 7)
