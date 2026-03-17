#Ejemplo de repeticion

def ejemplo_for():
    print("Estructura FOR")

    frutas = ["manzana","banana","naranja"]

    #For para iterar listas
    for fruta in frutas:
        print(fruta)

    #
    for i in range(1,5):
        print(i)

    for i in range(1,10,2):
        print(i)

def ejemplo_while():
    print("Estructura WHILE")

    contador = 0

    while contador <= 5:
        print(contador)
        contador += 1

def ejemplo_do_while():
    print("Estructura DO WHILE")

    secreto = "python12"
    intentos = 0

    while True:
        intentos_usuario = "python12"
        intentos += 1

        if intentos_usuario == secreto:
            print("¡ACCESO CONCEDIDO!")
            break
        else:
            print("Contraseña incorrecta. Intenta de nuevo")
            break
        print("\n")

def main():
    ejemplo_for()
    print("\n")
    ejemplo_while()
    print("\n")
    ejemplo_do_while()

if __name__ == "__main__":
    main()