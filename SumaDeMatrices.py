import Libreria.InversoAditivo

def sumaDeMatrices (mV, mW):

    mV = complejo(mV)
    mW = complejo(mW)
    return suma(mV, mW)

def complejo(matrisV):
    matrizCompleja = []
    for i in range(len(matrisV)):
        a = []
        for j in range(len(matrisV[i])):
            r = matrisV[i][j]
            a.append(complex(float(r[0]), float(r[1])))
        matrizCompleja.append(a)

    return matrizCompleja

def suma(v, w):

    resultado = []
    for i in range(len(v)):
        for j in range(len(w[i])):
            resultado.append((v[i][j] + w[i][j]))

    return resultado

