import cv2 

image = cv2.imread('./img/DSC_0043.jpg')
cv2.imshow('Original', image)
print(f'Dimensiones de la imagen original: {image.shape[:2]}')
cv2.waitKey(0)

cropped = image[100:240, 100:270]
cv2.imshow('Volante', cropped)
print(f'Dimensiones del recorte: {cropped.shape[:2]}')
cv2.waitKey(0)

cv2.destroyAllWindows()