import unittest
import Libreria.AdjuntaMatriz

class Testadjuntamatriz(unittest.TestCase):

    def test_matrizC1x1(self):
        self.assertEqual(Libreria.AdjuntaMatriz.adgjunta_matriz([[(6, 3)], [(5, 1)]]), [[(6, -3), (5, -1)]])

    def test_matrizC1x4(self):
        self.assertEqual(Libreria.AdjuntaMatriz.adgjunta_matriz([[(6, 3)], [(0, 0)], [(5, 1)], [(4, 0)]]), [[(6, -3), (0, 0), (5, -1), (4, 0)]])

    def test_matrizC2x4(self):
        self.assertEqual(Libreria.AdjuntaMatriz.adgjunta_matriz([[(6, 3), (8, 9)], [(0, 0), (8, 8)], [(5, 1), (6, 7)], [(4, 0), (1.0, 1.1)]]), [[(6, -3), (0, 0), (5, -1), (4, 0)], [(8, -9), (8, -8), (6, -7), (1.0, -1.1)]])

    def test_matrizC2x2(self):
        self.assertEqual(Libreria.AdjuntaMatriz.adgjunta_matriz([[(6, 3), (9, 1.0)], [(5, 1), (78, 9)]]), [[(6, -3), (5, -1)], [(9, -1.0), (78, -9)]])

    def test_matrizC3x3(self):
        self.assertEqual(Libreria.AdjuntaMatriz.adgjunta_matriz([[(6, 3), (9, 1.0), (1.1, 4)], [(5, 1), (78, 9), (1.1, 4.4)]]), [[(6, -3), (5, -1)], [(9, -1.0), (78, -9)], [(1.1, -4), (1.1, -4.4)]])

