FROM python:3.10.6

COPY requirements.txt /requirements.txt
# Soybean model
COPY model_val_loss0.3586-val_accuracy0.9048 /model_val_loss0.3586-val_accuracy0.9048
# Corn model
COPY model_corn_val_loss0.0.8671-val_accuracy0.6985 /model_corn_val_loss0.0.8671-val_accuracy0.6985
COPY soybean_prediction /soybean_prediction
COPY setup.py /setup.py
COPY style.css /style.css

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install -e .
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

# CMD ["uvicorn", "soybean_prediction.api.fast:app"]
CMD uvicorn soybean_prediction.api.fast:app --host 0.0.0.0 --port $PORT
