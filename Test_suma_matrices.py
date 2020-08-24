import unittest
import Libreria.SumaDeMatrices

class test_multiplicacion_matrices(unittest.TestCase):

    def test_multiplicacion(self):
        self.assertEqual(Libreria.SumaDeMatrices.sumaDeMatrices([[(3, 2), (0, 0), (5, -6)], [(1, 0), (4, 2), (0, 1)], [(4, -1),(0, 0),(4, 0)]],[[(5, 0), (2, -1), (6, -4)], [(0, 0), (4, 5), (2, 0)], [(7, -4),(2, 7),(0, 0)]]), [(8+2j), (2-1j), (11-10j), (1+0j), (8+7j), (2+1j), (11-5j), (2+7j), (4+0j)])

    def test_multiplicacion1(self):
        self.assertEqual(Libreria.SumaDeMatrices.sumaDeMatrices([[(5, 0), (3, 0), (-4, 0), (-2, 0)], [(8, 0), (-1, 0), (0, 0), (-3, 0)]], [[(1, 0), (4, 0), (0, 0)], [(-5, 0), (3, 0), (7, 0)], [(0, 0), (-9, 0), (5, 0)], [(5, 0), (1, 0), (4, 0)]]), [(6+0j), (7+0j), (-4+0j), (3+0j), (2+0j), (7+0j)])

    def test_multiplicacion2(self):
        self.assertEqual(Libreria.SumaDeMatrices.sumaDeMatrices([[(-2, 0), (3, 0)]],[[(-5, 0), (1, 0)]]), [(-7+0j), (4+0j)])