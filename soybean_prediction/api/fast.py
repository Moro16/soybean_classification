from fastapi import FastAPI
from fastapi import FastAPI, File, UploadFile

from typing import Union

import uuid

from ..arquivos_py.load_model import load_model
from ..arquivos_py.preprocess import img_to_array

app = FastAPI()

IMAGEDIR = "raw_data/"

@app.get("/upload")
async def create_upload_file(file: UploadFile = File(...)):

    file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()

    with open (f"{IMAGEDIR}/{file.filename}", "wb") as f:
        f.write(contents)

    return {"filename"}/{file.filename}

@app.get("/predict")
def predict(path):

    model = load_model()
    array = img_to_array(path)

    pred = model.predict(array)

    index_class = list(pred[0]).index(pred.max())
    list_class = ['Broken soybeans',
                  'Immature soybeans',
                  'Intact soybeans',
                  'Skin-damaged soybeans',
                  'Spotted soybeans']

    class_pred = list_class[index_class]
    porcent_pred = round(pred.max()*100, 2)

    return {
        'class': class_pred,
        'porcent': porcent_pred
            }


@app.get("/")
def root():
    return {
        'greeting': 'Hello'
            }
