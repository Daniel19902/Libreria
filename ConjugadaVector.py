


def conjugada_vector(vector):
    vector = convertir(vector)
    return vector

def convertir(vector):
    conjugada = []
    for i in range(len(vector)):
        r = vector[i]
        conjugada.append((r[0], r[1]*-1))
    return conjugada

