def capturar_temperaturas():
    temperaturas = []

    for i in range(8):
        lectura = float(input(f"Lectura {i + 1}: "))
        temperaturas.append(lectura)

    return temperaturas


def filtrar_temperaturas(temperaturas):
    contador_errores = 0

    for i in range(8):
        if temperaturas[i] < 0 or temperaturas[i] > 100:
            temperaturas[i] = 35.0
            contador_errores += 1

    return contador_errores


def calcular_promedio(temperaturas):
    suma = 0

    for temp in temperaturas:
        suma += temp

    promedio = suma / 8

    return promedio


def mostrar_estado(promedio):
    if promedio > 75:
        print("ALERTA: Activando sistema de enfriamiento líquido")
    else:
        print("Estado: Operación normal")


def main():
    print("--- SISTEMA DE FILTRADO DE DATOS (SENSOR GPU) ---\n")

    temperaturas = capturar_temperaturas()

    contador_errores = filtrar_temperaturas(temperaturas)

    print(f"\nSe detectaron {contador_errores} lecturas erróneas y fueron corregidas a 35.0.")

    print("Datos limpios:", temperaturas)

    promedio = calcular_promedio(temperaturas)

    print(f"\nPromedio de operación: {promedio:.2f}°C")

    mostrar_estado(promedio)


if __name__ == "__main__":
    main()