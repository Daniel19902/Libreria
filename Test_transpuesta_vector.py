import unittest
import Libreria.TranspuestaVector

class test_transpuesta_vector(unittest.TestCase):

    def test_transpuesta(self):
        self.assertEqual(Libreria.TranspuestaVector.vector_transpuesto([(8.8, 8.6), (3.9, -6.0)]), [(8.8, 8.6), (3.9, -6.0)])

    def test_transpuesta1(self):
        self.assertEqual(Libreria.TranspuestaVector.vector_transpuesto([(-6, 8), (9, 8)]), [(-6, 8), (9, 8)])

    def test_transpuesta2(self):
        self.assertEqual(Libreria.TranspuestaVector.vector_transpuesto([(1, -98),  (-9, -9),  (5, -10),  (5, 10)]), [(1, -98),  (-9, -9),  (5, -10),  (5, 10)])

    def test_transpuesta3(self):
        self.assertEqual(Libreria.TranspuestaVector.vector_transpuesto([(-1, 98), (2, 87), (2, 8.9), (3, 5.6), (-100, 65)]), [(-1, 98), (2, 87), (2, 8.9), (3, 5.6), (-100, 65)])

    def test_transpuesta4(self):
        self.assertEqual(Libreria.TranspuestaVector.vector_transpuesto([(1, 98)]), [(1, 98)])