import Libreria.AdjuntaMatriz
import Libreria.MultiplicacionMatrices
import numpy as np


def matriz_unitaria(matriz):
    matriz1 = Libreria.AdjuntaMatriz.adgjunta_matriz(matriz)
    return producto(matriz, matriz1)


def producto(matriz, matri1):
    resultado = Libreria.MultiplicacionMatrices.multiplicacion_matrices(matriz, matri1)
    return unitaria(resultado)


def unitaria(resultado):
    matriz_u = np.identity(len(resultado))
    matriz_unitaria1 = []
    for i in range(len(matriz_u)):
        a = []
        for j in range(len(matriz_u[0])):
            a.append(complex(matriz_u[i][j]))
        matriz_unitaria1.append(a)
    if matriz_unitaria1 == resultado:
        return True
    return False



