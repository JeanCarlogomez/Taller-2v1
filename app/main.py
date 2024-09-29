from .material import Material
from .vidrio import Vidrio
from .ventana import Ventana
from .cotizacion import Cotizacion

def main():
    # Crear instancias de materiales y vidrios
    aluminio = Material("Pulido", 50_700)  # Costo del aluminio por metro lineal
    vidrio_transparente = Vidrio("Transparente", 8.25)  # Costo del vidrio por cm²

    # Crear cotización
    cotizacion = Cotizacion()

    # Crear una ventana y agregar naves
    ventana1 = Ventana("XO", 120, 90, 10)  # Estilo XO, 120cm de ancho, 90cm de alto, 10 ventanas
    ventana1.agregar_nave("X", 40, 90, aluminio, vidrio_transparente)  # Agregar una nave de tipo X

    cotizacion.agregar_ventana(ventana1)

    # Calcular el costo total de la cotización
    precio_total = cotizacion.calcular_precio_total()
    print(f"El precio total de la cotización es: ${precio_total:,.2f}")

if __name__ == "__main__":
    main()
