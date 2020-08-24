

def multiplicacion_matrices(a, b):
    return multiplicacion(a, b)

def multiplicacion(a, b):

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

