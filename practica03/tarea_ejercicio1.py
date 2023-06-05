# Ejercicio aplicativo 1
# 1.-A plicar un filtro de la media a la imagen lena_ruido.jpg. Usar una matriz de 31x31
# elementos como filtro, del siguiente estilo:

# Importacion librerias
import cv2

# Cargar la imagen de lena con ruido
img1 = cv2.imread("../images/lena_ruido.jpg")
cv2.imshow("imagen_real",img1)

# Aplicamos el filtro promediado de 31 x 31
blurred = cv2.blur(img1,(31,31)) 
cv2.imshow("filtro_31x31",blurred)
cv2.waitKey(0)