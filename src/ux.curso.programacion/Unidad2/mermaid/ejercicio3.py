'''
Diseñar un algoritmo que
solicite un número entero
y luego genere una secuencia
de números
'''

def secuencia():
    N = int(input("Ingresa cuántos números quieres: "))
    
    contador = 0
    numero = 1
    
    while contador < N:
        print(numero)
        numero = numero + 2
        contador = contador + 1

secuencia()