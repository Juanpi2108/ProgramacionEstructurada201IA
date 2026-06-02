"""
Materia: Programación Estructurada
Laboratorio: Refactorización y Análisis de Código (Parte III)
Alumno: Juan Pablo Perea Lara
"""

import math

# =====================================================================
# RETO 1: Inicializador de Tablero de Juego (Matrices)
# =====================================================================
def inicializar_tablero_vacio():
    # CAMBIO:
    # Se utiliza comprensión de listas para crear filas independientes.
    # Evita que todas las filas apunten a la misma referencia en memoria.
    tablero = [[0 for _ in range(4)] for _ in range(4)]

    return tablero


# =====================================================================
# RETO 2: Recortador de Valores Atípicos (Clamping de Datos)
# =====================================================================
def limitar_senal_sensor(valor_lectura, minimo, maximo):
    # CAMBIO:
    # Se reemplaza el árbol de decisiones por min() y max().
    # Más legible y eficiente.
    return max(minimo, min(valor_lectura, maximo))


# =====================================================================
# RETO 3: Buscador del Valor Más Cercano a Cero (Error Mínimo)
# =====================================================================
def buscar_error_minimo(lista_errores):
    # CAMBIO:
    # Se utiliza infinito matemático en lugar de un número arbitrario.
    menor_error = math.inf

    # CAMBIO:
    # Se recorren directamente los elementos de la lista.
    for valor_actual in lista_errores:

        # CAMBIO:
        # Se utiliza abs() para obtener el valor absoluto.
        absoluto = abs(valor_actual)

        if absoluto < menor_error:
            menor_error = absoluto

    return menor_error


# =====================================================================
# RETO 4: Filtro de Valores Únicos (Eliminador de Duplicados)
# =====================================================================
def depurar_usuarios_repetidos(lista_ids):
    # CAMBIO:
    # Se usa set() para eliminar duplicados automáticamente.
    # Complejidad mucho menor que el algoritmo original.
    return list(set(lista_ids))


# === PROGRAMA PRINCIPAL ===
if __name__ == "__main__":
    print("--- Probando Código Refactorizado (Parte III) ---")

    tablero_ia = inicializar_tablero_vacio()
    print("Tablero inicializado de 4x4:")
    for fila in tablero_ia:
        print(fila)

    print(
        "Lectura recortada (125.4 en rango 0-100):",
        limitar_senal_sensor(125.4, 0.0, 100.0)
    )

    errores_entrenamiento = [0.45, -0.12, 0.89, -0.03, 0.22]
    print(
        "El error más cercano a cero es:",
        buscar_error_minimo(errores_entrenamiento)
    )

    ids_discord = [4521, 8892, 4521, 1022, 8892, 9931]
    print(
        "Lista de IDs únicas filtradas:",
        depurar_usuarios_repetidos(ids_discord)
    )