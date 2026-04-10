def obtener_lectura():
    lectura = float(input("Ingrese la lectura del sensor térmico: "))
    return lectura

def procesar_lectura(lectura):
    LIMITE_SUPERIOR = 100.0
    LIMITE_INFERIOR = 0.0

    if LIMITE_INFERIOR <= lectura <= LIMITE_SUPERIOR:
        dato_normalizado = lectura / LIMITE_SUPERIOR
        print(f"Señal aceptada. Valor normalizado para el modelo: {dato_normalizado}")
    else:
        print("Error: Lectura fuera de rango. La señal se considera ruido.")

def main():
    lectura = obtener_lectura()
    procesar_lectura(lectura)
    print("Fin del proceso de filtrado de datos.")

if __name__ == "__main__":
    main()