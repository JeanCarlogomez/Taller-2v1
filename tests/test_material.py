from app.material import Material

def test_material():
    material = Material("Pulido", 50_700)
    assert material.acabado == "Pulido", "El acabado debe ser 'Pulido'"
    assert material.precio_por_metro_lineal == 50_700, "El precio por metro debe ser 50,700"

    costo = material.calcular_costo(2)  # 2 metros
    assert costo == 101_400, "El costo para 2 metros debe ser 101,400"

test_material()
print("Prueba de Material: OK")
