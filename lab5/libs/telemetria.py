import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# 1. Generador de Datos Tabulares (CSV)
np.random.seed(42)
fechas = pd.date_range('2026-10-01', periods=200, freq='h')
df_sim = pd.DataFrame({
    'fecha': fechas,
    'voltaje_V': np.random.normal(12.0, 0.5, 200),
    'temperatura_C': np.random.normal(20.0, 5.0, 200),
    'estado_bateria': np.random.choice(['OK', 'WARNING', 'CRITICAL'], 200, p=[0.8, 0.15, 0.05])
})
# Inyectar ruido (Datos nulos / NaN) para que el estudiante los limpie
df_sim.loc[20:25, 'voltaje_V'] = np.nan
df_sim.loc[150:160, 'temperatura_C'] = np.nan
df_sim.to_csv('telemetria_satelite.csv', index=False)

# 2. Generador de Imagen Sintética (NumPy)
# Imagen 200x200 de 3 canales (RGB)
img_sim = np.zeros((200, 200, 3), dtype=np.uint8)
# Crear un gradiente simple en cada canal
for i in range(200):
    img_sim[:, i, 0] = int(255 * (i / 200))      # Canal Rojo (aumenta hacia la derecha)
    img_sim[i, :, 1] = int(255 * (i / 200))      # Canal Verde (aumenta hacia abajo)
    img_sim[:, :, 2] = 128                       # Canal Azul (constante)

plt.imsave('captura_satelite.jpg', img_sim)
print("Archivos de prueba creados: 'telemetria_satelite.csv' y 'captura_satelite.jpg'")