import unittest
import Libreria.Transpuestas

class test_transpuesta(unittest.TestCase):

    def test_transpuesta1(self):
        self.assertEqual(Libreria.Transpuestas.transpuesta([[(6, -4)],[(7,3)],[(4.2,-8.1)],[(0,-3)]]), [[(6, -4), (7, 3), (4.2, -8.1), (0, -3)]])

    def test_transpuesta2(self):
        self.assertEqual(Libreria.Transpuestas.transpuesta([[(16, 2.3)],[(0,-7)],[(6,0)],[(0,-4)]]), [[(16, 2.3), (0, -7), (6, 0), (0, -4)]])

    def test_transpuesta3(self):
        self.assertEqual(Libreria.Transpuestas.transpuesta([[(5, 8), (-2.7, 9), (8, 9.8)], [(7, 9), (1, 8), (0, 3)], [(-4, 10), (-7, 14), (-6, 48)]]), [[(5, 8), (7, 9), (-4, 10)],[(-2.7, 9), (1, 8), (-7, 14)],[(8, 9.8), (0, 3), (-6, 48)]])

    def test_transpuesta4(self):
        self.assertEqual(Libreria.Transpuestas.transpuesta([[(1, 1), (0, 10), (-5, -8), (6, 9)], [(2, 1.1), (8, 9), (4, 7), (-9, 10)]]), [[(1, 1), (2, 1.1)], [(0, 10), (8, 9)], [(-5, -8), (4, 7)], [(6, 9), (-9, 10)]])

    def test_transpuesta5(self):
        self.assertEqual(Libreria.Transpuestas.transpuesta([[(6, 3)], [(0, 0)], [(5, 1)], [(4, 0)]]), [[(6, 3), (0, 0), (5, 1), (4, 0)]])