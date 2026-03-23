def cargar_lotes():
    limite = 2500  # MB
    consumo_total = 0

    while True:
        lote = float(input("Ingresa el tamaño del lote en MB: "))

        consumo_total += lote
        print(f"Consumo acumulado: {consumo_total} MB")

        if consumo_total > limite:
            print("Se superó el límite de 2500 MB. Proceso detenido.")
            break

def main():
    cargar_lotes()

if __name__ == "__main__":
    main()