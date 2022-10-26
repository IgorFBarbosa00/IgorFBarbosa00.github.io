# Nome:  regions.py
# Autor: Igor Barbosa
# Última atualização : 23/10/2022

import cv2 as cv

img = cv.imread('./1.regions/OpenCV_Logo.png',cv.IMREAD_GRAYSCALE)
cv.namedWindow('Imagem selecionada')
cv.imshow('Imagem selecionada', img)

height, width = img.shape[:2]
print("A altura da imagem é: ", height)
print("A largura da imagem é: ", width)


while not (px1 := input('Coordenada X do P1: ')).isdigit() or (px1:=int(px1)) < 0 or px1 > height:
    print('Valor INVÁLIDO')
while not (py1 := input('Coordenada Y do P1: ')).isdigit() or (py1:=int(py1)) < 0 or py1 > width:
    print('Valor INVÁLIDO')
while not (px2 := input('Coordenada X do P2: ')).isdigit() or (px2:=int(px2)) < 0 or px2 > height:
    print('Valor INVÁLIDO')
while not (py2 := input('Coordenada Y do P2: ')).isdigit() or (py2:=int(px2)) < 0 or py2 > width:
    print('Valor INVÁLIDO')


for x in range (min(px1,px2),max(px1,px2)):
    for y in range (min(py1,py2),max(py1,py2)):
        img[x,y] = 255 - img[x,y]


cv.namedWindow('Resultado') 
cv.imshow('Resultado', img)  
cv.waitKey()
cv.imwrite('./1.regions/Output.png',img)
cv.destroyAllWindows()