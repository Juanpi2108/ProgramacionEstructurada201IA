def clasificar_objeto(dimension):
    UMBRAL_PEQUENO = 5.0
    UMBRAL_GRANDE = 20.0

    if dimension <= 0.0:
        print("Error: Lectura inválida. Verifique el sensor.")
    
    elif dimension <= UMBRAL_PEQUENO:
        print("Clasificación: Micro-componente (Grado A)")
    
    elif dimension <= UMBRAL_GRANDE:
        print("Clasificación: Componente Estándar (Grado B)")
    
    else:
        print("Clasificación: Componente Industrial (Grado C)")
        volumen = dimension ** 3
        print(f"Espacio requerido en contenedor: {volumen} cm3")

    print("Registro de inspección completado.")


def main():
    entrada = input("Ingrese el tamaño del objeto detectado (cm): ")
    dimension = float(entrada)

    clasificar_objeto(dimension)


if __name__ == "__main__":
    main()