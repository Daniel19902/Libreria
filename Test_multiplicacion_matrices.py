import unittest
import Libreria.MultiplicacionMatrices

class test_multiplicacion_matrices(unittest.TestCase):

    def test_multiplicacion(self):
        self.assertEqual(Libreria.MultiplicacionMatrices.multiplicacion_matrices([[(3, 2), (0, 0), (5, -6)], [(1, 0), (4, 2), (0, 1)], [(4, -1),(0, 0),(4, 0)]],[[(5, 0), (2, -1), (6, -4)], [(0, 0), (4, 5), (2, 0)], [(7, -4),(2, 7),(0, 0)]]), [[(26-52j), (60+24j), (26+0j)],[(9+7j), (1+29j), (14+0j)],[(48-21j), (15+22j), (20-22j)]])

    def test_multiplicacion1(self):
        self.assertEqual(Libreria.MultiplicacionMatrices.multiplicacion_matrices([[(5, 0), (3, 0), (-4, 0), (-2, 0)], [(8, 0), (-1, 0), (0, 0), (-3, 0)]], [[(1, 0), (4, 0), (0, 0)], [(-5, 0), (3, 0), (7, 0)], [(0, 0), (-9, 0), (5, 0)], [(5, 0), (1, 0), (4, 0)]]), [[(-20+0j), (63+0j), (-7+0j)], [(-2+0j), (26+0j), (-19+0j)]])

    def test_multiplicacion2(self):
        self.assertEqual(Libreria.MultiplicacionMatrices.multiplicacion_matrices([[(-2, 0), (3, 0)], [(-5, 0), (1, 0)], [(0, 0), (-6, 0)]], [[(1, 0), (-5, 0), (0, 0)], [(-8, 0), (9, 0), (2, 0)]]), [[(-26+0j), (37+0j), (6+0j)],[(-13+0j), (34+0j), (2+0j)],[(48+0j), (-54+0j), (-12+0j)]])