# Nome:  laplgauss.py
# Autor: Igor Barbosa
# Última atualização : 24/10/2022
import cv2 as cv
import numpy as np

#máscaras dos filtros
gauss = np.array([[0.0625, 0.125, 0.0625]   #borramento
                ,[0.125, 0.25, 0.125]
                ,[0.0625, 0.125, 0.0625]])

laplacian = np.array([[0, -1, 0]
                     ,[-1, 4, -1]
                     ,[0, -1, 0]])


webcam = cv.VideoCapture(0)

if webcam.isOpened():
    validacao, frame = webcam.read()

    while validacao:
        validacao, frame = webcam.read()
        framegray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) #aquisição original
        cv.imshow("Aquisicao", framegray)

        framegaussiano = cv.filter2D(framegray, -1, gauss)
        cv.imshow('Borramento', framegaussiano)

        framelaplaciano = cv.filter2D(framegray, -1, laplacian)
        cv.imshow('Laplaciano', framelaplaciano)

        framelaplgauss = cv.filter2D(framegaussiano, -1, laplacian)
        cv.imshow('LaplGauss', framelaplgauss)

        key = cv.waitKey(5)
        if key == 27: #esc
            break
    cv.imwrite('./6.laplgauss/GrayFrame.png', framegray)
    cv.imwrite('./6.laplgauss/FrameGaussiano.png', framegaussiano)
    cv.imwrite('./6.laplgauss/FrameLaplaciano.png', framelaplaciano)
    cv.imwrite('./6.laplgauss/FrameLaplGauss.png', framelaplgauss)


webcam.release()
cv.destroyAllWindows