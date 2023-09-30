import numpy as np

def criar_matriz_aleatoria():
    matriz = np.zeros((5, 5), dtype=int)
    bombas = 0
    
    while bombas < 1:
        x, y = np.random.randint(5, size=2) 
        if matriz[x, y] == 0:
            matriz[x, y] = -1  
            bombas += 1
    
    return matriz

matrizes = [criar_matriz_aleatoria() for _ in range(2)]

print(matrizes[1])