from app.ventana import Ventana
from app.material import Material
from app.vidrio import Vidrio

def test_ventana():
    material = Material("Pulido", 50_700)
    vidrio = Vidrio("Transparente", 8.25)
    ventana = Ventana("XO", 120, 90, 10)  # Cambia la cantidad a 10
    ventana.agregar_nave("X", 40, 90, material, vidrio)

    costo = ventana.calcular_costo()  # Este método debe devolver el costo total de las naves
    print(f"Costo calculado: {costo}")  # Imprimir el costo calculado para depuración
    assert costo == 1_599_298.12, "El costo de la ventana debe ser 1,599,298.12"

test_ventana()
print("Prueba de Ventana: OK")
