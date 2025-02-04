import http.client
import json

# Establecemos la conexión con el servidor
conn = http.client.HTTPSConnection("pokeapi.co")

# Realizamos la solicitud GET para obtener datos de Pikachu
conn.request("GET", "/api/v2/pokemon/pikachu")

# Obtenemos la respuesta
response = conn.getresponse()

# Verificamos si la solicitud fue exitosa
if response.status == 200:
    # Leemos los datos y los decodificamos de JSON a un diccionario de Python
    data = json.loads(response.read().decode())
    
    # Mostrar el nombre del Pokémon
    print(f"Nombre del Pokémon: {data['name']}")
    
    # Mostrar los tipos del Pokémon
    types = [type_info['type']['name'] for type_info in data['types']]
    print(f"Tipos: {', '.join(types)}")
    
else:
    print("Error al obtener los datos")

# Cerramos la conexión
conn.close()
