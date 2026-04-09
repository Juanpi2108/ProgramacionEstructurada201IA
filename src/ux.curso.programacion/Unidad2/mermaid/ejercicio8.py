def contraseña():
    intentos=0
    contraseña_incorrecta="1234"
    while intentos<3:
        clave=input("Ingrese la contraseña: ")
        if clave==contraseña_incorrecta:
            print("Contraseña correcta. Acceso concedido.")
            break
        else:
            intentos+=1
            print(f"Contraseña incorrecta. Intento {intentos} de 3.")
    else:
        print("Número máximo de intentos alcanzado. Acceso denegado.")

def main():
    contraseña()

if __name__ == "__main__":
    main()