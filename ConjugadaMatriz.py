


def conjudada_matriz(matriz):
    matriz = convertir(matriz)
    return matriz

def convertir(matriz):

    conjugada = []
    for i in range(len(matriz)):
        a = []
        for j in range(len(matriz[i])):
            r = matriz[i][j]
            a.append((r[0], r[1]*-1))
        conjugada.append(a)

    return conjugada

