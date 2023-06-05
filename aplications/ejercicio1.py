# Importamos las librerias necesarias
import cv2
import matplotlib.pyplot as plt
import numpy as np

# 1.- Lea una imagen Bloom.jpg y visualice
# Leemos la imagen en BGR
img_BGR = cv2.imread('bloom.jpg')
plt.subplot(2,3,1)
plt.imshow(img_BGR)
#cv2.imshow("img_BGR",img_BGR)

#----------------------------------------------

# 2.- Convierta a RGB y muestre la imagen
# Convertir al formato RGB
img_RGB = cv2.cvtColor(img_BGR,cv2.COLOR_BGR2RGB)
plt.subplot(2,3,2)
plt.imshow(img_RGB)
# plt.show()
#cv2.imshow("img_RGB",img_RGB)

#-----------------------------------------------

# 3.- Convierta la imagen a HSV
# Convertir de RGB a HSV
img_HSV = cv2.cvtColor(img_BGR,cv2.COLOR_BGR2HSV)
plt.subplot(2,3,3)
plt.imshow(img_HSV)
# plt.show()
#cv2.imshow("img_RGB2HSV",img_RGB2HSV)

#------------------------------------------------

# 4.- Dividir la imagen en los planos h, s y v
h, s, v = cv2.split(img_HSV)

#-----------------------------------------------

# 5.- Plotee el histograma del plano v
plt.subplot(2,3,4)
plt.hist(v.flatten(), bins=256, range=[0, 256], color='r')
# plt.show()

#-----------------------------------------------

# 6.- Ecualice el histograma en el canal v y plotee
plt.subplot(2,3,5)
v_ecua = cv2.equalizeHist(v)
plt.hist(v_ecua.flatten(), bins=256, range=[0, 256], color='r')
# plt.show()

#-----------------------------------------------

# 7.- Volver a mezclar los tres planos para obtener una imagen HSV actualizada y visualizar
img_HSV_actua = cv2.merge([h, s, v_ecua])

#-----------------------------------------------

# 8.- Convierta a RGB nuevamente y muestre la imagen
plt.subplot(2,3,6)
img_RGB_actua = cv2.cvtColor(img_HSV_actua, cv2.COLOR_HSV2RGB)
plt.imshow(img_RGB_actua)
plt.show()

