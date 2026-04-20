def convertir_a_romano(N):
    if N < 1 or N > 3000:
        return "Número inválido"
    
    resultado = ""
    
    valores = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    
    for valor, simbolo in valores:
        while N >= valor:
            resultado += simbolo
            N -= valor
    
    return resultado


try:
    numero = int(input("Ingresa un número: "))
    print("Resultado romano:", convertir_a_romano(numero))
except ValueError:
    print("Entrada inválida")

def main():
    convertir_a_romano()

if __name__ == "__main__":
    main()