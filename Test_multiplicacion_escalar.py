import unittest
import Libreria.MultiplicacionEscalar


class test_multiplicacion_escalar(unittest.TestCase):

    def test_multiplicacion1(self):
        self.assertEqual(Libreria.MultiplicacionEscalar.multiplicacionEscalar((3, 2), [[(6, 3)], [(0, 0)], [(5, 1)], [(4, 0)]]), [[(12+21j)], [0j], [(13+13j)], [(12+8j)]])

    def test_multiplicacion(self):
        self.assertEqual(Libreria.MultiplicacionEscalar.multiplicacionEscalar((-3, -2), [[(6, 3), (9, 1.0), (1.1, 4)], [(5, 1), (78, 9), (1.1, 4.4)]]), [[(-12-21j), (-25-21j), (4.699999999999999-14.2j)],[(-13-13j), (-216-183j), (5.5-15.400000000000002j)]])

    def test_multiplicacion2(self):
        self.assertEqual(Libreria.MultiplicacionEscalar.multiplicacionEscalar((10, 20), [[(6, 3), (9, 1.0)], [(5, 1), (78, 9)]]), [[150j, (70+190j)], [(30+110j), (600+1650j)]])

    def test_multiplicacion3(self):
        self.assertEqual(Libreria.MultiplicacionEscalar.multiplicacionEscalar((6, -4), [[(6, 3), (8, 9)], [(0, 0), (8, 8)], [(5, 1), (6, 7)], [(4, 0), (1.0, 1.1)]]), [[(48-6j), (84+22j)],[0j, (80+16j)],[(34-14j), (64+18j)],
 [(24-16j), (10.4+2.6000000000000005j)]])

    def test_multiplicacion4(self):
        self.assertEqual(Libreria.MultiplicacionEscalar.multiplicacionEscalar((-7, -9),[[(6, 3)], [(5, 1)]]), [[(-15-75j)], [(-26-52j)]])