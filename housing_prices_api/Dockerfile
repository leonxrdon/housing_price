# Usar imagen base de Python
FROM python:3.9-slim

# Definir directorio de trabajo
WORKDIR /app

# Copiar los archivos necesarios al contenedor
COPY requirements.txt .
COPY models/ /models/ 
COPY app /app/

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación
COPY . .

# Exponer el puerto de la aplicación
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["gunicorn", "-b", "0.0.0.0:5000", "run:app"]
