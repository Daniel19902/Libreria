


def multiplicacionEscalar(escalar, vector):
    return multiplicar(escalar, vector)


def multiplicar(escalar, vector):
    multi = []
    for i in range(len(vector)):
        m = []
        for j in range(len(vector[i])):
            r = vector[i][j]
            m.append(complex(escalar[0], escalar[1]) * complex(r[0], r[1]))
        multi.append(m)
    return multi


