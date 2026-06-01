def capturar_ventas(productos, dias):
    ventas = [[0] * len(dias) for _ in range(len(productos))]

    for i in range(len(productos)):
        print(f"\n--- Registro para {productos[i]} ---")

        for j in range(len(dias)):
            ventas[i][j] = int(
                input(f"Ingrese ventas de {productos[i]} para {dias[j]}: ")
            )

    return ventas


def mostrar_tabla(productos, dias, ventas):
    print("\n=====================================")
    print("         RESUMEN DE VENTAS")
    print("=====================================")

    print(
        f"{'Producto':<12} {'Lunes':<8} {'Martes':<8} "
        f"{'Miércoles':<10} {'Total':<8}"
    )

    for i in range(len(productos)):
        total_producto = sum(ventas[i])

        print(
            f"{productos[i]:<12} "
            f"{ventas[i][0]:<8} "
            f"{ventas[i][1]:<8} "
            f"{ventas[i][2]:<10} "
            f"{total_producto:<8}"
        )


def calcular_totales(productos, ventas):
    total_general = 0
    totales_productos = []

    for i in range(len(productos)):
        suma_producto = sum(ventas[i])
        totales_productos.append(suma_producto)
        total_general += suma_producto

    promedio = total_general / 9

    return total_general, promedio, totales_productos


def producto_mas_vendido(productos, totales_productos):
    indice = totales_productos.index(max(totales_productos))

    return productos[indice], totales_productos[indice]


def main():
    productos = ["Laptop", "Smartphone", "Tablet"]
    dias = ["Lunes", "Martes", "Miércoles"]

    # Captura de datos
    ventas = capturar_ventas(productos, dias)

    # Mostrar tabla
    mostrar_tabla(productos, dias, ventas)

    # Calcular estadísticas
    total_general, promedio, totales_productos = calcular_totales(
        productos, ventas
    )

    print(f"\nVenta total general: {total_general}")
    print(f"Promedio de ventas: {promedio:.2f}")

    # Producto más vendido
    nombre, total = producto_mas_vendido(
        productos, totales_productos
    )

    print(f"\nProducto más vendido de la semana: {nombre}")
    print(f"Total vendido: {total}")


if __name__ == "__main__":
    main()