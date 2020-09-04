import unittest
import LibreriaMatrices

class TestLibreriaMatrices(unittest.TestCase):

    def test_adicion_vectores(self):
        self.assertEqual(LibreriaMatrices.adicion_de_vectores([(1, 0)], [(7, 8)]), [(8 + 8j)])
        self.assertEqual(LibreriaMatrices.adicion_de_vectores([(1, 0), (4.8, 9)], [(7, 8), (1.1, 9)]),[(8 + 8j), (5.9 + 18j)])
        self.assertEqual(LibreriaMatrices.adicion_de_vectores([(1, 0), (4.8, 9), (8.9, 9)], [(-1, 0), (-4.8, -9), (-8.9, -9)]),[0j, 0j, 0j])
        self.assertEqual(LibreriaMatrices.adicion_de_vectores([(6, -4), (7, 3), (4.2, -8.1), (0, -3)],[(16, 2.3), (0, -7), (6, 0), (0, -4)]),[(22 - 1.7000000000000002j), (7 - 4j), (10.2 - 8.1j), -7j])
        self.assertEqual(LibreriaMatrices.adicion_de_vectores([(6, 4), (7, 3), (4.2, -8.1), (0, -3), (5.5, 8)],[(16, 2.3), (0, -7), (6, 0), (0, -4), (8, 9)]),[(22 + 6.3j), (7 - 4j), (10.2 - 8.1j), -7j, (13.5 + 17j)])

    def test_inverso_aditivo_matriz(self):
        self.assertEqual(LibreriaMatrices.inverso_Aditivo_matriz([[(6, 3)], [(5, 1)]]),[[(-6, -3)], [(-5, -1)]])
        self.assertEqual(LibreriaMatrices.inverso_Aditivo_matriz([[(6, 3)], [(0, 0)], [(5, 1)], [(4, 0)]]),[[(-6, -3)], [(0, 0)], [(-5, -1)], [(-4, 0)]])
        self.assertEqual(LibreriaMatrices.inverso_Aditivo_matriz([[(6, 3), (8, 9)], [(0, 0), (8, 8)], [(5, 1), (6, 7)], [(4, 0), (1.0, 1.1)]]),[[(-6, -3), (-8, -9)], [(0, 0), (-8, -8)], [(-5, -1), (-6, -7)], [(-4, 0), (-1.0, -1.1)]])
        self.assertEqual(LibreriaMatrices.inverso_Aditivo_matriz([[(6, 3), (9, 1.0)], [(5, 1), (78, 9)]]),[[(-6, -3), (-9, -1.0)], [(-5, -1), (-78, -9)]])
        self.assertEqual(LibreriaMatrices.inverso_Aditivo_matriz([[(6, 3), (9, 1.0), (1.1, 4)], [(5, 1), (78, 9), (1.1, 4.4)]]),[[(-6, -3), (-9, -1.0), (-1.1, -4)], [(-5, -1), (-78, -9), (-1.1, -4.4)]])

    def test_inverso_aditivo_vector(self):
        self.assertEqual(LibreriaMatrices.inverso_aditivo_vector([(1, 98)]), [(-1, -98)])
        self.assertEqual(LibreriaMatrices.inverso_aditivo_vector([(-6, 8), (9, 8)]), [(6, -8), (-9, -8)])
        self.assertEqual(LibreriaMatrices.inverso_aditivo_vector([(3.5, 9), (0, -8), (5, -9)]),[(-3.5, -9), (0, 8), (-5, 9)])
        self.assertEqual(LibreriaMatrices.inverso_aditivo_vector([(1, -98),  (-9, -9),  (5, -10),  (5, 10)]), [(-1, 98),  (9, 9),  (-5, 10),  (-5, -10)])
        self.assertEqual(LibreriaMatrices.inverso_aditivo_vector([(-1, 98), (2, 87), (2, 8.9), (3, 5.6), (-100, 65)]),[(1, -98), (-2, -87), (-2, -8.9), (-3, -5.6), (100, -65)])

    def test_adjunta_vector(self):
        self.assertEqual(LibreriaMatrices.adjunta_vector([(1, 98)]), [(1, -98)])
        self.assertEqual(LibreriaMatrices.adjunta_vector([(-6, 8), (9, 8)]), [(-6, -8), (9, -8)])
        self.assertEqual(LibreriaMatrices.adjunta_vector([(3.5, 9), (0, -8), (5, -9)]),[(3.5, -9), (0, 8), (5, 9)])
        self.assertEqual(LibreriaMatrices.adjunta_vector([(1, -98), (-9, -9), (5, -10), (5, 10)]),[(1, 98), (-9, 9), (5, 10), (5, -10)])
        self.assertEqual(LibreriaMatrices.adjunta_vector([(-1, 98), (2, 87), (2, 8.9), (3, 5.6), (-100, 65)]),[(-1, -98), (2, -87), (2, -8.9), (3, -5.6), (-100, -65)])

    def test_adjunta_matriz(self):
        self.assertEqual(LibreriaMatrices.adgjunta_matriz([[(6, 3)], [(5, 1)]]), [[(6, -3), (5, -1)]])
        self.assertEqual(LibreriaMatrices.adgjunta_matriz([[(6, 3)], [(0, 0)], [(5, 1)], [(4, 0)]]),[[(6, -3), (0, 0), (5, -1), (4, 0)]])
        self.assertEqual(LibreriaMatrices.adgjunta_matriz([[(6, 3)], [(0, 0)], [(5, 1)], [(4, 0)]]),[[(6, -3), (0, 0), (5, -1), (4, 0)]])
        self.assertEqual(LibreriaMatrices.adgjunta_matriz([[(6, 3), (9, 1.0)], [(5, 1), (78, 9)]]),[[(6, -3), (5, -1)], [(9, -1.0), (78, -9)]])
        self.assertEqual(LibreriaMatrices.adgjunta_matriz([[(6, 3), (9, 1.0), (1.1, 4)], [(5, 1), (78, 9), (1.1, 4.4)]]),[[(6, -3), (5, -1)], [(9, -1.0), (78, -9)], [(1.1, -4), (1.1, -4.4)]])

    def test_transpuesta_vector(self):
        self.assertEqual(LibreriaMatrices.vector_transpuesto([(8.8, 8.6), (3.9, -6.0)]),[(8.8, 8.6), (3.9, -6.0)])
        self.assertEqual(LibreriaMatrices.vector_transpuesto([(-6, 8), (9, 8)]), [(-6, 8), (9, 8)])
        self.assertEqual(LibreriaMatrices.vector_transpuesto([(1, -98), (-9, -9), (5, -10), (5, 10)]),[(1, -98), (-9, -9), (5, -10), (5, 10)])
        self.assertEqual(LibreriaMatrices.vector_transpuesto([(-1, 98), (2, 87), (2, 8.9), (3, 5.6), (-100, 65)]),[(-1, 98), (2, 87), (2, 8.9), (3, 5.6), (-100, 65)])
        self.assertEqual(LibreriaMatrices.vector_transpuesto([(1, 98)]), [(1, 98)])

    def test_transpuesta_matriz(self):
        self.assertEqual(LibreriaMatrices.transpuesta_matriz([[(6, -4)], [(7, 3)], [(4.2, -8.1)], [(0, -3)]]),[[(6, -4), (7, 3), (4.2, -8.1), (0, -3)]])
        self.assertEqual(LibreriaMatrices.transpuesta_matriz([[(16, 2.3)], [(0, -7)], [(6, 0)], [(0, -4)]]),[[(16, 2.3), (0, -7), (6, 0), (0, -4)]])
        self.assertEqual(LibreriaMatrices.transpuesta_matriz([[(5, 8), (-2.7, 9), (8, 9.8)], [(7, 9), (1, 8), (0, 3)], [(-4, 10), (-7, 14), (-6, 48)]]),[[(5, 8), (7, 9), (-4, 10)], [(-2.7, 9), (1, 8), (-7, 14)], [(8, 9.8), (0, 3), (-6, 48)]])
        self.assertEqual(LibreriaMatrices.transpuesta_matriz([[(1, 1), (0, 10), (-5, -8), (6, 9)], [(2, 1.1), (8, 9), (4, 7), (-9, 10)]]),[[(1, 1), (2, 1.1)], [(0, 10), (8, 9)], [(-5, -8), (4, 7)], [(6, 9), (-9, 10)]])
        self.assertEqual(LibreriaMatrices.transpuesta_matriz([[(6, 3)], [(0, 0)], [(5, 1)], [(4, 0)]]),[[(6, 3), (0, 0), (5, 1), (4, 0)]])


    def test_conjugada_matriz(self):
        self.assertEqual(LibreriaMatrices.conjudada_matriz([[(6, 3)], [(5, 1)]]),[[(6, -3)], [(5, -1)]])
        self.assertEqual(LibreriaMatrices.conjudada_matriz([[(6, 3)], [(0, 0)], [(5, 1)], [(4, 0)]]),[[(6, -3)], [(0, 0)], [(5, -1)], [(4, 0)]])
        self.assertEqual(LibreriaMatrices.conjudada_matriz([[(6, 3), (8, 9)], [(0, 0), (8, 8)], [(5, 1), (6, 7)], [(4, 0), (1.0, 1.1)]]),[[(6, -3), (8, -9)], [(0, 0), (8, -8)], [(5, -1), (6, -7)], [(4, 0), (1.0, -1.1)]])
        self.assertEqual(LibreriaMatrices.conjudada_matriz([[(6, 3), (9, 1.0)], [(5, 1), (78, 9)]]),[[(6, -3), (9, -1.0)], [(5, -1), (78, -9)]])
        self.assertEqual(LibreriaMatrices.conjudada_matriz([[(6, 3), (9, 1.0), (1.1, 4)], [(5, 1), (78, 9), (1.1, 4.4)]]),[[(6, -3), (9, -1.0), (1.1, -4)], [(5, -1), (78, -9), (1.1, -4.4)]])

    def test_conjugada_vector(self):
        self.assertEqual(LibreriaMatrices.conjugada_vector([(1, 98)]), [(1, -98)])
        self.assertEqual(LibreriaMatrices.conjugada_vector([(-6, 8), (9, 8)]), [(-6, -8), (9, -8)])
        self.assertEqual(LibreriaMatrices.conjugada_vector([(3.5, 9), (0, -8), (5, -9)]),[(3.5, -9), (0, 8), (5, 9)])
        self.assertEqual(LibreriaMatrices.conjugada_vector([(1, -98), (-9, -9), (5, -10), (5, 10)]),[(1, 98), (-9, 9), (5, 10), (5, -10)])
        self.assertEqual(LibreriaMatrices.conjugada_vector([(-1, 98), (2, 87), (2, 8.9), (3, 5.6), (-100, 65)]),[(-1, -98), (2, -87), (2, -8.9), (3, -5.6), (-100, -65)])

    def test_norma_vector(self):
        self.assertEqual(LibreriaMatrices.norma_vector([(8.8, 8.6), (3.9, -6.0)]), 14.23)
        self.assertEqual(LibreriaMatrices.norma_vector([(-6, 8), (9, 8)]), 15.65)
        self.assertEqual(LibreriaMatrices.norma_vector([(1, -98), (-9, -9), (5, -10), (5, 10)]), 100.08)
        self.assertEqual(LibreriaMatrices.norma_vector([(-1, 98), (2, 87), (2, 8.9), (3, 5.6), (-100, 65)]), 177.56)
        self.assertEqual(LibreriaMatrices.norma_vector([(1, 98)]), 98.01)

    def test_distancia_vector(self):
        self.assertEqual(LibreriaMatrices.distancia_vectores([(3, 0), (1, 0), (2, 0)], [(2, 0), (2, 0), (-1, 0)]), 1.0)
        self.assertEqual(LibreriaMatrices.distancia_vectores([(3, -2)], [(-1, 3)]), 6.4)

    def test_matriz_hermitania(self):
        self.assertEqual(LibreriaMatrices.matriz_hermitiana([[(2, 0), (1, 1)], [(1, -1), (3, 0)]]), True)
        self.assertEqual(LibreriaMatrices.matriz_hermitiana([[(5, 0), (3, 7)], [(3, -7), (2, 0)]]), True)
        self.assertEqual(LibreriaMatrices.matriz_hermitiana([[(2, 0), (1, 1), (9, 2), (0, 0)],[(1, -1), (5, 0), (4, 6), (3, -2)],[(9, -2), (4, -6), (10, 0), (1, 7)],[(0, 0), (3, 2), (1, -7), (4, 0)]]), True)
        self.assertEqual(LibreriaMatrices.matriz_hermitiana([[(2, 5), (4, 1)], [(10, -1), (3, 9)]]), False)
        self.assertEqual(LibreriaMatrices.matriz_hermitiana([[(5, 5), (3, 7)], [(30, 7), (8, 0)]]), False)

    def test_matriz_unitaria(self):
        self.assertEqual(LibreriaMatrices.matriz_unitaria([[(1, 0), (0, 0)], [(0, 0), (1, 0)]]), True)
        self.assertEqual(LibreriaMatrices.matriz_unitaria([[(0, 1), (0, 0)], [(0, 0), (0, 1)]]), True)
        self.assertEqual(LibreriaMatrices.matriz_unitaria([[(0, 0), (0, 1)], [(0, 1), (0, 0)]]), True)
        self.assertEqual(LibreriaMatrices.matriz_unitaria([[(1, 1), (1, -1)], [(1, -1), (1, 1)]]), False)
        self.assertEqual(LibreriaMatrices.matriz_unitaria([[(0, 1), (1, -8)], [(7, -1), (7, 1)]]), False)

    def test_multiplicacion_matrices(self):
        self.assertEqual(LibreriaMatrices.multiplicacion_matrices([[(3, 2), (0, 0), (5, -6)], [(1, 0), (4, 2), (0, 1)], [(4, -1), (0, 0), (4, 0)]],[[(5, 0), (2, -1), (6, -4)], [(0, 0), (4, 5), (2, 0)], [(7, -4), (2, 7), (0, 0)]]),[[(26 - 52j), (60 + 24j), (26 + 0j)], [(9 + 7j), (1 + 29j), (14 + 0j)],[(48 - 21j), (15 + 22j), (20 - 22j)]])
        self.assertEqual(LibreriaMatrices.multiplicacion_matrices([[(5, 0), (3, 0), (-4, 0), (-2, 0)], [(8, 0), (-1, 0), (0, 0), (-3, 0)]],[[(1, 0), (4, 0), (0, 0)], [(-5, 0), (3, 0), (7, 0)], [(0, 0), (-9, 0), (5, 0)], [(5, 0), (1, 0), (4, 0)]]),[[(-20 + 0j), (63 + 0j), (-7 + 0j)], [(-2 + 0j), (26 + 0j), (-19 + 0j)]])
        self.assertEqual(LibreriaMatrices.multiplicacion_matrices([[(-2, 0), (3, 0)], [(-5, 0), (1, 0)], [(0, 0), (-6, 0)]],[[(1, 0), (-5, 0), (0, 0)], [(-8, 0), (9, 0), (2, 0)]]),[[(-26 + 0j), (37 + 0j), (6 + 0j)], [(-13 + 0j), (34 + 0j), (2 + 0j)],[(48 + 0j), (-54 + 0j), (-12 + 0j)]])

    def test_multiplicacion_escalar_matriz(self):
        self.assertEqual(LibreriaMatrices.multiplicacionEscalar((3, 2), [[(6, 3)], [(0, 0)], [(5, 1)], [(4, 0)]]),[[(12 + 21j)], [0j], [(13 + 13j)], [(12 + 8j)]])
        self.assertEqual(LibreriaMatrices.multiplicacionEscalar((-3, -2), [[(6, 3), (9, 1.0), (1.1, 4)],[(5, 1), (78, 9),(1.1, 4.4)]]),[[(-12 - 21j), (-25 - 21j), (4.699999999999999 - 14.2j)],[(-13 - 13j), (-216 - 183j), (5.5 - 15.400000000000002j)]])
        self.assertEqual(LibreriaMatrices.multiplicacionEscalar((10, 20), [[(6, 3), (9, 1.0)], [(5, 1), (78, 9)]]),[[150j, (70 + 190j)], [(30 + 110j), (600 + 1650j)]])
        self.assertEqual(LibreriaMatrices.multiplicacionEscalar((6, -4),[[(6, 3), (8, 9)], [(0, 0), (8, 8)],[(5, 1), (6, 7)], [(4, 0), (1.0, 1.1)]]),[[(48 - 6j), (84 + 22j)], [0j, (80 + 16j)], [(34 - 14j), (64 + 18j)],[(24 - 16j), (10.4 + 2.6000000000000005j)]])
        self.assertEqual(LibreriaMatrices.multiplicacionEscalar((-7, -9), [[(6, 3)], [(5, 1)]]),[[(-15 - 75j)], [(-26 - 52j)]])

    def test_multiplicacion_escalar_vector(self):
        self.assertEqual(LibreriaMatrices.multiplicacion_escalar_vector((3, 2),[(6, 3), (0, 0), (5, 1),(4, 0)]),[(12 + 21j), 0j, (13 + 13j), (12 + 8j)])
        self.assertEqual(LibreriaMatrices.multiplicacion_escalar_vector((-3, -2),[(6, 3), (9, 1.0), (1.1, 4),(5, 1), (78, 9),(1.1, 4.4)]),[(-12 - 21j), (-25 - 21j), (4.699999999999999 - 14.2j), (-13 - 13j), (-216 - 183j),(5.5 - 15.400000000000002j)])
        self.assertEqual(LibreriaMatrices.multiplicacion_escalar_vector((10, 20),[(6, 3), (9, 1.0), (5, 1),(78, 9)]),[150j, (70 + 190j), (30 + 110j), (600 + 1650j)])
        self.assertEqual(LibreriaMatrices.multiplicacion_escalar_vector((6, -4),[(6, 3), (8, 9), (0, 0),(8, 8), (5, 1), (6, 7),(4, 0), (1.0, 1.1)]),[(48 - 6j), (84 + 22j), 0j, (80 + 16j), (34 - 14j), (64 + 18j), (24 - 16j),(10.4 + 2.6000000000000005j)])
        self.assertEqual(LibreriaMatrices.multiplicacion_escalar_vector((-7, -9), [(6, 3), (5, 1)]),[(-15 - 75j), (-26 - 52j)])

    def test_producto_interno(self):
        self.assertEqual(LibreriaMatrices.producto_interno([(1, 0), (0, 1), (1, -3)], [(2, 1), (0, 1), (2, 0)]),(5 + 7j))
        self.assertEqual(LibreriaMatrices.producto_interno([(-6, 8), (9, 8)], [(-6, -8), (9, -8)]), (-11 - 48j))
        self.assertEqual(LibreriaMatrices.producto_interno([(3.5, 9), (0, -8), (5, -9)], [(3.5, -9), (0, 8), (5, 9)]),(-188.75 + 27j))
        self.assertEqual(LibreriaMatrices.producto_interno([(1, -98), (-9, -9), (5, -10), (5, 10)],[(1, 98), (-9, 9), (5, 10), (5, -10)]),(-9753 + 34j))
        self.assertEqual(LibreriaMatrices.producto_interno([(-1, 98), (2, 87), (2, 8.9), (3, 5.6), (-100, 65)],[(-1, -98), (2, -87), (2, -8.9), (3, -5.6),(-100, -65)]), (-11490.57 + 12778.8j))

    def test_producto_tensor_vector(self):
        self.assertEqual(LibreriaMatrices.producto_tencsor_vector([(2, 0), (3, 0)], [(4, 0), (6, 0), (3, 0)]),[(8 + 0j), (12 + 0j), (6 + 0j), (12 + 0j), (18 + 0j), (9 + 0j)])
        self.assertEqual(LibreriaMatrices.producto_tencsor_vector([(2, 0), (-1, 0)], [(3, 0), (4, 0), (7, 0)]),[(6 + 0j), (8 + 0j), (14 + 0j), (-3 + 0j), (-4 + 0j), (-7 + 0j)])
        self.assertEqual(LibreriaMatrices.producto_tencsor_vector([(4.0, 0), (-1.1, 0)], [(4.6, 9), (4.3, 7.2)]),[(18.4 + 36j), (17.2 + 28.8j), (-5.06 - 9.9j), (-4.73 - 7.920000000000001j)])
        self.assertEqual(LibreriaMatrices.producto_tencsor_vector([(5.8, 4)], [(1, -1.0), (8, 7)]),[(9.8 - 1.7999999999999998j), (18.4 + 72.6j)])

    def test_producto_tensor_matriz(self):
        self.assertEqual(LibreriaMatrices.producto_tensor_matrices([[(1, 0), (2, 0)], [(3, 0), (1, 0)]],[[(0, 0), (3, 0)], [(2, 0), (1, 0)]]),[[[[0j, (3 + 0j)], [(2 + 0j), (1 + 0j)]], [[0j, (6 + 0j)], [(4 + 0j), (2 + 0j)]]],[[[0j, (9 + 0j)], [(6 + 0j), (3 + 0j)]], [[0j, (3 + 0j)], [(2 + 0j), (1 + 0j)]]]])
        self.assertEqual(LibreriaMatrices.producto_tensor_matrices([[(5, 0), (3, 0), (-4, 0), (-2, 0)], [(8, 0), (-1, 0), (0, 0), (-3, 0)]],[[(1, 0), (4, 0), (0, 0)], [(-5, 0), (3, 0), (7, 0)], [(0, 0), (-9, 0), (5, 0)], [(5, 0), (1, 0), (4, 0)]]),[[[[(5 + 0j), (20 + 0j), 0j], [(-25 + 0j), (15 + 0j), (35 + 0j)], [0j, (-45 + 0j), (25 + 0j)],[(25 + 0j), (5 + 0j), (20 + 0j)]],[[(3 + 0j), (12 + 0j), 0j], [(-15 + 0j), (9 + 0j), (21 + 0j)], [0j, (-27 + 0j), (15 + 0j)],[(15 + 0j), (3 + 0j), (12 + 0j)]],[[(-4 + 0j), (-16 + 0j), (-0 + 0j)], [(20 - 0j), (-12 + 0j), (-28 + 0j)],[(-0 + 0j), (36 - 0j), (-20 + 0j)], [(-20 + 0j), (-4 + 0j), (-16 + 0j)]],[[(-2 + 0j), (-8 + 0j), (-0 + 0j)], [(10 - 0j), (-6 + 0j), (-14 + 0j)],[(-0 + 0j), (18 - 0j), (-10 + 0j)], [(-10 + 0j), (-2 + 0j), (-8 + 0j)]]], [[[(8 + 0j), (32 + 0j), 0j], [(-40 + 0j), (24 + 0j), (56 + 0j)],[0j, (-72 + 0j), (40 + 0j)], [(40 + 0j), (8 + 0j), (32 + 0j)]],[[(-1 + 0j), (-4 + 0j), (-0 + 0j)], [(5 - 0j), (-3 + 0j), (-7 + 0j)],[(-0 + 0j), (9 - 0j), (-5 + 0j)], [(-5 + 0j), (-1 + 0j), (-4 + 0j)]],[[0j, 0j, 0j], [(-0 + 0j), 0j, 0j], [0j, (-0 + 0j), 0j], [0j, 0j, 0j]],[[(-3 + 0j), (-12 + 0j), (-0 + 0j)], [(15 - 0j), (-9 + 0j), (-21 + 0j)],[(-0 + 0j), (27 - 0j), (-15 + 0j)], [(-15 + 0j), (-3 + 0j), (-12 + 0j)]]]])
        self.assertEqual(LibreriaMatrices.producto_tensor_matrices([[(-2, 0), (3, 0)], [(-5, 0), (1, 0)], [(0, 0), (-6, 0)]],[[(1, 0), (-5, 0), (0, 0)], [(-8, 0), (9, 0), (2, 0)]]), [[[[(-2 + 0j), (10 - 0j), (-0 + 0j)], [(16 - 0j), (-18 + 0j), (-4 + 0j)]],[[(3 + 0j), (-15 + 0j), 0j], [(-24 + 0j), (27 + 0j), (6 + 0j)]]],[[[(-5 + 0j), (25 - 0j), (-0 + 0j)], [(40 - 0j), (-45 + 0j), (-10 + 0j)]],[[(1 + 0j), (-5 + 0j), 0j], [(-8 + 0j), (9 + 0j), (2 + 0j)]]],[[[0j, (-0 + 0j), 0j], [(-0 + 0j), 0j, 0j]],[[(-6 + 0j), (30 - 0j), (-0 + 0j)], [(48 - 0j), (-54 + 0j), (-12 + 0j)]]]])
        self.assertEqual(LibreriaMatrices.producto_tensor_matrices([[(16, 2.3)], [(0, -7)], [(6, 0)], [(0, -4)]],[[(6, -4)], [(7, 3)], [(4.2, -8.1)], [(0, -3)]]),[[[[(105.2 - 50.2j)], [(105.1 + 64.1j)], [(85.83 - 119.94j)], [(6.8999999999999995 - 48j)]]],[[[(-28 - 42j)], [(21 - 49j)], [(-56.699999999999996 - 29.400000000000002j)], [(-21 - 0j)]]],[[[(36 - 24j)], [(42 + 18j)], [(25.200000000000003 - 48.599999999999994j)], [-18j]]],[[[(-16 - 24j)], [(12 - 28j)], [(-32.4 - 16.8j)], [(-12 - 0j)]]]])

    def test_suma_matrices(self):
        self.assertEqual(LibreriaMatrices.sumaDeMatrices([[(3, 2), (0, 0), (5, -6)], [(1, 0), (4, 2), (0, 1)], [(4, -1), (0, 0), (4, 0)]],[[(5, 0), (2, -1), (6, -4)], [(0, 0), (4, 5), (2, 0)], [(7, -4), (2, 7), (0, 0)]]),[(8 + 2j), (2 - 1j), (11 - 10j), (1 + 0j), (8 + 7j), (2 + 1j), (11 - 5j), (2 + 7j), (4 + 0j)])
        self.assertEqual(LibreriaMatrices.sumaDeMatrices([[(5, 0), (3, 0), (-4, 0), (-2, 0)], [(8, 0), (-1, 0), (0, 0), (-3, 0)]],[[(1, 0), (4, 0), (0, 0)], [(-5, 0), (3, 0), (7, 0)], [(0, 0), (-9, 0), (5, 0)], [(5, 0), (1, 0), (4, 0)]]),[(6 + 0j), (7 + 0j), (-4 + 0j), (3 + 0j), (2 + 0j), (7 + 0j)])
        self.assertEqual(LibreriaMatrices.sumaDeMatrices([[(-2, 0), (3, 0)]], [[(-5, 0), (1, 0)]]),[(-7 + 0j), (4 + 0j)])
