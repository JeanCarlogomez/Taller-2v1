import unittest
from app.ventana import Ventana
from app.material import Material
from app.vidrio import Vidrio

class TestVentana(unittest.TestCase):
    def test_ventana(self):
        material = Material("Pulido", 50_700)
        vidrio = Vidrio("Transparente", 8.25)
        ventana = Ventana("XO", 120, 90, 1)
        ventana.agregar_nave("X", 40, 90, material, vidrio)

        costo = ventana.calcular_costo()
        self.assertAlmostEqual(costo, 1_600_256.90, places=2)  # Confirmar que el cálculo es correcto

if __name__ == '__main__':
    unittest.main()
