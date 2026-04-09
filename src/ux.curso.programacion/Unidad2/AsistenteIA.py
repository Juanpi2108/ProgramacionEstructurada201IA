def capturar_datos():
    instruccion = input("Instrucción recibida: ")
    confianza = float(input("Nivel de confianza calculado: "))
    return instruccion, confianza

def procesar_instruccion(instruccion, confianza):
    UMBRAL_ALTO = 80.0
    UMBRAL_MINIMO = 40.0

    if confianza >= UMBRAL_ALTO:
        print(f"Ejecutando la acción: {instruccion}... (Éxito)")
    elif UMBRAL_MINIMO <= confianza < UMBRAL_ALTO:
        print(f"Confianza insuficiente. ¿Se refiere a: {instruccion}? Por favor confirme.")
    else:
        print("Error 404: No pude entender la instrucción. Intente hablar más claro.")

def optimizacion(confianza):
    if confianza > 95.0:
        print("Aviso: El modelo ha sido reforzado con éxito debido a la alta precisión.")

def main():
    instruccion, confianza = capturar_datos()
    procesar_instruccion(instruccion, confianza)
    optimizacion(confianza)
    print("Sesión de procesamiento finalizada.")

if __name__ == "__main__":
    main()