import unittest
import Libreria.ProductoInterno

class test_producto_interno(unittest.TestCase):

    def test_producto(self):
        self.assertEqual(Libreria.ProductoInterno.producto_interno([(1, 0), (0, 1), (1, -3)], [(2, 1), (0, 1), (2, 0)]), (5+7j))

    def test_producto1(self):
        self.assertEqual(Libreria.ProductoInterno.producto_interno([(-6, 8), (9, 8)], [(-6, -8), (9, -8)]), (-11-48j))

    def test_producto2(self):
        self.assertEqual(Libreria.ProductoInterno.producto_interno([(3.5, 9), (0, -8), (5, -9)], [(3.5, -9), (0, 8), (5, 9)]), (-188.75+27j))

    def test_vectorC4(self):
        self.assertEqual(Libreria.ProductoInterno.producto_interno([(1, -98), (-9, -9), (5, -10), (5, 10)],[(1, 98), (-9, 9), (5, 10), (5, -10)]), (-9753+34j))

    def test_vectorC5(self):
        self.assertEqual(Libreria.ProductoInterno.producto_interno([(-1, 98), (2, 87), (2, 8.9), (3, 5.6), (-100, 65)],[(-1, -98), (2, -87), (2, -8.9), (3, -5.6), (-100, -65)]), (-11490.57+12778.8j))