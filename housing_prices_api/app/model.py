import tensorflow as tf
import numpy as np

# Cargar el modelo
model = tf.keras.models.load_model('/models/housing_price_model.keras')

def predict_price(features):
    features = tf.convert_to_tensor([features])
    prediction = model.predict(features)
    return prediction[0]