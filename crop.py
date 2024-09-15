import cv2
import numpy as np


image = cv2.imread('./img/DJI_0864.JPG')
#ancho x 4000
#alto y 2250
#2250 4000

#reporte
print(image.shape)
v=image.shape

imageOutA = image[0:600, 0:800]
imageOutB = image[600:1200, 800:1600]
imageOutC = image[1200:1800, 1600:2400]
imageOutD = image[1800:1800, 1600:2400]
imageOutE = image[2400:1800, 1600:2400]

#cv2.imshow("asd",imageOut)
filenameA = "./out/DSC_0043_Aasd.jpg"
filenameB = "./out/DSC_0043_Basd.jpg"
filenameC = "./out/DSC_0043_Casd.jpg"
filenameD = "./out/DSC_0043_Dasd.jpg"
filenameE = "./out/DSC_0043_Easd.jpg"

cv2.imwrite(filenameA, imageOutA)
cv2.imwrite(filenameB, imageOutB)
cv2.imwrite(filenameC, imageOutC)
cv2.imwrite(filenameD, imageOutD)
cv2.imwrite(filenameE, imageOutE)
