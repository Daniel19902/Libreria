


def inverso_aditivo_vector(vector):
    return inverso(vector)



def inverso(vector):

    for i in range(len(vector)):
        r = vector[i]
        vector[i] = complex(r[0]*-1, r[1]*-1)
    return vector


