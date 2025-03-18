#!/bin/bash

# Crear la carpeta 'app' y los archivos dentro de ella
mkdir app
touch app/__init__.py
touch app/routes.py
touch app/model.py
touch app/utils.py

# Crear los archivos principales del proyecto
touch Dockerfile
touch requirements.txt
touch run.py
touch config.py

# Mensaje de confirmación
echo "Estructura del proyecto Flask creada con éxito."
