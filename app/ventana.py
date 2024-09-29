from nave import Nave

class Ventana:
    def __init__(self, estilo, ancho, alto, cantidad):
        self.estilo = estilo
        self.ancho = ancho
        self.alto = alto
        self.naves = []  # Lista de instancias de Nave
        self.cantidad = cantidad

    def agregar_nave(self, tipo_nave, ancho, alto, material, vidrio):
        nave = Nave(tipo_nave, ancho, alto, material, vidrio)
        self.naves.append(nave)

    def calcular_costo(self):
        return sum(nave.calcular_costo_total() for nave in self.naves) * self.cantidad
