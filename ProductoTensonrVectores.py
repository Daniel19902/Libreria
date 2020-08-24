


def producto_tencsor_vector(vectorA, vectorB):
    return producto(vectorA, vectorB)



def producto(vectorA, vectorB):
    tensor = []
    for i in range(len(vectorA)):
        for j in range(len(vectorB)):
            r = vectorA[i]
            f = vectorB[j]
            tensor.append(complex(r[0], r[1]) * complex(f[0], f[1]))
    return tensor







