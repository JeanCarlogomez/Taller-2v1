import unittest
from app.material import Material

class TestMaterial(unittest.TestCase):
    def test_material(self):
        material = Material("Pulido", 50_700)
        self.assertEqual(material.acabado, "Pulido")
        self.assertEqual(material.precio_por_metro_lineal, 50_700)

        costo = material.calcular_costo(2)  # 2 metros
        self.assertEqual(costo, 101_400)  # 50,700 * 2

if __name__ == '__main__':
    unittest.main()
