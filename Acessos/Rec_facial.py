import os
import cv2
import time
import face_recognition

# Defina a resolução da tela do dispositivo Android
os.system("adb shell wm size 1080x1920")

# Defina o nome do arquivo de saída e o caminho onde será salvo
output_path = "lixo/"
output_name = "tela"
output_format = ".png"

# Defina a taxa de captura de tela (em segundos)
capture_rate = 0.2

# Carregue as imagens das pessoas conhecidas
known_face_encodings = []
known_face_names = []
for filename in os.listdir("C:\Faces_family_Flip"):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image = face_recognition.load_image_file("C:\Faces_family_Flip/" + filename)
        face_encoding = face_recognition.face_encodings(image)[0]
        known_face_encodings.append(face_encoding)
        known_face_names.append(os.path.splitext(filename)[0])

# Loop infinito para capturar a tela a cada intervalo de tempo
while True:
    # Capture a tela do dispositivo Android
    os.system("adb shell screencap -p /sdcard/screen.png")
    os.system("adb pull /sdcard/screen.png")

    # Leia a imagem capturada usando o OpenCV
    img = cv2.imread("screen.png")

    # Converta a imagem para escala de cinza para melhorar o desempenho do reconhecimento facial
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Localize os rostos na imagem usando o OpenCV
    face_locations = face_recognition.face_locations(gray)

    # Para cada rosto encontrado, tente identificar a pessoa usando o reconhecimento facial
    for (top, right, bottom, left) in face_locations:
        # Extrair a imagem do rosto
        face_image = img[top:bottom, left:right]

        # Converta a imagem do rosto para RGB para o reconhecimento facial
        face_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB)

        # Calcule a codificação facial do rosto
        face_encoding = face_recognition.face_encodings(face_image)

        # Tente identificar a pessoa usando a codificação facial
        if len(face_encoding) > 0:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding[0])
            name = "Unknown"

            # Se houver uma correspondência, use o nome correspondente
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            # Desenhe um retângulo em torno do rosto e adicione o nome da pessoa
            cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(img, name, (left, top - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    # Salve a imagem em um arquivo
    filename = output_path + output_name + str(time.time()) + output_format
    cv2.imwrite(filename, img)