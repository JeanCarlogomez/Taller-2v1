class Vidrio:
    def __init__(self, tipo, precio_por_cm2, esmerilado=False):
        self.tipo = tipo
        self.precio_por_cm2 = precio_por_cm2
        self.esmerilado = esmerilado
        self.precio_esmerilado = 5.20  # Costo adicional por esmerilado

    def calcular_costo(self, area):
        costo_base = area * self.precio_por_cm2
        if self.esmerilado:
            costo_base += self.precio_esmerilado
        return costo_base


