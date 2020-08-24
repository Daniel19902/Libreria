import unittest
import Libreria.NormaVector

class test_norma_vector(unittest.TestCase):

    def test_norma1(self):
        self.assertEqual(Libreria.NormaVector.norma_vector([(8.8, 8.6), (3.9, -6.0)]), 14.23)

    def test_norma2(self):
        self.assertEqual(Libreria.NormaVector.norma_vector([(-6, 8), (9, 8)]), 15.65)

    def test_norma3(self):
        self.assertEqual(Libreria.NormaVector.norma_vector([(1, -98),  (-9, -9),  (5, -10),  (5, 10)]), 100.08)

    def test_norma4(self):
        self.assertEqual(Libreria.NormaVector.norma_vector([(-1, 98), (2, 87), (2, 8.9), (3, 5.6), (-100, 65)]), 177.56)

    def test_norma5(self):
        self.assertEqual(Libreria.NormaVector.norma_vector([(1, 98)]), 98.01)