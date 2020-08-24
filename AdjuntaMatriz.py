import Libreria.Transpuestas
import Libreria.ConjugadaMatriz


def adgjunta_matriz(matriz):
    return convertir(matriz)

def convertir(matriz):
    matriz = Libreria.Transpuestas.transpuesta(matriz)
    matriz = Libreria.ConjugadaMatriz.conjudada_matriz(matriz)
    return matriz

