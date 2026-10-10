
import pandas as pd

# TAREA 1.1: Cargar el CSV
df = pd.read_csv('telemetria_satelite.csv')

# TAREA 1.2: Mostrar las primeras 5 filas
print(df.head())

# TAREA 1.3: Identificar datos nulos
print(df.isnull().sum())

# TAREA 1.4: Limpiar datos faltantes
df['voltaje_V'] = df['voltaje_V'].fillna(df['voltaje_V'].mean())
df = df.dropna(subset=['temperatura_C'])

# Comprobar que ya no hay datos nulos
print(df.isnull().sum())

# TAREA 1.5: Transformar fechas y agrupar
df['fecha'] = pd.to_datetime(df['fecha'])
df = df.set_index('fecha')

promedio_temperatura = df.groupby('estado_bateria')['temperatura_C'].mean()

print(promedio_temperatura)