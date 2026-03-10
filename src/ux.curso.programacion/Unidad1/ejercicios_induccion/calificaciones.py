

def calificaciones():
    calificacion = int(input("Ingresa el número: "))
    if calificacion<0 or calificacion>100:
        print("Calificación inválida")
    elif calificacion>=90:
        print("Tu calificación es: A")
    elif calificacion>=80:
        print("Tu calificación es: B")
    elif calificacion>=70:
        print("Tu calificación es: C")
    elif calificacion==69:
        print("Tu calificación es: D")
    else:
        print("Tu calificación es: F")

def main():
    calificaciones()

if __name__=="__main__":
    main()