

def transpuesta(matriz):
    return convertir(matriz)


def convertir(matriz):
    trans = []
    longitud = 0
    while longitud < len(matriz[0]):
        a = []
        for i in range(len(matriz)):
            a.append(matriz[i][longitud])
        trans.append(a)
        longitud += 1
    return trans


