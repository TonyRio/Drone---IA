import os
import cv2
# Defina a resolução da câmera do dispositivo Android
os.system("adb shell am start -a android.media.action.VIDEO_CAPTURE --ez android.intent.extra.VIDEO_QUALITY 1")

# Inicie a captura de vídeo
cap = cv2.VideoCapture(0)

# Loop para mostrar o vídeo capturado em tempo real
while True:

    # Capture um frame do vídeo
    ret, frame = cap.read()


    # Mostre o frame capturado em uma janela
    if frame is not None and frame.shape[0] > 0 and frame.shape[1] > 0:
      cv2.imshow('Capturando Video do Smartphone', frame)


    # Aguarde 1 milissegundo e verifique se a tecla 'q' foi pressionada para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libere a captura de vídeo e feche a janela
cv2.imshow

cap.release()
cv2.destroyAllWindows()