import math
from datetime import datetime

def imprimir_encabezado():
    print("====================================")
    print("   SISTEMA DE SALUD INTELIGENTE    ")
    print("====================================")
    print(f"Fecha: {datetime.now().strftime('%d/%m/%Y')}")
    print()

def calcular_imc(peso, estatura):
    return peso / (estatura ** 2)

def evaluar_presion(presion_sistolica):
    if presion_sistolica > 140:
        return "Alta"
    else:
        return "Normal"

def main():
    imprimir_encabezado()
    
    nombre = input("Nombre del Paciente: ")
    peso = float(input("Peso (kg): "))
    estatura = float(input("Estatura (m): "))
    presion = int(input("Presión Sistólica: "))
    
    print()
    
    imc = calcular_imc(peso, estatura)
    estado_presion = evaluar_presion(presion)
    
    print("--- RESULTADOS DEL ANÁLISIS ---")
    print(f"Paciente: {nombre}")
    print(f"IMC Calculado: {math.ceil(imc)}")
    print(f"Estado de Presión: {estado_presion}")
    print("-------------------------------")

if __name__ == "__main__":
    main()