from app.componente import Componente

def test_componente():
    comp = Componente("Chapa", 16_200)
    assert comp.tipo == "Chapa", "El tipo debe ser 'Chapa'"
    assert comp.costo == 16_200, "El costo debe ser 16,200"

test_componente()
print("Prueba de Componente: OK")
