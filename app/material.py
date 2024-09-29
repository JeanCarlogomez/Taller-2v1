class Material:
    def __init__(self, acabado, precio_por_metro_lineal):
        self.acabado = acabado
        self.precio_por_metro_lineal = precio_por_metro_lineal

    def calcular_costo(self, metros_lineales):
        return metros_lineales * self.precio_por_metro_lineal
