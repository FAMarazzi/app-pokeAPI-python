import http.client
import json

class APIClient:
    def __init__(self):
        self.conn = http.client.HTTPSConnection("pokeapi.co")

    def get_pokemon_data(self, pokemon_name: str):
        try:
            self.conn.request("GET", f"/api/v2/pokemon/{pokemon_name}") 
            response = self.conn.getresponse()
            data = response.read()
            return json.loads(data.decode())
            
        except Exception as e:
            if type(e).__name__=="JSONDecodeError":
                print(f"El pokemon {pokemon_name} no existe")
            else:
                print(f"Error: {type(e).__name__} - {str(e)}")
            return None

# Código de prueba directo
'''
if __name__ == "__main__":
    print("Iniciando prueba")
    client = APIClient()
    result = client.get_pokemon_data("pikachu")
    print("Resultado:", result is not None)
'''