
def datos():
    entero = 25
    decimal = 3.14
    cadena = "Hola, mundo"
    booleano = True

    print(entero)
    print(decimal)
    print(cadena)
    print(booleano)

def tipos_datos_compuesto():
    lista = [10,20,30,40]
    tupla = (19,29,39,49)
    diccionario = {"Nombre: ","Jetro","Edad: ",30,"Ciudad: ","Madrid"}

    print(lista)
    print(tupla)
    print(diccionario)


def main():
    datos()
    tipos_datos_compuesto()

if __name__=="__main__":
    main()