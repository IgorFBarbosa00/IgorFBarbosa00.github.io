import cv2 as cv

webcam = cv.VideoCapture(0)

if webcam.isOpened():
    validacao, frame = webcam.read()

    while validacao:
        validacao, frame = webcam.read()
        cv.imshow("Video da Webcam", frame)
        key = cv.waitKey(5)
        if key == 27: #esc
            break
    cv.imwrite('./camera/Finish.png', frame)

webcam.release()
cv.destroyAllWindows
