from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np

class SoybeanPrediciton:

    def __init__(self, image, model):
        self.image = image
        self.model = model

    def predict(self):

       img_array = img_to_array(self.image)
       x = np.expand_dims(img_array, axis=0)
       pred = self.model.predict(x)
       numero_classe = list(list(pred)[0]).index(pred.max())
       classe_lista = ['Broken soybeans', 'Immature soybeans', 'Intact soybeans',
                       'Skin-damaged soybeans', 'Spotted soybeans']
       return classe_lista[numero_classe]


def teste(teste):
    return print(teste)
