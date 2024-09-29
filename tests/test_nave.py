from app.nave import Nave
from app.material import Material
from app.vidrio import Vidrio

def test_nave():
    material = Material("Pulido", 50_700)
    vidrio = Vidrio("Transparente", 8.25)
    nave = Nave("X", 40, 90, material, vidrio)

    assert nave.ancho == 40, "El ancho debe ser 40"
    assert nave.alto == 90, "El alto debe ser 90"

    costo_aluminio = nave.calcular_costo_aluminio()
    assert costo_aluminio == 131820.0, "El costo del aluminio debe ser 131,820.0"

    area_vidrio = nave.calcular_costo_vidrio()
    print(f"Costo del vidrio calculado: {area_vidrio}")  # Imprimir el costo calculado
    assert round(area_vidrio, 2) == 28109.81, "El costo del vidrio debe ser 28,109.81"  # Mantener la afirmación aquí

test_nave()
print("Prueba de Nave: OK")


