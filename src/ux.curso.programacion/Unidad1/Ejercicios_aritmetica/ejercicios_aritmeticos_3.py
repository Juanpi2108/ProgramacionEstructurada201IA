import math

def mostrar_funciones_math(numero):
    sen_x = math.sin(numero)
    cos_x = math.cos(numero)

    print("El seno de ",numero," es: ",sen_x)
    print("El coseno de ",numero," es: ",cos_x)

    resultado = sen_x ** 2 + cos_x **2

    print("El resultado de sen^2(x) + cos^2(x) es: ",resultado)

def tangente(numero):
    tan_x = math.tan(numero)
    print("Tangente de ",numero," es: ",tan_x)

def main():
    numero = float(input("Ingrese número: "))
    mostrar_funciones_math(numero)
    tangente(numero)

if __name__ == "__main__":
    main()