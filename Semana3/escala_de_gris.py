import cv2

img = cv2.imread('Bgris.png')
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Línea añadida para escala de grises

cv2.imshow('Imagen', gris)
cv2.imwrite('Bgris.png', gris)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Estudiante: Fernando Martinez