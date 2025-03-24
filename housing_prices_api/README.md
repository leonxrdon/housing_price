Instrucciones:
Crea un archivo .sh, por ejemplo, crear_estructura.sh.

Copia y pega el código anterior en el archivo.

Da permisos de ejecución con el siguiente comando:

```bash
chmod +x crear_estructura.sh
```
Ejecuta el script con:

```bash
./crear_estructura.sh
```

Configuración de Docker
Ya que tenemos todos los archivos preparados, vamos a crear y ejecutar la aplicación dentro de Docker.

Construir la imagen Docker
Ejecuta el siguiente comando en la raíz de tu proyecto para construir la imagen de Docker.

```bash
docker build -t flask-api .
```
Ejecutar el contenedor Docker
Para ejecutar la API dentro de un contenedor Docker, utiliza:
```bash
docker run -d -p 5000:5000 --name flask-container flask-api
```
Probar la API
Una vez que el contenedor está en ejecución, puedes hacer solicitudes POST a http://localhost:5000/predict con un JSON que contenga las características de entrada.

Ejemplo de JSON para la solicitud:

```json
{
  "features": [7420, 4, 2, 3, 1, 0, 0, 0, 1, 0, 2, 1]
}
```
