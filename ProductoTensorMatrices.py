import Libreria.MultiplicacionEscalar



def producto_tensor_matrices(a, b):
    return producto(a, b)

def producto(matrizA, matrizB):

    tensor =[]
    for i in range(len(matrizA)):
        a = []
        for j in range(len(matrizA[i])):
            a.append(Libreria.MultiplicacionEscalar.multiplicacionEscalar(matrizA[i][j], matrizB))
        tensor.append(a)
    return tensor








