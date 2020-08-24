import Libreria.TranspuestaVector
import Libreria.ConjugadaVector


def adjunta_vector(vector):
    return convertir(vector)

def convertir(vector):
    vector = Libreria.TranspuestaVector.vector_transpuesto(vector)
    vector = Libreria.ConjugadaVector.conjugada_vector(vector)
    return vector

