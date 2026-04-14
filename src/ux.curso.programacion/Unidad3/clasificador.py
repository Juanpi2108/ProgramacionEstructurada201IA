#Limpieza de datos, normalizacion

UMBRAL_ALTO = 0.7
UMBRAL_BAJO = 0.3

def clasificar_pixeles():
    #Solicitar datos al usuario
    intensidad = float(input("Ingrese la intensidad del pixel (entre 0 y 1): "))

    #Si la intensidad es menor a 0 o mayor a 1, es un valor inválido
    if intensidad < 0 or intensidad > 1:
        print("Valor inválido. La intensidad debe estar entre 0 y 1.")
        return
    
    if 0 <= intensidad < UMBRAL_BAJO:
        print("Clasificacion (Fondo oscuro)")
        return
    
    if UMBRAL_BAJO <= intensidad < UMBRAL_ALTO:
        print("Clasificacion (Fondo gris)")
        return

    
    if intensidad >= UMBRAL_ALTO:
        print("Clasificacion (Objeto brillante)")
        return

    print("Analisis de imagen finalizado.")

def main():
    clasificar_pixeles()

if __name__ == "__main__":
    main()