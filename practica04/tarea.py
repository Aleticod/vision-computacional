import cv2
import matplotlib.pyplot as plt
import numpy as np


# HISTOGRAMA DE LA IMAGEN A COLOR
import cv2
import numpy as np
from matplotlib import pyplot as plt
# Leer la imagen
img = cv2.imread('./paisaje.jpg')
color = ('b','g','r')

# Calcular el histograma
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,255])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
# plt.show()


# cargamos la imagen de origen en BGR usando imread()
img = cv2.imread('./paisaje.jpg')

# convertimos la imagen a escala de grises (espacio img_yuv)
# usando el metodo cv2.cvtColor(image, flag) 
img_yuv = cv2.cvtColor(img,cv2.COLOR_BGR2YUV)

# aplicamos ecualizacion de histograma 
# usando la funcion OpenCV cv2.equalizeHist()
img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])

# Cnvertimos el color del espacio YUV a BGR
hist_eq = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

# Mostrar ambas imágenes (original y ecualizada)
# utilizando  la función cv2.imshow() y 
# hstack() del módulo numpy para apilar ambos valores de imagen
cv2.imshow('Uso de ecualizacion', np.hstack((img, hist_eq)))
cv2.waitKey(0)

