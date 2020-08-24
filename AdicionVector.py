

def adicion_de_vectores(vectorA, vectorB):
    return suma(vectorA, vectorB)


def suma(vectorA, vectorB):
    plus = []
    for i in range(len(vectorA)):
        a = vectorA[i]
        b = vectorB[i]
        plus.append(complex(a[0], a[1]) + complex(b[0], b[1]))
    return plus

