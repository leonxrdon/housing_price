from flask import Flask
from .routes import routes  # Importa el Blueprint
from .model import predict_price

def create_app():
    app = Flask(__name__)
    
    # Registrar Blueprint de rutas
    app.register_blueprint(routes, url_prefix='/api')  # Aquí defines el prefijo

    return app