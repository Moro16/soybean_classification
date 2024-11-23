from tensorflow.keras.preprocessing.image import load_img
import numpy as np

#Carrega uma imagem e devolve um array

def img_to_array(path):
    img = load_img(path, target_size=(128, 128))
    img_array = img_to_array(img)
    expanded_img = np.expand_dims(img_array, axis=0)

    return expanded_img
