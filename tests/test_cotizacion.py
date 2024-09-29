import unittest
from app.cotizacion import Cotizacion
from app.ventana import Ventana
from app.material import Material
from app.vidrio import Vidrio

class TestCotizacion(unittest.TestCase):
    def test_cotizacion(self):
        material = Material("Pulido", 50_700)
        vidrio = Vidrio("Transparente", 8.25)
        ventana = Ventana("XO", 120, 90, 1)
        ventana.agregar_nave("X", 40, 90, material, vidrio)

        cotizacion = Cotizacion()
        cotizacion.agregar_ventana(ventana)

        total = cotizacion.calcular_precio_total()
        self.assertAlmostEqual(total, 1_600_256.90, places=2)  # Ajusta el valor esperado si es necesario

if __name__ == '__main__':
    unittest.main()
