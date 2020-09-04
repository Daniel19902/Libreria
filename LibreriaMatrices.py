import numpy as np

"""
    Suma de vectores complejos------------------------------------------------------------------------------------------
"""
def adicion_de_vectores(vectorA, vectorB):
    return suma(vectorA, vectorB)


def suma(vectorA, vectorB):
    plus = []
    for i in range(len(vectorA)):
        a = vectorA[i]
        b = vectorB[i]
        plus.append(complex(a[0], a[1]) + complex(b[0], b[1]))
    return plus


"""
    Inverso (aditivo) de un vector complejo.----------------------------------------------------------------------------
"""
def inverso_aditivo_vector(vector):
    return inverso_vector(vector)



def inverso_vector(vector):

    for i in range(len(vector)):
        r = vector[i]
        vector[i] = (r[0]*-1, r[1]*-1)
    return vector


"""
    INVERSO (ADITIVO) MATRIZ--------------------------------------------------------------------------------------------
"""
def inverso_Aditivo_matriz(vector):
    vector = inverso_matriz(vector)
    return vector



def inverso_matriz(vector):

    for i in range(len(vector)):
        for j in range(len(vector[i])):
            r = vector[i][j]
            vector[i][j] = (r[0]*-1, r[1]*-1)
    return vector


"""
    Multiplicación de un escalar por un matriz complejo.----------------------------------------------------------------
"""
def multiplicacionEscalar(escalar, matriz):
    return multiplicar(escalar, matriz)


def multiplicar(escalar, matriz):
    multi = []
    for i in range(len(matriz)):
        m = []
        for j in range(len(matriz[i])):
            r = matriz[i][j]
            m.append(complex(escalar[0], escalar[1]) * complex(r[0], r[1]))
        multi.append(m)
    return multi

"""
    Adjunta matriz------------------------------------------------------------------------------------------------------
"""
def adgjunta_matriz(matriz):
    return convertir_adjunta_matriz(matriz)

def convertir_adjunta_matriz(matriz):
    matriz = transpuesta_matriz(matriz)
    matriz = conjudada_matriz(matriz)
    return matriz


"""
    Adjunta vector------------------------------------------------------------------------------------------------------
"""

def adjunta_vector(vector):
    return convertir(vector)

def convertir(vector):
    vector = vector_transpuesto(vector)
    vector = conjugada_vector(vector)
    return vector


"""
    Transpuesta vector--------------------------------------------------------------------------------------------------
"""

def vector_transpuesto(vector):
    return convertir_trasnpuesta_vector(vector)


def convertir_trasnpuesta_vector(vector):
    transpuesta = []
    for i in range(len(vector)):
        transpuesta.append(vector[i])
    return transpuesta


"""
    Transpuesta_matriz--------------------------------------------------------------------------------------------------
"""

def transpuesta_matriz(matriz):
    return convertir_transpuesta_matriz(matriz)


def convertir_transpuesta_matriz(matriz):
    trans = []
    longitud = 0
    while longitud < len(matriz[0]):
        a = []
        for i in range(len(matriz)):
            a.append(matriz[i][longitud])
        trans.append(a)
        longitud += 1
    return trans


"""
    conjugada matriz----------------------------------------------------------------------------------------------------
"""
def conjudada_matriz(matriz):
    matriz = convertir_conjugada_matriz(matriz)
    return matriz

def convertir_conjugada_matriz(matriz):

    conjugada = []
    for i in range(len(matriz)):
        a = []
        for j in range(len(matriz[i])):
            r = matriz[i][j]
            a.append((r[0], r[1]*-1))
        conjugada.append(a)

    return conjugada


"""
    CONJUGADA VECTOR----------------------------------------------------------------------------------------------------
"""
def conjugada_vector(vector):
    vector = convertir_conjugada_vector(vector)
    return vector

def convertir_conjugada_vector(vector):
    conjugada = []
    for i in range(len(vector)):
        r = vector[i]
        conjugada.append((r[0], r[1]*-1))
    return conjugada


"""
    Norma vector--------------------------------------------------------------------------------------------------------
"""
def norma_vector(vector):
    return convertir_norma_vector(vector)



def convertir_norma_vector(vector):
    suma = 0
    for i in range(len(vector)):
        r = vector[i]
        for j in range(2):
            suma += r[j]**2
    return round((suma)**(1/2), 2)


