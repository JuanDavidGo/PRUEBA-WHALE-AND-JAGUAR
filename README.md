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
docker run --network="host" juandavidgo/prueba:latest
```
El servicio estará corriendo y solo es necesario abrir el link que proporciona la consola
![image](https://user-images.githubusercontent.com/24253618/129129059-d33aefb4-2ab3-4a2a-99ba-22a05fc11598.png)
