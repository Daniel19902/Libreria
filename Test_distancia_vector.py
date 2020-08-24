import unittest
import Libreria.DistanciaVector

class test_distancia_vecctor(unittest.TestCase):

    def test_distacia_vector(self):
        self.assertEqual(Libreria.DistanciaVector.distancia_vectores([(3, 0), (1, 0), (2, 0)], [(2, 0), (2, 0), (-1, 0)]), 1.0)

    def test_distacia_vector1(self):
        self.assertEqual(Libreria.DistanciaVector.distancia_vectores([(3,-2)], [(-1, 3)]), 6.4)