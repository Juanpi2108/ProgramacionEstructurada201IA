import math

def calcular_imc():
    W = int(input("Ingresa tu peso: "))
    H = float(input("Ingresa tu estatura: "))
    imc = W * H
    print("Tu peso es: ",W,"KG","\nTu estatura es: ",H,"M","\nPor lo tanto tu IMC es de: ",imc)

def main():
    calcular_imc()

if __name__ == "__main__":
    main()

