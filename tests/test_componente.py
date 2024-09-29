import unittest
from app.componente import Componente

class TestComponente(unittest.TestCase):
    def test_componente(self):
        comp = Componente("Chapa", 16_200)
        self.assertEqual(comp.tipo, "Chapa")
        self.assertEqual(comp.costo, 16_200)

if __name__ == '__main__':
    unittest.main()
