from fastapi import FastAPI
from fastapi import FastAPI, File, UploadFile
from ..arquivos_py.soybean_predictor import SoybeanPrediciton
import tensorflow as tf


import streamlit as st
from typing import Union
import uuid
from PIL import Image
# Open the image form working directory


import numpy as np
import cv2

from ..arquivos_py.load_model import load_model_sb
from ..arquivos_py.preprocess import img_to_array

app = FastAPI()
app.state.model = load_model_sb()

IMAGEDIR = "raw_data/"

@app.post('/upload_image')
async def receive_image(img: UploadFile=File(...)):

    contents = await img.read()

    nparr = np.fromstring(contents, np.uint8)
    cv2_img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imwrite("result.jpg", cv2_img)

    cv2_img = Image.open('result.jpg')

    cv2_img = tf.image.resize(cv2_img, [128, 128])

    cv2_img = np.expand_dims(cv2_img, axis=0)

    result = app.state.model.predict(cv2_img)
    print(cv2_img.shape)
    print(result)
    numero_classe = list(result[0]).index(result.max())
    classe_lista = ['Broken soybeans', 'Immature soybeans', 'Intact soybeans',
                    'Skin-damaged soybeans', 'Spotted soybeans']
    porcent_pred = round(result.max()*100, 2)
    return {
        'class': classe_lista[numero_classe],
        'accuracy': porcent_pred
    }


@app.get("/")
def root():
    return {
        'greeting': 'Hello'
            }
