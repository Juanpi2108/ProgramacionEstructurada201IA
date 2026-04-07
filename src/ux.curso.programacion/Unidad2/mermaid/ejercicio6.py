'''
Algoritmo para el calculo del fondo de ahorro
'''

def fondos():
    saldo=0
    meta=1000
    while saldo < meta:
        deposito=int(input("Ingrese el monto a depositar: "))
        saldo+=deposito
    return saldo

def main():
    resultado=fondos()
    print("El fondo de ahorro acumulado es: ",resultado)

if __name__=="__main__":
    main()