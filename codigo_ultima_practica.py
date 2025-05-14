import numpy as np
import matplotlib.pyplot as plt

# Datos
X1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
Yd = np.array([2, 5, 8, 10, 14.5, 19, 20, 24.5, 29])

# Hiperparámetros
b0 = 0.0
b1 = 1.0
lr = 0.01
m = len(X1)
L = 0.0

# Epsilon
epsilon = 1e-6

# Variables
max_epochs = 100000  
ECM_record = [0] * max_epochs
ecm_prev = float('inf')
epoch = 0

# Entrenamiento
for i in range(max_epochs):
    
    
    Yobt = b0 + b1 * X1
    b0 = b0 - (lr/m) * np.sum(Yobt - Yd)
    b1 = b1 - (lr/m) * np.dot((Yobt - Yd), X1)
    
    ecm = (1/(2*m)) * np.sum((Yd - Yobt)**2)
    
    ECM_record[i] = ecm

    # Verificar convergencia
    if abs(ecm - ecm_prev) < epsilon:
        
        print(f"Convergencia alcanzada en la época {i}")
        epoch = i + 1
        break

    ecm_prev = ecm

#Se muestra hasta donde se llego en epocas
ECM_record = ECM_record[:epoch]

# Resultados
print("El valor final de b0 es:", b0)
print("El valor final de b1 es:", b1)
print("El último ECM es:", ecm)

# Mostrar los resultados del descenso
plt.plot(ECM_record)
plt.xlabel("Épocas")
plt.ylabel("ECM")
plt.title("Descenso de gradiente con parada por epsilon")
plt.grid(True)
plt.yscale("log")  # Para visualizar mejor el descenso exponencial
plt.show()
