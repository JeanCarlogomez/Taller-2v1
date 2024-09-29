import unittest
from app.nave import Nave
from app.material import Material
from app.vidrio import Vidrio

class TestNave(unittest.TestCase):
    def test_nave(self):
        material = Material("Pulido", 50_700)
        vidrio = Vidrio("Transparente", 8.25)
        nave = Nave("X", 40, 90, material, vidrio)

        self.assertEqual(nave.ancho, 40)
        self.assertEqual(nave.alto, 90)

        costo_aluminio = nave.calcular_costo_aluminio()
        self.assertEqual(costo_aluminio, 131820.0)  # Confirmar que el cálculo es correcto

        area_vidrio = nave.calcular_costo_vidrio()
        self.assertEqual(area_vidrio, 28_205.69)  # Confirmar que el cálculo es correcto

if __name__ == '__main__':
    unittest.main()
