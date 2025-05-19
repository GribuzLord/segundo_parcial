import numpy as np

def n_reinas(n):
        
    
    ##Pone una matriz llena de ceros y pone un 1 donde haya una reina
    def imprimir_tablero(tablero):
        ##Matriz de puros 0 nxn
        tablerito = np.zeros((n, n))
        
        ##Recorre cada fila del tablero
        for fila in range(n):
            ##Aun no hay reina ahi
            if tablero[fila] != -1:
                ##Pone un uno en la posicion de la reina 
                tablerito[fila, tablero[fila]] = 1 
        ##Imprime la matriz con 1 donde hay una reina y 0 donde no hubo pq de eso ya estaba llena
        print(tablerito)
        print()

    ##Se llena el tablero de puros -1
    tablero = [-1] * n  # Una reina por fila
    fila = 0            # Empezamos desde la primera fila

    while fila >= 0:
        tablero[fila] += 1  # Se mueve la reina a la siguiente columna

        while tablero[fila] < n:
            col = tablero[fila]
            # Verificamos si la reina en (fila, col) es válida
            valida = True
            
            ##Se checa que la posicion sea valida
            for i in range(fila):
                ##Checa columna
                if (tablero[i] == col or
                    ##Checa diagonal abajo derecha
                    tablero[i] - i == col - fila or
                    ##Checa diagonal abajo izquierda
                    tablero[i] + i == col + fila):
                    valida = False
                    break
            
            if valida:
                break  # Encontramos una posición válida
            ##Si no nos pasamos a la siguiente
            else:
                tablero[fila] += 1  # Intentamos la siguiente columna

        ##Si ya no hay mas columnas para recorrer
        if tablero[fila] < n:
            
            if fila == n - 1:
                imprimir_tablero(tablero)
                # Nos brincamos a la fila anterior
                tablero[fila] = -1
                fila -= 1
            else:
                ##Si ya se pudo poner la reina va a la siguiente fila
                fila += 1
                tablero[fila] = -1  # Inicializamos la nueva fila
        else:
            ##Si de plano no se pudo nada ya se regresa todo de nuevo
            # No hay más columnas válidas en esta fila, hacemos backtracking
            tablero[fila] = -1
            fila -= 1



n_reinas(5)

##NOTA: tablero[fila] representa la columna donde esta la reina 