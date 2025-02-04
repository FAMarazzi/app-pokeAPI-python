from debug_requests import APIClient
def get_pokemon_abilities(nombrePokemon):
    try:
        data=APIClient().get_pokemon_data(nombrePokemon)
        print("Abilities: ")
        for ability in data["abilities"]:
            pokemon_abilities=ability['ability']['name'].title()
            print(f"{pokemon_abilities}")
    except Exception as e:
        print(f"Error: {type(e).__name__} - {str(e)}")
        return

def get_pokemon_stats(nombrePokemon):
    try:
        data=APIClient().get_pokemon_data(nombrePokemon)
        print("Stats: ")
        for stat in data["stats"]:
            pokemon_stats=stat['stat']['name'].title()
            print(f"{pokemon_stats}: {stat['base_stat']}")
    except Exception as e:
        print(f"Error: {type(e).__name__} - {str(e)}")
        return

def getPokemonType(nombrePokemon):
    """
    Dado el nombre de un pokemon, imprime su tipo.

    Parameters
    ----------
    nombrePokemon : str
        El nombre del pokemon a consultar su tipo.

    Returns
    -------
    None
    """
    try:
        data= APIClient().get_pokemon_data(nombrePokemon)
        tipo_pokemon=data['types'][0]['type']['name'].title()
        print(f"Tipo: {tipo_pokemon}")
    except Exception as e:
        print(f"Error: {type(e).__name__} - {str(e)}")
        return
    
userAnswer='s'  
while userAnswer=='s':
    nombrePokemon = input('Ingrese el nombre del pokemon para consultar su tipo: ')
    print(f"Pokemon: {nombrePokemon.title()}")
    getPokemonType(nombrePokemon)
    get_pokemon_abilities(nombrePokemon)
    get_pokemon_stats(nombrePokemon)
    userAnswer=input('¿Desea consultar algún otro pokemon? (s/n): ')
    if(userAnswer=='n' or userAnswer=='s'):
        pass
    else:
        userAnswer=input('¿Desea consultar Librería Pokémon? (s/n): ')
        if(userAnswer=='s'):
            userAnswer=input('Ingrese cuantos pokemons desea consultar: ')
            data=APIClient().get_pokemon_data(f"?offset={userAnswer}&limit={userAnswer}")
            for pokemon in data['results']:
                print(f"Pokemon: {pokemon['name'].title()}")
            userAnswer='s'