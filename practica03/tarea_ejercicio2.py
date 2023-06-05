# Ejercicio aplicativo 2
# 2.- Cargar la imagen insta.jpg. Introducir ruido gaussiano y ruido sal y pimienta a la
# imagen. Probar con distintos tipos de filtros hasta obtener una imagen de calidad
# para los ruidos anteriormente introducidos. ¿Qué tipo de filtro funciona mejor en
# cada uno de los casos anteriores? Justifica tu respuesta-.

# Importacion de librerias
import cv2
import numpy as np
from skimage.util import random_noise

# Cargar la imagen insta.jpg
img = cv2.imread("../images/insta.jpg")

# Agregar ruido guassiano
noise_gaussiano = random_noise(img, mode='gaussian', var=0.01)

# Agregar ruido sal y pimienta
noise_sal_pimienta = random_noise(img, mode='s&p', amount=0.01)

# Cambio a uint8 
noise_gaussiano = np.array(255*noise_gaussiano, dtype = 'uint8')
noise_sal_pimienta = np.array(255*noise_sal_pimienta, dtype = 'uint8')
#cv2.imshow("ruido_gaussiano",noise_gaussiano)
#cv2.imshow("ruido_sal_pimienta",noise_sal_pimienta)

# LAS IMAGENES CON RUIDO SON:
# noise_gaussiano
# noise_sal_pimienta

########## FILTRO PROMEDIADO ##########
# Aplicacion de filtro promediado para noise_gaussiano
filtro_promediado_g = cv2.blur(noise_gaussiano,(3,3))
#cv2.imshow("filtro_promedio_g",filtro_promediado_g)

# Aplicacion de filtro promediado para noise_sal_pimienta
filtro_promediado_sp = cv2.blur(noise_gaussiano,(3,3))
#cv2.imshow("filtro_promedio_sp",filtro_promediado_sp)

########## FILTRO MEDIANA ##########
# Aplicacion de filtro mediana para noise_gaussiano
filtro_mediana_g = cv2.medianBlur(noise_gaussiano, 3)
#cv2.imshow("filtro_mediana_g",filtro_mediana_g)

# Aplicacion de filtro mediana para noise_sal_pimienta
filtro_mediana_sp = cv2.medianBlur(noise_sal_pimienta, 3)
cv2.imshow("filtro_mediana_sp",filtro_mediana_sp)

########## FILTRO GAUSSIANO ##########
# Aplicacion de filtro gaussiano para noise_gaussiano
filtro_gaussiano_g = cv2.GaussianBlur(noise_gaussiano,(3,3),cv2.BORDER_DEFAULT)
cv2.imshow("filtro_gaussiano_g",filtro_gaussiano_g)

# Aplicacion de filtro gaussiano para noise_sal_pimienta
filtro_gaussiano_sp = cv2.GaussianBlur(noise_sal_pimienta,(3,3),cv2.BORDER_DEFAULT)
#cv2.imshow("filtro_gaussiano_sp",filtro_gaussiano_sp)

########## FILTRO SHAPENING ##########
filter_sharpen = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
# Aplicacion de filtro sharpening para noise_gaussiano
filtro_sharpening_g = cv2.filter2D(noise_gaussiano,-1,filter_sharpen)
#cv2.imshow("filtro_sharpening_g",filtro_sharpening_g)

# Aplicacion de filtro sharpening para noise_sal_pimienta
filtro_sharpening_sp = cv2.filter2D(noise_sal_pimienta,-1,filter_sharpen)
#cv2.imshow("filtro_sharpening_sp",filtro_sharpening_sp)

########## FILTRO HAT MEXICAN##########
filter_hat = np.array([[0,0,-1,0,0],[0,-1,-2,-1,0],[-1,-2,16,-2,-1],[0,-1,-2,-1,0],[0,0,-1,0,0]])
# Aplicacion de filtro hat para noise_gaussiano
filtro_hat_g = cv2.filter2D(noise_gaussiano,-1,filter_hat)
#cv2.imshow("filtro_hat_g",filtro_hat_g)

# Aplicacion de filtro hat para noise_sal_pimienta
filtro_hat_sp = cv2.filter2D(noise_sal_pimienta,-1,filter_hat)
#cv2.imshow("filtro_hat_sp",filtro_hat_sp)

cv2.waitKey(0)

'''
JUSTIFICACION DE RESPUESTA

**Para la imagen con ruido gaussiano
Para mejorar una imagen con ruido gaussiano, uno de los filtros más efectivos
es el filtro de desenfoque gaussiano.
El filtro de desenfoque gaussiano funciona al suavizar la imagen mediante la 
aplicación de un efecto de desenfoque basado en una distribución gaussiana. 
Este filtro es especialmente útil para reducir el ruido gaussiano.


**Para la imagen con ruido de sal y pimienta
Para reducir el ruido de sal y pimienta en una imagen, uno de los filtros más 
efectivos es el filtro de mediana. Este filtro reemplaza el valor de un píxel 
ruidoso por la mediana de los valores de los píxeles vecinos
'''
