import requests

# Esta url contiene la dirección del web service 
# y los parámetros que se requiren para la consulta
url = 'https://api.github.com/repos/IIC2233/Syllabus/contents/Actividades'
respuesta = requests.get(url)


print(f'Status: {respuesta.status_code}')
print(f"body: {respuesta.headers}")

# El output de esta respuesta particular
# puede ser transformado con .json() a un diccionario o una lista
# en este caso, fue a una lista
data = respuesta.json()
for file in data:
    print(file["name"], file["html_url"])