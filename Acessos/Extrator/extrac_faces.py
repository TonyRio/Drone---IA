from  mtcnn import MTCNN
from PIL import Image
from os import listdir
from os.path import isdir
from numpy import asarray

detector = MTCNN()

def extrair_face(arquivo, size=(160,160)):

    img =  Image.open(arquivo) # Caminho completo

    img =  img.convert('RGB') # Converter em RGB

    array = asarray(img)

    results = detector.detect_faces(array)
    x1, y1 , width, height = results[0] ['box']

    x2, y2 = x1 + width, y1 + height # dimensiona o tamanho da face

    face = array[y1:y2,x1:x2]

    image = Image.fromarray(face) # mudar o Array para o tamanho padrao
    image = image.resize(size)

    return image

def flip_image(image):
    img =image.transpose(Image.FLIP_LEFT_RIGHT)
    return img


def load_fotos(directory_src, directory_target):

    for filename in listdir(directory_src):
        path = directory_src + filename

        path_tg = directory_target + filename

        path_tg_flip = directory_target +  "flip-" + filename

        try:
            face = extrair_face(path)

            flip = flip_image(face)
            face.save(path_tg, "JPEG", quality=100, optimize=True, progressive=True)
            flip.save(path_tg_flip, "JPEG", quality=100, optimize=True, progressive=True)

        except:
            print("erro na Imagem {}".format(path))

def load_dir(directoy_src,directory_target):
    for subdir in listdir(directoy_src):

        path = directoy_src + subdir + "\\"

        path_tg = directory_target + subdir + "\\"

        if not isdir(path):
            continue

        load_fotos (path, path_tg)

if __name__ == '__main__':
    load_dir("C:\\DATA_SETS\\Faces_family\\",
        "C:\\DATA_SETS\\Faces_family_Flip\\")

    ### final
