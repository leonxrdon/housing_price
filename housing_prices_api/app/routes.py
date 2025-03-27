import logging
from flask import Blueprint, jsonify, request, Flask
from app.model import predict_price
from app.utils import calculate_features, scaler_predict
import numpy as np
import pandas as pd
from app.utils import scaler_values

from flask_cors import CORS

# Configurar el logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Definir Blueprint para las rutas
routes = Blueprint('routes', __name__)
CORS(routes)  # Permitir todas las solicitudes CORS

# Ruta GET para saludo
@routes.route('/hello', methods=['GET'])
def hello():
    logger.info("¡Hola! La API está funcionando correctamente. LOL")
    return jsonify({"message": "¡Hola! La API está funcionando correctamente. LOL"})

@routes.route('/predict', methods=['POST'])
def predict():
    logger.info("======= Predicción de precios =======")
    
    # Obtener los datos JSON
    data = request.get_json()
    if data is None or 'features' not in data:
        return jsonify({'error': 'No se recibieron datos JSON'}), 400
    
    # Obtener las características
    features = data['features']

    # Calcular las características faltantes
    complete_features = calculate_features(features)
    scaler_features = scaler_values(complete_features)

    # Intentar hacer la predicción
    try:
        # Transformar el featured a dataframe
        prediction = predict_price(scaler_features)
        prediction = scaler_predict(prediction)

    except Exception as e:
        logger.error(f"Error al hacer la predicción: {str(e)}")
        return jsonify({'error': f'Prediction failed: {str(e)}'}), 500
    
    # Retornar la predicción
    logger.info(f"Predicción: {prediction}")
    # Scaler
    logger.info(f"Predicción escalada: {prediction}")
    return jsonify({'predicted_price': prediction})
