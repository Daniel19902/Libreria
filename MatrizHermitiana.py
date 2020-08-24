import Libreria.AdjuntaMatriz



def matriz_hermitiana(matriz):
    adjunta = Libreria.AdjuntaMatriz.adgjunta_matriz(matriz)
    return comprobar(matriz, adjunta)

def comprobar(matriz, adjunta):
    if matriz == adjunta:
        return True
    return False



