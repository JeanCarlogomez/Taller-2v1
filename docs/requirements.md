markdown-it-py==3.0.0
mdurl==0.1.2
Pygments==2.18.0
rich==13.8.1

# Requisitos del Sistema de Gestión de Ventanas

## 1. Gestión de Ventanas
- El sistema debe permitir registrar diferentes estilos de ventanas: O, XO, OXXO y OXO.
- El sistema debe calcular automáticamente las dimensiones de las naves (paneles) según el estilo seleccionado y las dimensiones totales de la ventana.

## 2. Gestión de Materiales
- El sistema debe permitir seleccionar el tipo de aluminio para las ventanas, con opciones de acabado: Pulido, Lacado Brillante, Lacado Mate y Anodizado.
- Debe calcular el costo del aluminio basado en los metros lineales de las naves, teniendo en cuenta los bordes y esquinas.

## 3. Gestión de Vidrio
- El sistema debe permitir seleccionar el tipo de vidrio: Transparente, Bronce y Azul.
- Debe existir una opción para aplicar esmerilado al vidrio, con un costo adicional.
- Debe calcular el costo del vidrio según el área de las naves, descontando 1.5 cm de cada lado para la inserción en el marco.

## 4. Componentes Adicionales
- El sistema debe incluir el costo de los componentes adicionales, como:
  - Esquinas, a un costo fijo por unidad.
  - Chapas (solo aplicable a las naves móviles "X"), a un costo fijo por unidad.

## 5. Cálculo de Cotización
- El sistema debe calcular el precio total de cada ventana, sumando:
  - Costo del aluminio.
  - Costo del vidrio.
  - Costo de los componentes adicionales.
- Debe aplicar un descuento del 10% cuando el número total de ventanas cotizadas supera las 100 unidades.

## 6. Generación de Cotizaciones
- El sistema debe permitir la creación de una cotización que contenga una o más ventanas.
- Debe mostrar un resumen con el costo desglosado por ventana y el costo total de la cotización.

## 7. Descuentos por Volumen
- El sistema debe ofrecer un 10% de descuento cuando la cantidad de ventanas cotizadas sea mayor a 100.

## 8. Validaciones
- El sistema debe validar que las dimensiones de la ventana sean correctas según el estilo seleccionado.
- Debe evitar estilos inválidos, como XOX.

## 9. Generación de Reportes
- El sistema debe generar un reporte final con el costo desglosado de cada ventana, el descuento aplicado (si corresponde), y el total final de la cotización.
