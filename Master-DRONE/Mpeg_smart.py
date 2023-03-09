import cv2
import numpy as np
import tensorflow as tf

# Carregando o modelo YOLOv3 pré-treinado
model = tf.keras.models.load_model('yolov3.weights')

# Definindo as classes que o modelo pode detectar
classes = ['pessoa', 'carro', 'bicicleta', ...]

# Definindo as cores para cada classe
colors = [[0, 255, 0], [0, 0, 255], [255, 0, 0], ...]

# Iniciando a captura de vídeo da câmera
cap = cv2.VideoCapture(0)

while True:
    # Capturando um quadro do vídeo
    ret, frame = cap.read()

    if not ret:
        break

    # Redimensionando o quadro para o tamanho esperado pelo modelo
    resized_frame = cv2.resize(frame, (416, 416))

    # Normalizando os valores dos pixels para o intervalo [0, 1]
    normalized_frame = resized_frame / 255.0

    # Adicionando uma dimensão extra para representar o lote (batch)
    batched_frame = np.expand_dims(normalized_frame, axis=0)

    # Executando a detecção de objetos no quadro usando o modelo YOLOv3
    detections = model.predict(batched_frame)

    # Convertendo as detecções em caixas delimitadoras e classes
    boxes, scores, classes = tf.keras.backend.ctc_decode(detections,
                                                         tf.ones((detections.shape[0], 1)),
                                                         [detections.shape[1]] * detections.shape[0],
                                                         greedy=True)

    boxes = boxes[0].numpy()
    scores = scores[0].numpy()
    classes = classes[0].numpy()

    # Desenhando as caixas delimitadoras e etiquetas para as detecções
    for box, score, class_id in zip(boxes, scores, classes):
        if score < 0.5:
            continue

        color = colors[class_id]
        label = f'{classes[class_id]}: {score:.2f}'

        x1, y1, x2, y2 = box

        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Exibindo o quadro resultante na janela
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) == ord('q'):
        break

# Finalizando a captura de vídeo e fechando a janela
cap.release()
cv2.destroyAllWindows()
