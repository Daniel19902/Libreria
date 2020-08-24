import unittest
import Libreria.AdicionVector



class Testadicionsuma(unittest.TestCase):

    def test_vectorC1(self):
        self.assertEqual(Libreria.AdicionVector.adicion_de_vectores([(1, 0)], [(7, 8)]), [(8 + 8j)])

    def test_vectorC2(self):
        self.assertEqual(Libreria.AdicionVector.adicion_de_vectores([(1, 0), (4.8, 9)], [(7, 8), (1.1, 9)]), [(8 + 8j), (5.9 + 18j)])

    def test_vectorC3(self):
        self.assertEqual(Libreria.AdicionVector.adicion_de_vectores([(1, 0), (4.8, 9), (8.9, 9)], [(-1, 0), (-4.8, -9), (-8.9, -9)]), [0j, 0j, 0j])

    def test_vectorC4(self):
        self.assertEqual(Libreria.AdicionVector.adicion_de_vectores([(6, -4), (7, 3), (4.2, -8.1), (0, -3)], [(16, 2.3), (0, -7), (6, 0), (0, -4)]), [(22-1.7000000000000002j), (7-4j), (10.2-8.1j), -7j])

    def test_vectorC5(self):
        self.assertEqual(Libreria.AdicionVector.adicion_de_vectores([(6, 4), (7, 3), (4.2, -8.1), (0, -3), (5.5, 8)], [(16, 2.3), (0, -7), (6, 0), (0, -4), (8, 9)]), [(22+6.3j), (7-4j), (10.2-8.1j), -7j, (13.5+17j)])