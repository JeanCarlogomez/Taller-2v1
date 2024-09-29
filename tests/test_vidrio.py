import unittest
from app.vidrio import Vidrio

class TestVidrio(unittest.TestCase):
    def test_vidrio(self):
        vidrio = Vidrio("Transparente", 8.25)
        self.assertEqual(vidrio.tipo, "Transparente")
        self.assertEqual(vidrio.precio_por_cm2, 8.25)

        costo = vidrio.calcular_costo(3407.25)  # Usando el área calculada previamente
        self.assertAlmostEqual(costo, 28_205.69, places=2)  # Confirmar que el cálculo es correcto

if __name__ == '__main__':
    unittest.main()
