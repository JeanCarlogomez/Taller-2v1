from ventana import Ventana

class Cotizacion:
    def __init__(self):
        self.ventanas = []  # Lista de instancias de Ventana

    def agregar_ventana(self, ventana):
        self.ventanas.append(ventana)

    def calcular_precio_total(self):
        total = sum(ventana.calcular_costo() for ventana in self.ventanas)
        if len(self.ventanas) > 100:
            total *= 0.9  # Aplicar 10% de descuento
        return total
