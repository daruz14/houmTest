from getPokeApiJson import getPokeApiJSON

if __name__ == "__main__":
  allPokemons = getPokeApiJSON('pokemon')
  if not allPokemons:
    print('Error getting pokemons')
    exit()

  pokemonByNames = [pokemon.get('name') for pokemon in allPokemons if ("at" in pokemon.get('name') and pokemon.get('name').count('a'))]
  print(len(pokemonByNames))