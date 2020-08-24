import unittest
import Libreria.InversoAditivoVector

class test_inverso_aditivo_vector(unittest.TestCase):

    def test_vectorC1(self):
        self.assertEqual(Libreria.InversoAditivoVector.inverso_aditivo_vector([(1, 98)]), [(-1, -98)])

    def test_vectorC2(self):
        self.assertEqual(Libreria.InversoAditivoVector.inverso_aditivo_vector([(-6, 8), (9, 8)]), [(6, -8), (-9, -8)] )

    def test_vectorC3(self):
        self.assertEqual(Libreria.InversoAditivoVector.inverso_aditivo_vector([(3.5, 9), (0, -8), (5, -9)]), [(-3.5, -9), (0, 8), (-5, 9)])

    def test_vectorC4(self):
        self.assertEqual(Libreria.InversoAditivoVector.inverso_aditivo_vector([(1, -98),  (-9, -9),  (5, -10),  (5, 10)]), [(-1, 98),  (9, 9),  (-5, 10),  (-5, -10)])

    def test_vectorC5(self):
        self.assertEqual(Libreria.InversoAditivoVector.inverso_aditivo_vector([(-1, 98), (2, 87), (2, 8.9), (3, 5.6), (-100, 65)]), [(1, -98), (-2, -87), (-2, -8.9), (-3, -5.6), (100, -65)])
