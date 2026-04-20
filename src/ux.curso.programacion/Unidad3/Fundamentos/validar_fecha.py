def es_bisiesto(anio):
    return (anio % 400 == 0) or ((anio % 4 == 0) and (anio % 100 != 0))


def validar_fecha(dia, mes, anio):

    if mes < 1 or mes > 12:
        return False

    if mes == 2:
        if es_bisiesto(anio):
            max_dias = 29
        else:
            max_dias = 28
    elif mes in [1, 3, 5, 7, 8, 10, 12]:
        max_dias = 31
    else:
        max_dias = 30

    if dia >= 1 and dia <= max_dias:
        return True
    else:
        return False


dia = int(input("Ingresa el día: "))
mes = int(input("Ingresa el mes: "))
anio = int(input("Ingresa el año: "))

if validar_fecha(dia, mes, anio):
    print("Fecha válida")
else:
    print("Fecha inválida")

def main():
    validar_fecha()

if __name__ == "__main__":
    main()