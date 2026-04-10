import math

def define_esfera():
    radio = float(input("Ingrese el radio: "))
    volume = (4/3) * math.pi * math.pow(radio,2)

    print ("El volumen de la esfera es: ", volume, "cm cubicos")


def main():
    define_esfera()

if __name__ == "__main__":
    main()