



def inversoAditivo(vector):
    vector = inverso(vector)
    return vector



def inverso(vector):

    for i in range(len(vector)):
        for j in range(len(vector[i])):
            r = vector[i][j]
            vector[i][j] = (r[0]*-1, r[1]*-1)
    return vector

