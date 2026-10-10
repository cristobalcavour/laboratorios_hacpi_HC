# Parámetros físicos constantes del circuito
L = 0.5       # Inductancia (Henrios)
C = 2e-6      # Capacitancia (Faradios) -> 2 uF
Vs = 12.0     # Voltaje de la fuente DC (Voltios)

def circuito_rlc(t, y, R):
    """
    Representación en variables de estado del circuito RLC serie.
    
    t: Tiempo (requerido por la firma de solve_ivp, aunque el sistema es autónomo)
    y: Arreglo de estado actual [V_c, dV_c/dt]
    R: Valor de la resistencia en Ohmios (pasado por args)
    
    Retorna:
    Lista con las derivadas [dy0/dt, dy1/dt]
    """
    y0, y1 = y
    
    dy0_dt = y1
    dy1_dt = (Vs - y0) / (L * C) - (R / L) * y1
    
    return [dy0_dt, dy1_dt]

# Condiciones Iniciales en t = 0
# El capacitor está completamente descargado (0V) y no hay corriente (0 V/s de cambio).
y0_inicial = [0.0, 0.0]