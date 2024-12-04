from tensorflow.keras.models import load_model

def load_model_sb():
    model = load_model("model_val_loss0.3586-val_accuracy0.9048")

    return model

def load_model_corn():
    model = load_model("model_corn_val_loss0.0.8671-val_accuracy0.6985")

    return model
