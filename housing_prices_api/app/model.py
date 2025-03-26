import tensorflow as tf
import numpy as np
import pandas as pd
# Cargar el modelo
#model = tf.keras.models.load_model('models/housing_price_model.keras')
model = tf.keras.models.load_model('models/best_model.keras')

def predict_price(features):
    """"
    Función para hacer la predicción de precios de vivienda basada en las características proporcionadas.
    """
    feature_array = np.array(list(features)).reshape(1, -1)
    prediction = model.predict(feature_array)
    return prediction.reshape(1, -1) 