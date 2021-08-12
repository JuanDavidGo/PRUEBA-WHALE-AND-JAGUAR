# PRUEBA BACK END DEVELOPER - Whale & Jaguar

La API REST fue desarrollada utilizando el mini framework Flask, cuenta con una sencilla interfaz para consumir el servicio de verificación de tarjetas de creditos
### Para ejecutar el servidor debemos ingresar en el directorio principal e instalar los requerimientos necesarios, asi:
```
pip install requiremets.txt
```
### Para correr el servidor debemos ejecutar el siguiente comando
```
python app.py
```
# SERVICIO PORTABLE
### Para usar el servicio desde cualquier sistema operativo se dockerizó la aplicación, para bajar y correr la imagen de docker se deben ejecutar los siguientes comandos
```
docker pull juandavidgo/prueba:latest
docker run -d -p 5000:5000 juandavidgo/prueba:latest
```
El servicio podrá ser utilizado utilizando el siguiente link: http://localhost:5000/
