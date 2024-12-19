import requests # libreria para consumir datos en internet
import json

# esta funcion nos ayudara a crear usuarios y guardarlos en un BD

# esta es la url a la cual vamos a estan madando la informacion
url = 'https://3337-189-193-83-212.ngrok-free.app/'

def registrar_usuario(nombre, apellido, telefono, correo, password):

    informacion_a_enviar = {
        'nombre': nombre + ' ' +apellido,
        'telefono': telefono,
        'correo': correo,
        'password': password
    }

    print(informacion_a_enviar)


    respuesta = requests.post(url+'/registro', data=informacion_a_enviar)

    respuesta_string = respuesta.contect.decode('utf-8')

    respuesta_diccionario = json.loads(respuesta_string)

    return respuesta_diccionario

def login_usuario(correo, password):

    # este diccionario enviara mandara toda la informacion a a db
    informacion_a_enviar = {
        'correo': correo,
        'password': password
    }

    print(informacion_a_enviar)

    respuesta = requests.post(url+'/login', data=informacion_a_enviar)

   # print(respuesta.content)


if __name__ == "__main__":

    registrar_usuario('Jose', 'Esteva', '2374832749327483', 'jose@correo.com', 'hola123')
