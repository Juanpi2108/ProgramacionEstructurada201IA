'''
Algoritmo que me diga cuantas semanas necesito trabajar para acumular $2500
'''
def salario():
    total_acumulado=0
    semanas=0
    meta=2500
    while total_acumulado < meta:
        salario_semanal=int(input("Ingrese tu salario semanal: "))
        total_acumulado+=salario_semanal
        semanas+=1
    return semanas

def main():
    resultado=salario()
    print("Semanas trabajadas: ",resultado)

if __name__=="__main__":
    main()