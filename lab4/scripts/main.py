import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
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
# Calculamos la resistencia crítica teórica
R_critica = 2 * np.sqrt(L / C)

# Nuestros 3 casos de estudio para R:
R_sub     = R_critica * 0.1   # Muy poca fricción eléctrica -> oscilará
R_crit    = R_critica         # El punto perfecto
R_sobre   = R_critica * 5.0   # Demasiada fricción eléctrica -> lentitud

print(f"Resistencia Subamortiguada:  {R_sub:.1f} Ohms")
print(f"Resistencia Crítica:         {R_crit:.1f} Ohms")
print(f"Resistencia Sobreamortiguada: {R_sobre:.1f} Ohms")

# Vector de tiempo: Simularemos los primeros 0.05 segundos con alta resolución
t_span = (0.0, 0.05)
t_eval = np.linspace(0, 0.05, 2000)

# Resolvemos los tres sistemas usando RK45 (Runge-Kutta)
sol_sub   = solve_ivp(circuito_rlc, t_span, y0_inicial, args=(R_sub,),   t_eval=t_eval, method='RK45')
sol_crit  = solve_ivp(circuito_rlc, t_span, y0_inicial, args=(R_crit,),  t_eval=t_eval, method='RK45')
sol_sobre = solve_ivp(circuito_rlc, t_span, y0_inicial, args=(R_sobre,), t_eval=t_eval, method='RK45')
plt.figure(figsize=(12, 7))

# Extraemos la primera fila (.y[0]) que corresponde al voltaje en el capacitor
plt.plot(sol_sub.t * 1000,   sol_sub.y[0],   color='tomato',       lw=2, label='Subamortiguado (R=100Ω)')
plt.plot(sol_crit.t * 1000,  sol_crit.y[0],  color='mediumseagreen', lw=2, label='Crítico (R=1000Ω)')
plt.plot(sol_sobre.t * 1000, sol_sobre.y[0], color='steelblue',    lw=2, label='Sobreamortiguado (R=5000Ω)')

# Línea de referencia del voltaje de la fuente (estado estacionario final)
plt.axhline(Vs, color='k', linestyle='--', alpha=0.6, label='Voltaje Fuente (12V)')

# Detalles estéticos de la gráfica
plt.title('Respuesta Transitoria del Voltaje Vc(t) en el Circuito RLC', fontsize=14, fontweight='bold')
plt.xlabel('Tiempo [ms]', fontsize=12)
plt.ylabel('Voltaje del Capacitor Vc(t) [V]', fontsize=12)
plt.legend(fontsize=10, loc='lower right')
plt.grid(True, alpha=0.4)
plt.xlim(0, 50)

plt.tight_layout()
plt.show()