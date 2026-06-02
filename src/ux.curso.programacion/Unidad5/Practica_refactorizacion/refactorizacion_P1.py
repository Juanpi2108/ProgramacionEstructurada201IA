"""
Materia: Programación Estructurada
Laboratorio: Refactorización y Análisis de Código
Alumno: Juan Pablo Perea Lara
"""

import random
import math  # Se agrega para utilizar funciones matemáticas optimizadas

# =====================================================================
# RETO 1: El Teorema de Fermat
# Mejora:
# - Se eliminó el exponente fijo.
# - Ahora la función recibe el valor de n como parámetro.
# - Es más reutilizable y flexible.
# =====================================================================
def verificar_fermat(a, b, c, n):
    if n > 2 and (a ** n + b ** n == c ** n):
        print("¡Fermat se equivocó!")
    else:
        print("No, esa combinación no funciona.")


# =====================================================================
# RETO 2: Distancia Euclidiana entre dos puntos
# Mejora:
# - Se reemplaza la raíz cuadrada manual (**0.5)
#   por math.dist(), función especializada de Python.
# - Código más legible y profesional.
# =====================================================================
def calcular_distancia(x1, y1, x2, y2):
    return math.dist((x1, y1), (x2, y2))


# =====================================================================
# RETO 3: Selector Aleatorio de Respuestas
# Mejora:
# - Se elimina la cadena de if-elif.
# - Se almacena todo en una lista.
# - Se utiliza random.choice() para seleccionar
#   directamente un elemento aleatorio.
# =====================================================================
def obtener_saludo_agente():

    saludos = [
        "Hola, soy el agente de IA. ¿En qué ayudo?",
        "¡Conexión establecida! Listo para operar.",
        "Sistemas en línea. Monitoreando el servidor.",
        "Hola humano, procesando tus peticiones."
    ]

    return random.choice(saludos)


# =====================================================================
# RETO 4: Clasificador de Alertas Críticas
# Mejora:
# - Se eliminan los if anidados.
# - Se utilizan retornos tempranos.
# - El flujo es más claro y fácil de mantener.
# =====================================================================
def evaluar_error_sistema(valor_loss):

    if valor_loss < 0:
        return "Error: Valor negativo inválido"

    if valor_loss < 0.4:
        return "Estable"

    if valor_loss < 0.8:
        return "Advertencia: Gradiente inestable"

    if valor_loss <= 1.0:
        return "CRÍTICO: Abortar entrenamiento"

    return "Error: Valor fuera de rango"


# =====================================================================
# FUNCIÓN PRINCIPAL
# Punto de entrada del programa.
# =====================================================================
def main():

    print("--- Probando Código Refactorizado ---")

    verificar_fermat(3, 4, 5, 4)

    print("Distancia calculada:",
          calcular_distancia(0, 0, 3, 4))

    print("Respuesta bot:",
          obtener_saludo_agente())

    print("Estado del log:",
          evaluar_error_sistema(0.85))


# Ejecución del programa
if __name__ == "__main__":
    main()