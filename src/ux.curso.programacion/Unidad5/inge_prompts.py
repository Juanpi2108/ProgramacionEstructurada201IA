# ==========================================
# IMPORTACIÓN DE BIBLIOTECAS (Biblioteca Estándar)
# ==========================================

import sys

# ==========================================
# FUNCIONES GENERADAS A PARTIR DE LOS CONTRATOS
# ==========================================

def limpiar_lecturas(lista_datos):
    """
    Filtra las lecturas de telemetría eliminando valores
    fuera del rango permitido (0.0 a 100.0).

    Parámetros:
        lista_datos (list): Lista de números flotantes.

    Retorna:
        list: Nueva lista con lecturas válidas.
    """
    lista_filtrada = []

    for dato in lista_datos:
        if dato >= 0.0 and dato <= 100.0:
            lista_filtrada.append(dato)

    return lista_filtrada


def calcular_alertas(lista_filtrada, umbral_critico):
    """
    Cuenta cuántas lecturas se encuentran por debajo
    del umbral crítico establecido.

    Parámetros:
        lista_filtrada (list): Lista de lecturas válidas.
        umbral_critico (float): Distancia crítica.

    Retorna:
        int: Cantidad de alertas detectadas.
    """
    total_alertas = 0

    for lectura in lista_filtrada:
        if lectura < umbral_critico:
            total_alertas += 1

    return total_alertas


def generar_log_sistema(total_alertas):
    """
    Genera un mensaje de log indicando la plataforma
    donde se ejecuta el programa y la acción sugerida.

    Parámetros:
        total_alertas (int): Número total de alertas.

    Retorna:
        str: Mensaje de log formateado.
    """
    sistema = sys.platform

    if total_alertas > 3:
        accion = "ABORTAR"
    else:
        accion = "PERMITIDA"

    log = (
        "[" + sistema + "] "
        + "Alertas críticas encontradas: "
        + str(total_alertas)
        + ". Acción: "
        + accion
    )

    return log


# ==========================================
# PROGRAMA PRINCIPAL (Orquestación Manual)
# ==========================================

if __name__ == "__main__":

    # 1. Datos simulados de telemetría
    lecturas_raw = [12.5, -5.0, 88.2, 120.1, 1.2, 0.0, 45.6, 2.5]

    UMBRAL = 3.0

    print("=== SISTEMA DE TELEMETRÍA DE AGENTE AUTÓNOMO ===\n")

    # Paso 1: Limpiar datos
    lecturas_limpias = limpiar_lecturas(lecturas_raw)

    # Paso 2: Calcular alertas
    alertas = calcular_alertas(lecturas_limpias, UMBRAL)

    # Paso 3: Generar log
    log_final = generar_log_sistema(alertas)

    # Mostrar resultado
    print("Lecturas originales:", lecturas_raw)
    print("Lecturas válidas:", lecturas_limpias)
    print("Total de alertas:", alertas)
    print("\nLOG DEL SISTEMA:")
    print(log_final)


"""
EVIDENCIAS DE CONTROL DE CALIDAD

1. PROMPT UTILIZADO

Actúa como un programador experto en Python Estructurado.
Escribe el código de una función llamada limpiar_lecturas.
Recibe como parámetro una lista de números flotantes y debe
retornar una nueva lista con los valores comprendidos entre
0.0 y 100.0 inclusive.

Restricciones estrictas:
1. No utilices programación orientada a objetos (POO).
2. No utilices manejo de excepciones (nada de bloques try-except).
3. Utiliza únicamente estructuras básicas como if, for y variables.
4. Incluye la documentación de la función mediante un Docstring descriptivo.


2. TABLA DE PRUEBA DE ESCRITORIO MANUAL

Caso de prueba:

lecturas_raw = [-20.0, 150.0, -3.5]
UMBRAL = 5.0

Paso 1: limpiar_lecturas()

Dato actual     ¿Es válido?     Lista filtrada
------------------------------------------------
-20.0           No              []
150.0           No              []
-3.5            No              []

Resultado:
lecturas_limpias = []

Paso 2: calcular_alertas()

La lista está vacía, por lo que el ciclo for no se ejecuta.

Resultado:
alertas = 0

Paso 3: generar_log_sistema()

total_alertas = 0

¿0 > 3?
No

accion = "PERMITIDA"

Resultado final:
"[win32] Alertas críticas encontradas: 0. Acción: PERMITIDA"

(La plataforma puede variar según el sistema operativo).


3. AUDITORÍA DE CÓDIGO

En algunos intentos la IA generó:

- Comprensión de listas:
  [x for x in lista_datos if 0.0 <= x <= 100.0]

- Funciones avanzadas como filter().

Aunque son válidas en Python, no corresponden al estilo
estructurado básico visto en clase.

Para corregirlo se modificó el prompt agregando:
"Utiliza únicamente estructuras básicas como if, for,
variables y listas tradicionales. No uses comprensión
de listas, filter(), lambda ni sintaxis avanzada."

La versión final utiliza exclusivamente:
- Variables
- if/else
- for
- append()
- Funciones definidas con def

cumpliendo completamente con el paradigma estructurado.
"""