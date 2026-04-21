def division_por_restas():
    dividendo = int(input("Ingresa el dividendo: "))
    divisor = int(input("Ingresa el divisor: "))

    if divisor == 0:
        print("Error: división por cero")
        return

    cociente = 0
    resto = dividendo

    while resto >= divisor:
        resto = resto - divisor
        cociente = cociente + 1

    print("Cociente:", cociente)
    print("Resto:", resto)


def main():
    division_por_restas()

if __name__ == "__main__":
    main()