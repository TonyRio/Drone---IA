import os
import cv2
import numpy as np
import time

# Defina a resolução da tela do dispositivo Android
os.system("adb shell wm size 1080x1920")

# Defina o nome do arquivo de saída e o caminho onde será salvo
#output_path = "C:\lixo\\"
#output_name = "tela"
#output_format = ".png"

# Defina a taxa de captura de tela (em segundos)
capture_rate = 0.1

# Defina o classificador de reconhecimento de rosto do OpenCV
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Loop infinito para capturar a tela a cada intervalo de tempo
while True:
    # Capture a tela do dispositivo Android
    os.system("adb shell screencap -p /sdcard/screen.png")
    os.system("adb pull /sdcard/screen.png")

    # Leia a imagem capturada usando o OpenCV
    img = cv2.imread("screen.png")

    # Converta a imagem para escala de cinza para melhorar o desempenho do classificador
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Use o classificador de reconhecimento de rosto do OpenCV para detectar rostos na imagem
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Salve a imagem com os retângulos desenhados em um arquivo
    #output_file = output_path + output_name + str(int(time.time())) + output_format
    #cv2.imwrite(output_file, img)

    # Espere o tempo definido antes de capturar a próxima tela
    time.sleep(capture_rate)