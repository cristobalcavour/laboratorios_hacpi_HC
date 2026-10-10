"""
Módulo de Telemetría Térmica para Sistemas Trifásicos.
Proporciona funciones para el cálculo de medias aritméticas y validación de umbrales.
"""

def calcular_promedio_fases(r: float, s: float, t: float) -> float:
    """Calcula el promedio aritmético exacto de las tres fases."""
    return (r + s + t) / 3.0


def validar_temperaturas(temperaturas: list[float], max_temp: float = 75.0) -> tuple[bool, int]:
    """
    Evalúa una lista de temperaturas frente a un umbral máximo admisible.
    
    Retorna:
        tuple[bool, int]: (sobrepasado, conteo_fallas)
    """
    conteo_fallas = 0
    for temp in temperaturas:
        if temp > max_temp:
            conteo_fallas += 1
            
    sobrepasado = conteo_fallas > 0
    return sobrepasado, conteo_fallas


if __name__ == '__main__':
    # Pruebas de validación local (se ignoran al ser importado)
    print("--- PRUEBAS UNITARIAS DE TELEMETRIA.PY ---")
    prom_test = calcular_promedio_fases(50.0, 60.0, 70.0)
    print(f"Prueba promedio (50, 60, 70): {prom_test:.2f} °C")
    
    alerta_test, fallas_test = validar_temperaturas([45.0, 80.0, 52.0])
    print(f"Prueba validación [45, 80, 52]: Alerta={alerta_test}, Fallas={fallas_test}")