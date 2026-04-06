'''
Diseñar un algoritmo que solicite
un número entero y que calcule su
factorial.
'''

def calcular_factorial():
    N = int(input("Ingresa un número: "))
    
    factorial = 1
    i = 1
    
    while i <= N:
        factorial = factorial * i
        i = i + 1
    
    print("El factorial es:", factorial)

calcular_factorial()