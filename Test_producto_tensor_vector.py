import unittest
import Libreria.ProductoTensonrVectores

class test_producto_tensor_vector(unittest.TestCase):

    def test_tensor1(self):
        self.assertEqual(Libreria.ProductoTensonrVectores.producto_tencsor_vector([(2, 0), (3, 0)], [(4, 0), (6, 0), (3, 0)]), [(8+0j), (12+0j), (6+0j), (12+0j), (18+0j), (9+0j)])

    def test_tensor2(self):
        self.assertEqual(Libreria.ProductoTensonrVectores.producto_tencsor_vector([(2, 0), (-1, 0)],[(3, 0), (4, 0), (7, 0)]), [(6+0j), (8+0j), (14+0j), (-3+0j), (-4+0j), (-7+0j)])

    def test_tensor3(self):
        self.assertEqual(Libreria.ProductoTensonrVectores.producto_tencsor_vector([(4.0, 0), (-1.1, 0)],[(4.6, 9), (4.3, 7.2)]), [(18.4+36j), (17.2+28.8j), (-5.06-9.9j), (-4.73-7.920000000000001j)])

    def test_tensor4(self):
        self.assertEqual(Libreria.ProductoTensonrVectores.producto_tencsor_vector([(5.8, 4)], [(1, -1.0), (8, 7)]), [(9.8-1.7999999999999998j), (18.4+72.6j)])