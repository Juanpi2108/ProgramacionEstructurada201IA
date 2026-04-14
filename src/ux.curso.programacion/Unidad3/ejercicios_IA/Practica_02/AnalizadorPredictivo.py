# --- SISTEMA DE MONITOREO INDUSTRIAL ---
 
def limpiar_dato(lectura):

    try:
        valor = float(lectura)
        
        if valor < 0 or valor > 100:
            return None

        return valor

    except ValueError:
        return None


 
 
def calcular_alerta(valor_normalizado):


    if valor_normalizado > 0.8:
            return 'CRÍTICO'
    elif valor_normalizado > 0.5:
            return 'PRECAUCIÓN'
    else:
            return 'NORMAL'
 
 
def obtener_estadisticas(lista_datos):
    # IMPLEMENTAR AQUÍ

    if not lista_datos:
        return (0, 0, 0)

    maximo = max(lista_datos)
    minimo = min(lista_datos)
    promedio = sum(lista_datos) / len(lista_datos)

    return (maximo, minimo, promedio)
 
def generar_reporte(total_datos, validos, estadisticas):

    v_max, v_min, v_prom = estadisticas
    descartados = total_datos - validos


    print("*" * 30)
    print("REPORTE DE ANALISIS PREDICTIVO")
    print("*" * 30)
    print(f"Total de lecturas: {total_datos}")
    print(f"Lecturas válidas: {validos}")
    print(f"Lecturas descartadas: {descartados}")
    print(f"Valor máximo: {v_max:.2f}")
    print(f"Valor mínimo: {v_min:.2f}")
    print(f"Valor promedio: {v_prom:.2f}")


 
# --- LÓGICA PRINCIPAL (NO MODIFICAR ESTA PARTE) ---
import os
def ejecutar_pipeline():
    datos_finales = []
    cuenta_total = 0
    # Obtener la ruta absoluta del archivo en la misma carpeta que el script
    ruta_script = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(ruta_script, "lecturas_sensores.txt")

    with open(ruta_archivo, "r") as f:
         for linea in f:
                cuenta_total += 1
         valor = limpiar_dato(linea.strip())
    
         if valor is not None:
            # Normalizar para la IA (0-1)
            datos_finales.append(valor / 100)
         if datos_finales:
            stats = obtener_estadisticas(datos_finales)
            generar_reporte(cuenta_total, len(datos_finales), stats)

if __name__ == "__main__":
    ejecutar_pipeline()

    
