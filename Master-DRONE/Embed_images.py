from  mtcnn import MTCNN
from PIL import Image
from os import listdir
from os.path import isdir
from numpy import asarray, expand_dims
from tensorflow import keras
from tensorflow import _keras_module
from tensorflow.keras.models import load_model
import numpy as np

def load_face(filename): #, required_size =(160,160)):
    #carregando arquivo
    image = Image.open(filename)

    #converter par rgb

    image = image.convert("RGB")

    return asarray(image)

### CARREGANDO AS FACES DO DIRETORIO

def load_faces(directory_src):

    faces = [] ##list()

# Iterando arquivos

    for filename in listdir(directory_src):
        path = directory_src + filename

        try:
            faces.append(load_face(path))
        except:
            print(" *** ERRO na Imagem {} ***".format(path))

    return faces

def load_fotos(directory_src):
    x, y = [], []

    #iterar pastas por classse

    for subdir in listdir(directory_src):

        path= directory_src +subdir +"\\"

        if not isdir(path):
            continue

        faces = load_faces(path)

        labels = [subdir for _ in range(len(faces))]

         #Sumarizar o progresso

        print(">Carregadas %d faces da classe: %s " %(len(faces), subdir))


        x.extend(faces)
        y.extend(labels)

    return asarray(x), asarray(y)

#carregando todas as imagens

trainx, trainy = load_fotos(directory_src="E:\\DATA_SETS\\Faces\\")


model = load_model('facenet_keras.h5')
##Downgrade 2.8

def get_embedding(model, face_pixels):
mean , std = face_pixels.mean(), face_pixels.std()