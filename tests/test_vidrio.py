from app.vidrio import Vidrio

def test_vidrio():
    vidrio = Vidrio("Transparente", 8.25)
    assert vidrio.tipo == "Transparente", "El tipo de vidrio debe ser 'Transparente'"
    assert vidrio.precio_por_cm2 == 8.25, "El precio por cm² debe ser 8.25"

    costo = vidrio.calcular_costo(3407.25)  # Usando el área calculada previamente
    assert costo == 28_109.81, "El costo del vidrio debe ser 28,109.81"

test_vidrio()
print("Prueba de Vidrio: OK")
