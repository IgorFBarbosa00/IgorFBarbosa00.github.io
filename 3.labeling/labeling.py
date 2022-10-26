# Nome:  labeling.py
# Autor: Igor Barbosa
# Última atualização : 24/10/2022

import cv2 as cv

img = cv.imread('./3.labeling/bolhas.png',cv.IMREAD_GRAYSCALE)
cv.namedWindow('Imagem selecionada')
cv.imshow('Imagem selecionada', img)

height, width = img.shape[:2]
print("A altura da imagem é: ", height)
print("A largura da imagem é: ", width)

#retirando as bolhas das bordas
#bordas verticais
for y in [0,width-1]:
    for x in range (height):
        if img[x,y] == 255:
            cv.floodFill(img, None, (y,x), 0)
#bordas horizontais
for x in [0,height-1]:
    for y in range (width):
        if img[x,y] == 255:
            cv.floodFill(img, None, (y,x), 0)
cv.imwrite('./3.labeling/bolhas_bordas_retiradas.png',img)
cv.namedWindow('Bordas Retiradas') 
cv.imshow('Bordas Retiradas', img)  

#contando o número total de bolhas
nbolhas = 0
for y in range (width):
    for x in range (height):
        if img[x,y] == 255:
            nbolhas = nbolhas + 1
            cv.floodFill(img, None, (y,x), nbolhas)
cv.imwrite('./3.labeling/bolhas_pintadas.png',img)
cv.namedWindow('Bolhas pintadas') 
cv.imshow('Bolhas pintadas', img)  

#contando o número total de bolhas com buracos
cv.floodFill(img, None, (0,0), 255)
cv.imwrite('./3.labeling/fundo_pintado.png',img)
cv.namedWindow('Fundo pintado') 
cv.imshow('Fundo pintado', img) 

nbolhasburacos = 0
for y in range (width):
    for x in range (height):
        if img[x,y] == 0:
            nbolhasburacos = nbolhasburacos + 1
            cv.floodFill(img, None, (y,x), 255)
cv.imwrite('./3.labeling/buracos_pintados.png',img)
cv.namedWindow('Buracos pintados') 
cv.imshow('Buracos pintados', img) 

print(f'Número total de bolhas: {nbolhas}')
print(f'Número total de bolhas com buracos: {nbolhasburacos}')

cv.waitKey()
cv.destroyAllWindows()