# utils.py
import http.client
import json

def get_pokemon_data(pokemon_name):
    # Establecemos la conexión con el servidor
    conn = http.client.HTTPSConnection("pokeapi.co")

    # Realizamos la solicitud GET para obtener datos de un Pokémon
    conn.request("GET", f"/api/v2/pokemon/{pokemon_name}")

    # Obtenemos la respuesta
    response = conn.getresponse()
    response_data=response.read()
    print(type(response_data))
    # Verificamos si la solicitud fue exitosa
    if response.status == 200:
        # Leemos los datos y los decodificamos de JSON a un diccionario de Python
        data = json.loads(response_data.read().decode('UTF-8'))
        print(type(data))
        conn.close()  # Cerramos la conexión
        return data
    else:
        conn.close()  # Cerramos la conexión
        return None  # Devuelve None si ocurre un error
