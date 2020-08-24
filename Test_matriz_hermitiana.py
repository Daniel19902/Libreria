import unittest
import Libreria.MatrizHermitiana

class test_matriz_hermitiana(unittest.TestCase):

    def test_hermitiana1(self):
        self.assertEqual(Libreria.MatrizHermitiana.matriz_hermitiana([[(2, 0), (1, 1)], [(1, -1), (3, 0)]]), True)
    def test_hermitiana2(self):
        self.assertEqual(Libreria.MatrizHermitiana.matriz_hermitiana([[(5, 0), (3, 7)], [(3, -7), (2, 0)]]), True)
    def test_hermitiana3(self):
        self.assertEqual(Libreria.MatrizHermitiana.matriz_hermitiana([[(2, 0), (1, 1), (9, 2), (0, 0)],
                                                                      [(1, -1), (5, 0),(4, 6), (3, -2)],
                                                                      [(9, -2), (4, -6), (10, 0), (1, 7)],
                                                                      [(0, 0), (3, 2), (1, -7), (4, 0)]]), True)

    def test_hermitiana4(self):
        self.assertEqual(Libreria.MatrizHermitiana.matriz_hermitiana([[(2, 5), (4, 1)], [(10, -1), (3, 9)]]), False)
    def test_hermitiana5(self):
        self.assertEqual(Libreria.MatrizHermitiana.matriz_hermitiana([[(5, 5), (3, 7)], [(30, 7), (8, 0)]]), False)