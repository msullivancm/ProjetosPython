#pip install opencv-python
import cv2 

webcam = cv2.VideoCapture()

try:
    if webcam.isOpened():
        validacao, frame = webcam.read()
        while validacao:
            validacao, frame = webcam.read()
            cv2.imshow("Video da Webcam", frame)
            key = cv2.waitKey(5)
            if key == 27: #ESC
                break
        cv2.imwrite("testeWebcam.png", frame)
    webcam.release()
    cv2.destroyAllWindows()
except:
    print("Não foi possível abrir a câmera.")