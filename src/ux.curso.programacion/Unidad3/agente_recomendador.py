# ============================================
# SISTEMA DE RECOMENDACIÓN IA v1.0
# ============================================

# ----------- PREPARACIÓN DE DATOS -----------
peliculas_accion = ["Mad Max", "John Wick", "Inglourious Basterds", "The Dark Knight", "Man of Steel"]
peliculas_comedia = ["Hangover", "Scary Movie", "Free Guy", "The Mask", "Kick-Ass"]
peliculas_crimen = ["The Godfather", "Goodfellas", "Casino", "The Irishman", "The Intouchables"]

# ----------- FUNCIÓN DE RECOMENDACIÓN -----------
def obtener_recomendacion(genero_elegido, edad_usuario):
    
    # Si es menor de 13 años, solo comedia
    if edad_usuario < 13:
        return peliculas_comedia[0]
    
    # Si tiene 13 o más, se respeta su elección
    if genero_elegido == "accion":
        return peliculas_accion[0]
    elif genero_elegido == "comedia":
        return peliculas_comedia[0]
    elif genero_elegido == "crimen":
        return peliculas_crimen[0]
    else:
        return "Género no válido"

# ----------- LÓGICA PRINCIPAL -----------
print("SISTEMA DE RECOMENDACIÓN IA v1.0")
print("--------------------------------")

edad = int(input("Ingrese su edad: "))
genero = input("¿Qué género prefiere (accion/comedia/crimen)?: ").lower()

recomendacion = obtener_recomendacion(genero, edad)

# ----------- SALIDA DE RESULTADOS -----------
if edad < 13 and genero == "crimen":
    print("\nNota: Debido a tu edad, hemos ajustado la recomendación a contenido apto para todo público.")

print(f"\nRecomendación de la IA: {recomendacion}")

def main():
    obtener_recomendacion()

if __name__ == "__main__":
    main()