"""
    Distancia vector----------------------------------------------------------------------------------------------------
"""
def distancia_vectores(vectorA, vectorB):
    return calcular_distancia_vectores(vectorA, vectorB)


def calcular_distancia_vectores(vectorA, vectorB):
    for i in range(len(vectorB)):
        r = vectorB[i]
        vectorB[i] = (r[0]*-1, r[1]*-1)
    adicion = adicion_de_vectores(vectorA, vectorB)
    norma = norma_vector([(adicion[0].real, adicion[0].imag)])
    return norma


"""
    Matriz Hermitania---------------------------------------------------------------------------------------------------
"""

def matriz_hermitiana(matriz):
    adjunta = adgjunta_matriz(matriz)
    return comprobar_hermitania(matriz, adjunta)

def comprobar_hermitania(matriz, adjunta):
    if matriz == adjunta:
        return True
    return False


"""
    Matriz Unitaria-----------------------------------------------------------------------------------------------------
"""

def matriz_unitaria(matriz):
    matriz1 = adgjunta_matriz(matriz)
    return producto_unitaria(matriz, matriz1)


def producto_unitaria(matriz, matri1):
    resultado = multiplicacion_matrices(matriz, matri1)
    return comprobar_unitaria(resultado)


def comprobar_unitaria(resultado):
    matriz_u = np.identity(len(resultado))
    matriz_unitaria1 = []
    for i in range(len(matriz_u)):
        a = []
        for j in range(len(matriz_u[0])):
            a.append(complex(matriz_u[i][j]))
        matriz_unitaria1.append(a)
    if matriz_unitaria1 == resultado:
        return True
    return False


"""
    Multiplicacion matrices---------------------------------------------------------------------------------------------
"""

def multiplicacion_matrices(a, b):
    return calcular_multiplicacion(a, b)

def calcular_multiplicacion(a, b):

    producto = []
    for i in range(len(a)):
        multi = []
        for j in range(len(b[0])):
            suma = complex(0, 0)
            for x in range(len(a[i])):
                r = a[i][x]
                f = b[x][j]
                suma += complex(r[0], r[1]) * complex(f[0], f[1])
            multi.append(suma)
        producto.append(multi)
    return producto


"""
    Multiplicacion escalar vector---------------------------------------------------------------------------------------
"""
def multiplicacion_escalar_vector(escalar, vector):
    return calcular_multiplicacion_escalar_vector(escalar, vector)



def calcular_multiplicacion_escalar_vector(escalar, vector):
    multi = []
    for i in range(len(vector)):
        r = vector[i]
        multi.append(complex(escalar[0], escalar[1]) * complex(r[0], r[1]))
    return multi


"""
    PRODUCTO INTERNO----------------------------------------------------------------------------------------------------
"""

def producto_interno(vectorA, vectorB):
    vectorA = adjunta_vector(vectorA)
    return calcular_producto_interno(vectorA, vectorB)


def calcular_producto_interno(vectorA, vectorB):
    suma = complex(0, 0)
    for i in range(len(vectorA)):
        r = vectorA[i]
        f = vectorB[i]
        suma += complex(r[0], r[1]) * complex(f[0], f[1])
    return suma


"""
    Producto tensor vector----------------------------------------------------------------------------------------------
"""

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


"""
    Producto tensor matrices--------------------------------------------------------------------------------------------
"""

def producto_tensor_matrices(a, b):
    return calcualr_producto_tensor_matrices(a, b)

def calcualr_producto_tensor_matrices(matrizA, matrizB):

    tensor =[]
    for i in range(len(matrizA)):
        a = []
        for j in range(len(matrizA[i])):
            a.append(multiplicacionEscalar(matrizA[i][j], matrizB))
        tensor.append(a)
    return tensor

"""
    Suma de matrices
"""
def sumaDeMatrices (mV, mW):

    mV = complejo_matriz(mV)
    mW = complejo_matriz(mW)
    return suma_matriz(mV, mW)

def complejo_matriz(matrisV):
    matrizCompleja = []
    for i in range(len(matrisV)):
        a = []
        for j in range(len(matrisV[i])):
            r = matrisV[i][j]
            a.append(complex(float(r[0]), float(r[1])))
        matrizCompleja.append(a)

    return matrizCompleja

def suma_matriz(v, w):

    resultado = []
    for i in range(len(v)):
        for j in range(len(w[i])):
            resultado.append((v[i][j] + w[i][j]))

    return resultado
