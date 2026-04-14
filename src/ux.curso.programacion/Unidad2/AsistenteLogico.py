def mostrar_bienvenida(nombre_asistente):
    print(f"Bienvenido, soy {nombre_asistente}. Estoy listo para ayudarte.")


def obtener_entrada():
    return input("¿En qué puedo ayudarte hoy?: ").lower()


def clasificar_intencion(frase):
    if "hola" in frase or "buenos días" in frase:
        print("¡Hola! Soy tu asistente. Es un gusto saludarte.")

    elif "clima" in frase or "temperatura" in frase:
        print("Consultando el servicio meteorológico... Hoy en Xalapa tendremos un día nublado.")

    elif "hora" in frase or "tiempo" in frase:
        print("La hora actual del sistema es: 10:00 PM")

    else:
        print("Lo siento, todavía no entiendo ese comando. ¿Podrías intentar con otra palabra?")


def despedida(nombre_asistente):
    print(f"Proceso finalizado. Gracias por usar {nombre_asistente}.")


def main():
    nombre_asistente = "IA-UX"
    mostrar_bienvenida(nombre_asistente)
    frase = obtener_entrada()
    clasificar_intencion(frase)
    despedida(nombre_asistente)


if __name__ == "__main__":
    main()