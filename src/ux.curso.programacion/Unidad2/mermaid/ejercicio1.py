"""
Diseñar un algoritmo que calcule la suma de 
todos los números enteros del 1 al 100 que son
divisibles por 3 Y, además, impares 
"""
def es_divisible():
    while i<=100:
        if i % 3==0 and i % 2!=0:
            suma += i
            i += 1
            return suma
def main():
    suma=es_divisible()
    print(suma)

    if __name__=="__main__":
        main()