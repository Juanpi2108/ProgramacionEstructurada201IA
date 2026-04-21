def imprimir_encabezado(n):
    """Imprime la primera fila con los números"""
    print("    ", end="")
    for i in range(1, n + 1):
        print(f"{i:4}", end="")
    print()


def imprimir_separador(n):
    """Imprime la línea separadora"""
    print("    " + "----" * n)


def imprimir_filas(n):
    """Imprime las filas con las multiplicaciones"""
    for i in range(1, n + 1):
        print(f"{i:2} |", end="")
        for j in range(1, n + 1):
            print(f"{i * j:4}", end="")
        print()


def tabla_multiplicar(n):
    """Función principal que organiza todo"""
    imprimir_encabezado(n)
    imprimir_separador(n)
    imprimir_filas(n)


def main():
    n = 15
    tabla_multiplicar(n)


if __name__ == "__main__":
    main()