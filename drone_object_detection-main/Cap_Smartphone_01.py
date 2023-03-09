import glob
import os
import cv2
import time
from PIL import Image






# Defina a resolução da tela do dispositivo Android
os.system("adb shell wm size 1080x1920")

# Defina o nome do arquivo de saída e o caminho onde será salvo
output_path = "c:\\lixo\\"
output_name = "tela"
output_format = ".png"

# Defina a taxa de captura de tela (em segundos)
capture_rate = 0

# Loop infinito para capturar a tela a cada intervalo de tempo
while True:
    # Capture a tela do dispositivo Android
    os.system("adb shell screencap -p /sdcard/screen.png")
    os.system("adb pull /sdcard/screen.png")

    # Leia a imagem capturada usando o OpenCV
    img = cv2.imread("screen.png")


    # Salve a imagem em um arquivo
    filename = output_path + output_name + str(time.time()) + output_format
    cv2.imwrite(filename, img)
    # Abra a imagem salva
    img = Image.open("screen.png")

    # Mostre a imagem na tela
    img.show()

      # Aguarde um intervalo de tempo antes de capturar a próxima tela
    time.sleep(capture_rate)

    # Feche a janela da imagem
    img.close()

    # Lista todos os arquivos de imagem na pasta de saída e ordena-os por data de modificação
    files = glob.glob(output_path + "*" + output_format)
    files.sort(key=os.path.getmtime)

    # Apaga todos os arquivos, exceto os 5 mais recentes
    for i in range(len(files) - 2):
        os.remove(files[i])
# Defina o comando para fechar o aplicativo de visualização de fotos no Windows
    close_command = "TASKKILL /F /IM microsoft.photos.exe"