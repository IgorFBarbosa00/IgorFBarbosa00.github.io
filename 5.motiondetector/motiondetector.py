# Nome:  motiondetector.py
# Autor: Igor Barbosa
# Última atualização : 25/10/2022
import cv2 as cv
import numpy as np
import imageio

gif = []

webcam = cv.VideoCapture(0)

#teste com a câmera
if webcam.isOpened():
    validacao, frame = webcam.read()

    while validacao:
        validacao, quadro1 = webcam.read() #frame anterior
        frame1 = cv.cvtColor(quadro1, cv.COLOR_BGR2GRAY)
        cv.waitKey(25)
        quadro2 = webcam.read()[1]         #frame atual
        frame2 = cv.cvtColor(quadro2, cv.COLOR_BGR2GRAY)
        
        #Geração dos histogramas
        histSize = 64
        histframe1 = cv.calcHist(frame1, [0], None, [histSize], (0,255), False)
        histframe2 = cv.calcHist(frame2, [0], None, [histSize], (0,255), False)

        #Comparação dos histogramas
        limiar = cv.compareHist(histframe1, histframe2, cv.HISTCMP_CORREL)
        if limiar < 0.94 : #limiar definido para detecção de movimento
            cv.putText(frame2, 'Motion Detected!', (300,400), cv.FONT_ITALIC, 1, (0,0,0), thickness=2)

        #Exibição do frame atual capturado com suas respectivas informações
        hist_w = 200
        hist_h = 100
        bin_w = int(round(hist_w/histSize))
        histImage = np.zeros((hist_h, hist_w), dtype=np.uint8)
        cv.normalize(histImage, histImage, 0, hist_h, norm_type=cv.NORM_MINMAX)
        for i in range(1, histSize):
            cv.line(histImage, (bin_w*(i), hist_h - int(histframe1[i])),
                               (bin_w*(i), hist_h),
                               (255, 255, 255), thickness=2)

        for x in range (0, hist_h-1):
            for y in range (0, hist_w-1):
                frame2[x,y] = histImage[x,y]
        
        #cv.imshow('Webcam1', frame1)
        cv.imshow('Webcam', frame2)
        key = cv.waitKey(5)
        if key == 27: #esc
            break

        #Ao apertar a tecla "a", o programa irá armazenar os frames para gerar um gif
        if key == ord("a"):
            gif.append(frame2)
        
webcam.release()
cv.destroyAllWindows
#geração do gif através da biblioteca imageio
print("Saving GIF file")
with imageio.get_writer("./5.motiondetector/resultado.gif", mode="I") as writer:
    for idx, frame in enumerate(gif):
        print("Adding frame to GIF file: ", idx + 1)
        writer.append_data(frame)