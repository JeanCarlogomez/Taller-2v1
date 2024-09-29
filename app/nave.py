from .componente import Componente

class Nave:
    def __init__(self, tipo, ancho, alto, material, vidrio):
        self.tipo = tipo  # O o X
        self.ancho = ancho
        self.alto = alto
        self.material = material  # Instancia de Material
        self.vidrio = vidrio  # Instancia de Vidrio
        self.componentes = []  # Lista de componentes

    def agregar_componente(self, componente):
        self.componentes.append(componente)

    def calcular_costo_aluminio(self):
        # Cálculo simplificado
        perimetro = 2 * (self.ancho + self.alto)  # Perímetro de la nave
        return self.material.calcular_costo(perimetro / 100)  # Cambiar a metros

    def calcular_costo_vidrio(self):
        # El área del vidrio es (ancho * alto), menos 1.5 cm de cada lado
        area = (self.ancho - 1.5) * (self.alto - 1.5)
        print(f"Área del vidrio: {area}")
        return self.vidrio.calcular_costo(area)

    def calcular_costo_componentes(self):
        return sum(componente.costo for componente in self.componentes)

    def calcular_costo_total(self):
        costo_aluminio = self.calcular_costo_aluminio()
        costo_vidrio = self.calcular_costo_vidrio()
        costo_componentes = self.calcular_costo_componentes()

        print(f"Costo Aluminio: {costo_aluminio}")
        print(f"Costo Vidrio: {costo_vidrio}")
        print(f"Costo Componentes: {costo_componentes}")

        total = costo_aluminio + costo_vidrio + costo_componentes
        print(f"Costo Total Nave: {total}")
        return total
