def leer_sensores():
    distancia = float(input("¿A qué distancia está el objeto más cercano (en metros)?: "))
    semaforo = input("¿De qué color está el semáforo? (verde/amarillo/rojo): ").lower()
    peaton = input("¿Hay un peatón cruzando? (si/no): ").lower()
    return distancia, semaforo, peaton


def evaluar_navegacion(distancia, semaforo, peaton):
    if distancia < 5 or peaton == "si":
        print("¡FRENO DE EMERGENCIA ACTIVADO! Deteniendo el vehículo inmediatamente.")
    if semaforo == "rojo":
        print("Estado: Detenido. Esperando luz verde.")
    elif semaforo == "amarillo":
        print("Estado: Precaución. Reduciendo velocidad para detenerse.")
    elif semaforo == "verde":
        if distancia >= 5:
            print("Estado: En movimiento. Todo despejado para avanzar.")
    else:
        print("Error de lectura en sensores: Color de semáforo no reconocido.")


def main():
    distancia, semaforo, peaton = leer_sensores()
    evaluar_navegacion(distancia, semaforo, peaton)
    
    print("Monitoreo de sensores constante... Sistema activo.")


if __name__ == "__main__":
    main()