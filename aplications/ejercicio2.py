# Importamos las librerias
import numpy as np

# Definimos el factor de escala
factor = 3

# Definimos matriz de la imagen inicial
img_inicial = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

# Obtenemos las dimensiones de la matriz original
alto_orig, ancho_orig = img_inicial.shape

# Obtenemos las nuevas dimensiones de la matriz escalada
alto_esca = alto_orig * factor
ancho_esca = ancho_orig * factor

# Creamos una matriz vacia con el tamanio de la imagen escalada
img_final = np.zeros((alto_esca, ancho_esca))

# Bucle para asignar el valor del vecino más cercano a cada píxel escalado
for i in range(alto_esca):
    for j in range(ancho_esca):
        i_img_orig = i // factor
        j_img_orig = j // factor
        # Vecino mas cercano
        img_final[i, j] = img_inicial[i_img_orig, j_img_orig]

# Mostrar la matriz de la imagen escalada
print(img_final)
