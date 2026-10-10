"""
Programa Principal del Sistema de Telemetría Térmica.
Orquesta la interacción con el usuario por consola y consume las librerías de cálculo.
"""
import sys
from pathlib import Path

# =============================================================================
# DETECCIÓN DINÁMICA DE RUTAS (PATH RESOLUTION)
# =============================================================================
# Detecta la ruta absoluta de 'libs' respecto a la posición de este archivo
RUTA_LIBS = Path(__file__).resolve().parent.parent / "libs"
sys.path.append(str(RUTA_LIBS))

# Importación de la biblioteca modular
from telemetria import calcular_promedio_fases, validar_temperaturas


def ejecutar_consola():
    """Ejecuta el ciclo de interacción interactivo por consola."""
    print("=" * 55)
    print("   SISTEMA DE CONTROL DE TELEMETRÍA TRIFÁSICA (LAB 2)")
    print("=" * 55)
    
    while True:
        opcion = input("\nPresione ENTER para ingresar lecturas o escriba 'EXIT' para salir: ")
        if opcion.strip().upper() == "EXIT":
            print("\nCerrando el sistema de telemetría de forma segura. ¡Hasta pronto!")
            break
            
        try:
            r = float(input("Ingrese Temperatura Fase R (°C): "))
            s = float(input("Ingrese Temperatura Fase S (°C): "))
            t = float(input("Ingrese Temperatura Fase T (°C): "))
        except ValueError:
            print("[ERROR] Entrada inválida. Debe ingresar valores numéricos reales.")
            continue

        # Procesamiento mediante las funciones modulares
        promedio = calcular_promedio_fases(r, s, t)
        alerta, fallas = validar_temperaturas([r, s, t], max_temp=75.0)

        # Visualización de resultados
        print("\n" + "-" * 40)
        print(f">> Promedio del Nodo Trifásico: {promedio:.2f} °C")
        
        if alerta:
            print(f">> ALERTA: {fallas} fase(s) superaron el límite crítico (75.0 °C)!")
        else:
            print(">> Estado del nodo: Estable (todas las fases dentro del rango operativo).")
        print("-" * 40)


if __name__ == '__main__':
    ejecutar_consola()
    