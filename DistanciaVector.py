import Libreria.AdicionVector
import Libreria.NormaVector



def distancia_vectores(vectorA, vectorB):
    return distancia(vectorA, vectorB)


def distancia(vectorA, vectorB):
    for i in range(len(vectorB)):
        r = vectorB[i]
        vectorB[i] = (r[0]*-1, r[1]*-1)
    adicion = Libreria.AdicionVector.suma(vectorA, vectorB)
    norma = Libreria.NormaVector.norma_vector([(adicion[0].real, adicion[0].imag)])
    return norma
