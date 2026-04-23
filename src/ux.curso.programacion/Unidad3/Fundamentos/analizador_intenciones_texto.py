def normalizar_mensaje(texto):
    """
    Convierte el texto a minúsculas y elimina espacios extra
    al inicio y al final.
    """
    texto_limpio = texto.lower().strip()
    return texto_limpio

def detectar_intencion(mensaje):
    """
    Detecta la intención del mensaje basado en palabras clave.
    """
    acciones = ["encender", "activar", "reproducir"]
    soporte = ["ayuda", "error", "fallo"]

    for palabra in acciones:
        if palabra in mensaje:
            return "COMANDO DE ACCIÓN"

    for palabra in soporte:
        if palabra in mensaje:
            return "REPORTE DE SOPORTE"

    return "CONSULTA GENERAL"

def main():
    mensaje_original = input("Ingrese comando de voz: ")
    mensaje_limpio = normalizar_mensaje(mensaje_original)
    categoria = detectar_intencion(mensaje_limpio)
    longitud = len(mensaje_original)

    print("\n--- PROCESANDO POR IA ---\n")
    print(f'Mensaje Normalizado: "{mensaje_limpio}"')
    print(f"Categoría de Intención: {categoria}")
    print(f"Longitud del mensaje: {longitud} caracteres")
    print("\n--------------------------")

if __name__ == "__main__":
    main()