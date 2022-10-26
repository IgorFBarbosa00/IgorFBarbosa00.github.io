# Nome:  trocaregioes.py
# Autor: Igor Barbosa
# Última atualização : 24/10/2022

import cv2 as cv
import numpy as np

img = cv.imread('./2.trocaregioes/OpenCV_Logo.png',cv.IMREAD_COLOR)
cv.namedWindow('Imagem selecionada')
cv.imshow('Imagem selecionada', img)


height, width = img.shape[:2]
h_centro, w_centro = height//2 , width//2
#print(height, width)                       #teste
#print(h_centro, w_centro)


q1 = img[0:h_centro, w_centro:width]
#h1, w1 = q1.shape[:2]                      #teste Q1
#print(h1,w1)
#cv.namedWindow('Quadrante 1')
#cv.imshow('Quadrante 1', q1)

q2 = img[0:h_centro, 0:w_centro]
#h2, w2 = q2.shape[:2]                      #teste Q2
#print(h2,w2)
#cv.namedWindow('Quadrante 2')
#cv.imshow('Quadrante 2', q2)

q3 = img[h_centro:height, 0:w_centro]
#h3, w3 = q3.shape[:2]                      #teste Q3
#print(h3,w3)
#cv.namedWindow('Quadrante 3')
#cv.imshow('Quadrante 3', q3)

q4 = img[h_centro:height, w_centro:width]
#h4, w4 = q4.shape[:2]                      #teste Q4
#print(h4,w4)
#cv.namedWindow('Quadrante 4')
#cv.imshow('Quadrante 4', q4)

q43 = np.concatenate((q4,q3),axis=1)
q12 = np.concatenate((q1,q2),axis=1)
img = np.concatenate((q43,q12),axis=0)


cv.namedWindow('Resultado') 
cv.imshow('Resultado', img)  
cv.waitKey()
cv.imwrite('./2.trocaregioes/Output.png',img)
cv.imwrite('./2.trocaregioes/Quadrante1.png',q1)
cv.imwrite('./2.trocaregioes/Quadrante2.png',q2)
cv.imwrite('./2.trocaregioes/Quadrante3.png',q3)
cv.imwrite('./2.trocaregioes/Quadrante4.png',q4)
cv.destroyAllWindows()