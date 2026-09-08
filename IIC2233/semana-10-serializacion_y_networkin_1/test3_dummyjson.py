import requests


BASE = "https://dummyjson.com/"
endpoint_1 = "recipes/"

respuesta = requests.get(BASE + endpoint_1)

# imprimir el status_code
print(respuesta.status_code)


data = respuesta.json()
print("Llaves: ", data.keys())


print(data['recipes'][0])



# =========================================================

endpoint_2 = "products/"

respuesta = requests.get(BASE + endpoint_2)

data = respuesta.json()
[product['title'] for product in data['products'][:2]]