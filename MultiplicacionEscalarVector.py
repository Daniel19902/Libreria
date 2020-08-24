


def multiplicacion_escalar_vector(escalar, vector):
    return multiplicacion(escalar, vector)



def multiplicacion(escalar, vector):
    multi = []
    for i in range(len(vector)):
        r = vector[i]
        multi.append(complex(escalar[0], escalar[1]) * complex(r[0], r[1]))
    return multi



