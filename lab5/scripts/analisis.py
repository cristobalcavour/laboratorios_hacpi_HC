
import matplotlib.pyplot as plt
import numpy as np

# TAREA 2.1: Leer la imagen
imagen = plt.imread('captura_satelite.jpg')

# TAREA 2.2: Imprimir las dimensiones
print("Dimensiones de la imagen:", imagen.shape)

# TAREA 2.3: Mostrar la imagen completa
plt.imshow(imagen)
plt.title("Imagen Original")
plt.show()

# TAREA 2.4: Extraer y graficar el canal rojo
canal_rojo = imagen[:, :, 0]

plt.imshow(canal_rojo, cmap='Reds')
plt.colorbar()
plt.title("Filtro: Canal Rojo")
plt.show()

# TAREA 2.5: Recortar la región central
recorte = imagen[50:150, 50:150, :]

plt.imshow(recorte)
plt.title("Recorte Central (Region of Interest)")
plt.show()

print("Dimensiones del canal rojo:", canal_rojo.shape)
print("Dimensiones del recorte:", recorte.shape)