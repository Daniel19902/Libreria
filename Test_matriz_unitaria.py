import unittest
import Libreria.MatrizUnitaria

class test_matriz_unitaria(unittest.TestCase):

    def test_unitaraia(self):
        self.assertEqual(Libreria.MatrizUnitaria.matriz_unitaria([[(1, 0), (0, 0)], [(0, 0), (1, 0)]]), True)

    def test_unitaraia1(self):
        self.assertEqual(Libreria.MatrizUnitaria.matriz_unitaria([[(0, 1), (0, 0)], [(0, 0), (0, 1)]]), True)

    def test_unitaraia2(self):
        self.assertEqual(Libreria.MatrizUnitaria.matriz_unitaria([[(0, 0), (0, 1)], [(0, 1), (0, 0)]]), True)

    def test_unitaraia3(self):
        self.assertEqual(Libreria.MatrizUnitaria.matriz_unitaria([[(1, 1), (1, -1)], [(1, -1), (1, 1)]]), False)

    def test_unitaraia4(self):
        self.assertEqual(Libreria.MatrizUnitaria.matriz_unitaria([[(0, 1), (1, -8)], [(7, -1), (7, 1)]]), False)