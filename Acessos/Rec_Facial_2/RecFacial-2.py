import cv2  # Open-CV
import mediapipe as mp
import tensorflow  as tf
# inicializar o Open-CV

webcam = cv2.VideoCapture(0)
solucao_reconhecimento_rosto = mp.solutions.face_detection
reconhecedor_rostos = solucao_reconhecimento_rosto.FaceDetection()
desenho = mp.solutions.drawing_utils

while True:
    #ler informacoes da webcam
    verificador, frame = webcam.read()

    if not verificador:
        break
    #reconhecer os rostos na imagem
    lista_rostos = reconhecedor_rostos.process(frame)

    if lista_rostos.detections:
    # desenhar os rostos na imagem
        for rosto in lista_rostos.detections:
            desenho.draw_detection(frame, rosto)
    cv2.imshow("Rostos na Webcam", frame)

    #Quando apertar 'Esc' ele parar o Loop
    if cv2.waitKey(5) == 27:
        break

webcam.release()
cv2.destroyAllWindows()
