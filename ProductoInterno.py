import Libreria.AdjuntaVector



def producto_interno(vectorA, vectorB):
    vectorA = Libreria.AdjuntaVector.adjunta_vector(vectorA)
    return producto(vectorA, vectorB)


def producto(vectorA, vectorB):
    suma = complex(0, 0)
    for i in range(len(vectorA)):
        r = vectorA[i]
        f = vectorB[i]
        suma += complex(r[0], r[1]) * complex(f[0], f[1])
    return suma

