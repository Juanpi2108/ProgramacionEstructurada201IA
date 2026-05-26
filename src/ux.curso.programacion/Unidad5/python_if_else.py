def verificar_numero(n):
    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and 2 <= n <= 5:
        print("Not Weird")
    elif n % 2 == 0 and 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")


def main():
    numero = int(input("Ingresa un número: "))
    verificar_numero(numero)


if __name__ == "__main__":
    main()