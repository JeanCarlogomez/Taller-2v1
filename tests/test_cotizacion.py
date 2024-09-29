import unittest
from app.cotizacion import Cotizacion
from app.ventana import Ventana
from app.material import Material
from app.vidrio import Vidrio

def test_cotizacion():
    material = Material("Pulido", 50_700)
    vidrio = Vidrio("Transparente", 8.25)
    ventana = Ventana("XO", 120, 90, 10)  # Asegúrate de que la cantidad sea 10
    ventana.agregar_nave("X", 40, 90, material, vidrio)

    cotizacion = Cotizacion()
    cotizacion.agregar_ventana(ventana)

    total = cotizacion.calcular_precio_total()
    assert round(total, 2) == 1599298.12, "El total de la cotización debe ser 1,599,298.12"

test_cotizacion()
print("Prueba de Cotización: OK")
