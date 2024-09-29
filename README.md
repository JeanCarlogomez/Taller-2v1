# Sistema de Gestión de Inventarios

## Descripción
Este proyecto desarrolla un sistema para la empresa PQR, dedicada a la fabricación de ventanas de aluminio. El objetivo del sistema es mejorar el proceso manual de cotización de ventanas, proporcionando una herramienta automatizada que permita calcular el precio de ventanas basadas en sus dimensiones, el tipo de aluminio utilizado, el tipo de vidrio, y otros elementos adicionales como las chapas y las esquinas.

El sistema permite gestionar diferentes estilos de ventanas, como O, XO, OXXO, y OXO, y calcular el costo de cada ventana dependiendo del tipo de aluminio y vidrio seleccionado. Además, incluye reglas de negocio como la posibilidad de aplicar un descuento del 10% en pedidos de más de 100 ventanas.

Funcionalidades
Selección de estilos de ventanas: O, XO, OXXO, y OXO.
Cálculo de costos basado en:
Dimensiones de las ventanas: Ancho y alto.
Materiales:
Acabado del aluminio (Pulido, Lacado Brillante, Lacado Mate, Anodizado).
Tipo de vidrio (Transparente, Bronce, Azul) con opción de esmerilado.
Otros componentes (chapas, esquinas).
Aplicación automática de descuentos para grandes pedidos.
Tecnologías Utilizadas
Lenguaje de programación: Python
Gestión de dependencias: venv
Interfaz de usuario: Consola (utilizando la librería Rich)
Versionamiento: Git y GitHub

## Información del Proyecto
- **Estudiante**: Jean Carlo Gomez Ortiz
- **Profesor**: Diego Fernando Marin
- **Curso**: Lenguaje de Programación Avanzada 1

## Instalación

1. **Clonar el repositorio**:
    Git Bash
   git clone https://github.com/JeanCarlogomez/Taller-2v1.git

2. **Crear y activar un entorno virtual**: 
    py -m venv venv
    source venv\scripts\activate

3. **Instalar las dependencias listadas en requirements.txt:**: 
    pip install -r requirements.txt

## Requerimientos del Sistema
    Python 3.x
    Librerías: Rich (y otras que estén listadas en requirements.txt).