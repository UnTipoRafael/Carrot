import cv2
import numpy as np
import os
from tqdm import tqdm
import time

columnas    =   [0, 450, 900,  1350, 1800, 2250]
filas       =   [0, 800, 1600, 2400, 3200, 4000]

fotos=os.listdir('./img/in/')
#print(fotos)

for fotito in tqdm(fotos, mininterval=1, unit="archivos"):
        img=1
       # tqdm(img ,fotito, unit:"foto")
        image = cv2.imread('./img/in/'+fotito)
        #2250x4000 archivo de drone dji 2.7k mavic mini 1
        #800x450 recorte de salida dividido en 5 para q encaje

        #reporte
        #print(image.shape)
        #v=image.shape 
        for i in range(5):
            for e in range(5):
                filename = "./img/out/"+fotito[:-4]+"_"+str(img)+".jpg"
                imageOut = image[columnas[i]:columnas[i+1], filas[e]:filas[e+1]]
                #print(columnas[i],columnas[i+1], filas[e],filas[e+1])
                cv2.imwrite(filename, imageOut)
                #print(filename)
                img=img+1
