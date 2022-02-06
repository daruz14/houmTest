from multiprocessing import Pool
from getPokeApiJson import getPokeApiJSON

def idFromUrl(pokemon):
  pokemonData = pokemon.get('pokemon')
  url = pokemonData.get('url')
  id = url.split('/')[-2]
  return int(id)

def fightingPokemonsNames(fightingPokemons):
  result = []
  for pokemon in fightingPokemons.get('pokemon', []):
    pokemonId = idFromUrl(pokemon)
    if pokemonId <= 151:
      result.append(pokemon.get('pokemon').get('name'))
  return result

def pokemonWeigth(pokemonName):
  pokemon = getPokeApiJSON(f'pokemon/{pokemonName}')
  return pokemon.get('weight')

def pokemonsWeigths(pokemonWeigth, pokemons):
  with Pool(4) as p:
    result = p.map(pokemonWeigth, pokemons)
    p.close()
    p.join()
  return result

if __name__ == "__main__":
  fightingPokemons = getPokeApiJSON('type/fighting/')
  if not fightingPokemons:
    print('Error getting figthing pokemons')
    exit()
  
  pokemons = fightingPokemonsNames(fightingPokemons)
  weigths = pokemonsWeigths(pokemonWeigth, pokemons)
  print([max(weigths), min(weigths)])