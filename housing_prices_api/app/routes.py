from flask import Blueprint, jsonify, request
from app.model import predict_price

# Definir Blueprint para las rutas
routes = Blueprint('routes', __name__)

# Ruta GET para saludo
@routes.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "¡Hola! La API está funcionando correctamente. LOL"})

@routes.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    # Validar que la clave 'features' esté presente en el JSON
    if not data or 'features' not in data:
        return jsonify({'error': 'No features provided'}), 400
    
    # Obtener las características, y si no están, asignarles un valor por defecto
    features = data['features']
    print("*" * 50)
    print(features)
    print("*" * 50)
    area = features.get('area', None)
    bedrooms = features.get('bedrooms', None)
    bathrooms = features.get('bathrooms', None)
    stories = features.get('stories', None)
    mainroad = features.get('mainroad', None)
    guestroom = features.get('guestroom', None)
    basement = features.get('basement', None)
    hotwaterheating = features.get('hotwaterheating', None)
    airconditioning = features.get('airconditioning', None)
    parking = features.get('parking', None)
    prefarea = features.get('prefarea', None)
    furnishingstatus_semi_furnished = features.get('furnishingstatus_semi-furnished', None)
    furnishingstatus_unfurnished = features.get('furnishingstatus_unfurnished', None)
    furnishingstatus_furnished = features.get('furnishingstatus_furnished', None)

    # Verificar si los parámetros esenciales están presentes
    if area is None or bedrooms is None or bathrooms is None:
        return jsonify({'error': 'Missing essential features (area, bedrooms, bathrooms)'}), 400
    
    # Si alguno de los parámetros opcionales no está presente, le asignamos un valor por defecto
    prediction = None
    try:
        prediction = predict_price([
            area, bedrooms, bathrooms, stories if stories is not None else 0,
            mainroad if mainroad is not None else 0,
            guestroom if guestroom is not None else 0,
            basement if basement is not None else 0,
            hotwaterheating if hotwaterheating is not None else 0,
            airconditioning if airconditioning is not None else 0,
            parking if parking is not None else 0,
            prefarea if prefarea is not None else 0,
            furnishingstatus_semi_furnished if furnishingstatus_semi_furnished is not None else 0,
            furnishingstatus_unfurnished if furnishingstatus_unfurnished is not None else 0,
            furnishingstatus_furnished if furnishingstatus_furnished is not None else 0
        ])
    except Exception as e:
        return jsonify({'error': f'Prediction failed: {str(e)}'}), 500
    
    # Retornar la predicción en formato JSON
    return jsonify({'predicted_price': prediction})
