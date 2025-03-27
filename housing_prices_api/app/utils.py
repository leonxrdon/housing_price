import joblib

def scaler_values(values):
    """
    Función para escalar los valores de características.
    
    :param values: Valores de características a escalar.
    :return: Valores de características escalados.
    """
    # Cargar el scaler
    scaler = joblib.load('scaler/robust_scaler_X.joblib')
    # Convertir el diccionario a una lista
    values_list = [values[key] for key in values.keys()]

    # Escalar los valores
    return scaler.transform([values_list])


def scaler_predict(predict):
    """
    Función para escalar la predicción de precios.
    
    :param predict: Predicción de precios a escalar.
    :return: Predicción de precios escalada.
    """
    # Cargar el scaler
    scaler = joblib.load('scaler/robust_scaler_y.joblib')
    predict_scaler = scaler.inverse_transform(predict)
    # Escalar la predicción
    return float(predict_scaler[0][0])

def calculate_features(features):
    """
    Función para calcular características faltantes basadas en las características proporcionadas.
    
    :param features: Diccionario con las características proporcionadas en el JSON.
    :return: Diccionario con las características completas, incluyendo las calculadas.
    """
    
    # Asignar valores predeterminados si no están presentes
    area = int(features.get('area', 0))  # Si 'area' no está presente, usa 0 por defecto
    bedrooms = int(features.get('bedrooms', 0))  # Igual para otras características
    bathrooms = int(features.get('bathrooms', 0))
    stories = int(features.get('stories', 0))
    parking = int(features.get('parking', 0))
    mainroad = int(features.get('mainroad', 0)) 
    guestroom = int(features.get('guestroom', 0)) 
    basement = int(features.get('basement', 0)) 
    hotwaterheating = int(features.get('hotwaterheating', 0))
    airconditioning = int(features.get('airconditioning', 0))
    prefarea = int(features.get('prefarea', 0)) 
    furnishingstatus = features.get('furnishingstatus', '')

    if furnishingstatus == 'semi-furnished':
        furnishingstatus_unfurnished = 0
        furnishingstatus_semi_furnished = 1
        furnishingstatus_furnished = 0 
    elif furnishingstatus == 'furnished':
        furnishingstatus_furnished = 1
        furnishingstatus_semi_furnished = 0
        furnishingstatus_unfurnished = 0
    else:
        furnishingstatus_furnished = 0
        furnishingstatus_semi_furnished = 0
        furnishingstatus_unfurnished = 1

    # Cálculos de características faltantes o derivados
    area_per_room = area / bedrooms if area and bedrooms else 0
    bath_per_bed = bathrooms / bedrooms if bathrooms and bedrooms else 0
    area_per_story = area / stories if area and stories else 0
    area_per_parking = area / parking if area and parking else 0
    
    # Amenities totales (por ejemplo, suma de características booleanas)
    total_amenities = sum([
        mainroad, guestroom,
        basement, hotwaterheating,
        airconditioning, prefarea,
        ])
    
    # Retornar las características completas y transformadas
    values = {
        'area': area,
        'bedrooms': bedrooms,
        'bathrooms': bathrooms,
        'stories': stories,
        'mainroad': mainroad,
        'guestroom': guestroom,
        'basement': basement,
        'hotwaterheating': hotwaterheating,
        'airconditioning': airconditioning,
        'parking': parking,
        'prefarea': prefarea,
        'furnishingstatus_semi-furnished': furnishingstatus_semi_furnished,
        'furnishingstatus_unfurnished': furnishingstatus_unfurnished,
        'furnishingstatus_furnished': furnishingstatus_furnished,
        'area_per_room': area_per_room,
        'bath_per_bed': bath_per_bed,
        'area_per_story': area_per_story,
        'area_per_parking': area_per_parking,
        'total_amenities': total_amenities  
    }
    return values