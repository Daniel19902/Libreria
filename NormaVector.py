


def norma_vector(vector):
    return norma(vector)



def norma(vector):
    suma = 0
    for i in range(len(vector)):
        r = vector[i]
        for j in range(2):
            suma += r[j]**2
    return round((suma)**(1/2), 2)

