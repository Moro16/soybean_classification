from tensorflow.keras.models import load_model

def load_model_sb():
    model = load_model("model_val_loss:0.3586-val_accuracy:0.9048")

    return model
