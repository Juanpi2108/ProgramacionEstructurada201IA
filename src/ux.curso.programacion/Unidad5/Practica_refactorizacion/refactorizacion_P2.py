"""
Materia: Programación Estructurada
Laboratorio: Refactorización y Análisis de Código (Parte II)
Alumno: Juan Pablo Perea Lara
"""

import random
from statistics import median  # Librería especializada para calcular medianas


# =====================================================================
# RETO 1: Formateador de Nombres de Usuario para Discord
# =====================================================================
def limpiar_nombre_usuario(nombre_sucio):
    """
    Limpia espacios al inicio y final del nombre
    y formatea el texto con la primera letra en mayúscula.
    """

    # CAMBIO:
    # Se reemplazó la eliminación manual de espacios
    # por strip(), que ya realiza esta tarea eficientemente.
    nombre_limpio = nombre_sucio.strip()

    # CAMBIO:
    # Se reemplazó la conversión manual usando códigos ASCII
    # por capitalize(), que convierte la primera letra en mayúscula
    # y el resto en minúsculas automáticamente.
    return nombre_limpio.capitalize()


# =====================================================================
# RETO 2: Buscador de Palabras Prohibidas
# =====================================================================
def contiene_palabra_bloqueada(mensaje_chat, palabra_prohibida):
    """
    Verifica si una palabra prohibida existe dentro del mensaje.
    """

    # CAMBIO:
    # Se eliminó el recorrido manual carácter por carácter.
    # El operador 'in' ya realiza esta búsqueda internamente
    # de manera más eficiente y legible.
    return palabra_prohibida in mensaje_chat


# =====================================================================
# RETO 3: Generador de Contraseñas Temporales
# =====================================================================
def generar_clave_temporal():
    """
    Genera una contraseña aleatoria de 8 caracteres.
    """

    caracteres_validos = (
        "ABCDEFGHJKLMNPQRSTUVWXYZ"
        "abcdefghijkmnpqrstuvwxyz"
        "23456789"
    )

    # CAMBIO:
    # Se eliminó la concatenación repetitiva dentro del ciclo.
    # random.choices() selecciona varios caracteres de una sola vez
    # y join() los une eficientemente.
    return "".join(random.choices(caracteres_validos, k=8))


# =====================================================================
# RETO 4: Mediana de Latencia de Red
# =====================================================================
def calcular_mediana_latencia(lista_pings):
    """
    Calcula la mediana de una lista de pings.
    """

    # CAMBIO:
    # Se eliminó el algoritmo de ordenamiento Burbuja
    # y el cálculo manual de la mediana.
    # La librería statistics ya incluye una función optimizada.
    return median(lista_pings)


# =====================================================================
# FUNCIÓN PRINCIPAL
# =====================================================================
def main():
    print("--- Probando Código Refactorizado (Parte II) ---")

    print(
        "Usuario limpio:",
        limpiar_nombre_usuario("   luNA_eDUaRDo  ")
    )

    msg = "No digas malas palabras en este servidor"
    print(
        "¿Tiene groserías?:",
        contiene_palabra_bloqueada(msg, "malas")
    )

    print(
        "Clave generada por el sistema:",
        generar_clave_temporal()
    )

    pings_servidor = [120, 45, 80, 23, 150, 62]
    print(
        "Mediana de latencia encontrada:",
        calcular_mediana_latencia(pings_servidor)
    )


# Punto de entrada del programa
if __name__ == "__main__":
    main()