from fastapi import FastAPI
from fastapi import FastAPI, File, UploadFile
import tensorflow as tf


import streamlit as st
from typing import Union
from PIL import Image

import numpy as np
import cv2

from ..arquivos_py.load_model import load_model_sb, load_model_corn


app = FastAPI()
app.state.model_1 = load_model_sb()
app.state.model_2 = load_model_corn()


IMAGEDIR = "raw_data/"

@app.post('/upload_image_sb')
async def receive_image(img: UploadFile=File(...)):

    contents = await img.read()

    nparr = np.fromstring(contents, np.uint8)
    cv2_img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imwrite("result.jpg", cv2_img)

    cv2_img = Image.open('result.jpg')

    cv2_img = tf.image.resize(cv2_img, [128, 128])

    cv2_img = np.expand_dims(cv2_img, axis=0)

    result = app.state.model_1.predict(cv2_img)
    print(cv2_img.shape)
    print(result)
    numero_classe = list(result[0]).index(result.max())
    classe_lista = ['Broken', 'Immature', 'Intact',
                    'Skin-damaged', 'Spotted']
    porcent_pred = round(result.max()*100, 2)
    return {
        'class': classe_lista[numero_classe],
        'accuracy': porcent_pred
    }

@app.post('/upload_image_corn')
async def receive_image(img: UploadFile=File(...)):

    contents = await img.read()

    nparr = np.fromstring(contents, np.uint8)
    cv2_img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imwrite("result.jpg", cv2_img)

    cv2_img = Image.open('result.jpg')

    cv2_img = tf.image.resize(cv2_img, [192, 192])

    cv2_img = np.expand_dims(cv2_img, axis=0)

    result = app.state.model_2.predict(cv2_img)
    numero_classe = list(result[0]).index(result.max())
    classe_lista = ['Broken', 'Discolored', 'Pure',
                    'Silkcut']
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
