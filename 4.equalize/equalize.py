# Nome:  equalize.py
# Autor: Igor Barbosa
# Última atualização : 25/10/2022
import cv2 as cv
import numpy as np

webcam = cv.VideoCapture(0)


if webcam.isOpened():
    validacao, frame = webcam.read()

    while validacao:
        validacao, frame = webcam.read()
        framegray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        histEqualize = cv.equalizeHist(framegray) #imagem Equalizada
        
        #Geração dos histogramas
        histSize = 64
        hist = cv.calcHist(framegray, [0], None, [histSize], (0,255), False)
        histEqual = cv.calcHist(histEqualize, [0], None, [histSize], (0,255), False)

        #Tamanho dos histogramas
        hist_w = 200
        hist_h = 100
        bin_w = int(round(hist_w/histSize))

        #Matrizes dos histogramas
        histImage = np.zeros((hist_h, hist_w), dtype=np.uint8)
        histImageEqual = np.zeros((hist_h, hist_w), dtype=np.uint8)

        #Normalização dos histogramas
        cv.normalize(hist, hist, 0, hist_h, norm_type=cv.NORM_MINMAX)
        cv.normalize(histEqual, histEqual, 0, hist_h, norm_type=cv.NORM_MINMAX)

        for i in range(1, histSize):
            cv.line(histImage, (bin_w*(i), hist_h - int(hist[i])),
                               (bin_w*(i), hist_h),
                               (255, 255, 255), thickness=2)
            cv.line(histImageEqual, (bin_w*(i), hist_h - int(histEqual[i])),
                               (bin_w*(i), hist_h),
                               (255, 255, 255), thickness=2)

        for x in range (0, hist_h-1):
            for y in range (0, hist_w-1):
                framegray[x,y] = histImage[x,y]
                histEqualize[x,y] = histImageEqual[x,y]

        cv.imshow('Hist', framegray)
        cv.imshow('Equalize',histEqualize)
        key = cv.waitKey(5)
        if key == 27: #esc
            break

cv.imwrite('./4.Equalize/Entrada.png', framegray)
cv.imwrite('./4.Equalize/EntradaEqualizada.png', histEqualize)
webcam.release()
cv.destroyAllWindows