Instrucciones:
Crea un archivo .sh, por ejemplo, crear_estructura.sh.

Copia y pega el código anterior en el archivo.

Da permisos de ejecución con el siguiente comando:

bash
Copiar
Editar
chmod +x crear_estructura.sh
Ejecuta el script con:

bash
Copiar
Editar
./crear_estructura.sh


 Configuración de Docker
Ya que tenemos todos los archivos preparados, vamos a crear y ejecutar la aplicación dentro de Docker.

Construir la imagen Docker
Ejecuta el siguiente comando en la raíz de tu proyecto para construir la imagen de Docker.

bash
Copiar
Editar
docker build -t flask-api .
Ejecutar el contenedor Docker
Para ejecutar la API dentro de un contenedor Docker, utiliza:

bash
Copiar
Editar
docker run -p 5000:5000 flask-api
9. Probar la API
Una vez que el contenedor está en ejecución, puedes hacer solicitudes POST a http://localhost:5000/predict con un JSON que contenga las características de entrada.

Ejemplo de JSON para la solicitud:

json
Copiar
Editar
{
  "features": [7420, 4, 2, 3, 1, 0, 0, 0, 1, 0, 2, 1]
}


. Reconstruir la imagen Docker
Después de realizar estos cambios, asegúrate de reconstruir la imagen Docker para que los archivos se copien correctamente en el contenedor:

bash
Copiar
Editar
docker build -t flask-api .
5. Verificar la estructura dentro del contenedor
Para asegurarte de que los archivos se copiaron correctamente al contenedor, puedes acceder al contenedor después de ejecutarlo:

bash
Copiar
Editar
docker run -d -p 5000:5000 --name flask-container flask-api


http://localhost:5000/api/predict


 Reconstruir la imagen Docker
Después de realizar estos cambios, asegúrate de reconstruir la imagen Docker para que los archivos se copien correctamente en el contenedor:

bash
Copiar
Editar
docker build -t flask-api .
5. Verificar la estructura dentro del contenedor
Para asegurarte de que los archivos se copiaron correctamente al contenedor, puedes acceder al contenedor después de ejecutarlo:

bash
Copiar
Editar
docker run -d -p 5000:5000 --name flask-container flask-api