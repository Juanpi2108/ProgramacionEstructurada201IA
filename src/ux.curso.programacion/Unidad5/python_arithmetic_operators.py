def operaciones(a, b):
    print(a + b)
    print(a - b)
    print(a * b)


def main():
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    operaciones(num1, num2)


if __name__ == "__main__":
    main()