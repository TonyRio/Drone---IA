import cv2
from PIL import ImageGrab
import numpy as np

# Define o tamanho da janela de exibição
width, height = 640, 480

# Inicia a captura de tela em tempo real
while True:
    # Captura a tela do smartphone
    im = ImageGrab.grab()

    # Redimensiona a imagem para o tamanho da janela de exibição
    im = im.resize((width, height))

    # Converte a imagem para um array numpy
    im_array = np.array(im)

    # Converte o array numpy para o formato BGR (OpenCV)
    im_array = cv2.cvtColor(im_array, cv2.COLOR_RGB2BGR)

    # Exibe a imagem em tempo real
    cv2.imshow('Captura de tela', im_array)

    # Aguarda a tecla 'q' ser pressionada para sair do loop
    if cv2.waitKey(1) == ord('q'):
        break

# Libera a janela de exibição e encerra o programa
cv2.destroyAllWindows()