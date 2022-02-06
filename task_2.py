from getPokeApiJson import getPokeApiJSON
from multiprocessing import Pool

def getCountOfPokemonsFromEggGroup(eggGroup, raichuEggsGroupsOptions):
  totalCount = 0
  for pokemon in eggGroup.get('pokemon_species', []):
    pokemonName = pokemon.get('name')
    if (pokemonName != 'raichu' and not pokemonName in raichuEggsGroupsOptions):
      raichuEggsGroupsOptions[pokemonName] = 1
      totalCount += 1
  return totalCount

def totalRaichuPartners(raichuEggsGroups):
  raichuEggsGroupsOptions = {}
  totalCount = 0
  for eggGroupName in raichuEggsGroups:
    eggGroup = getPokeApiJSON(f'egg-group/{eggGroupName}')
    if not eggGroup:
      print(f'Error getting data of Egg Group {eggGroupName}')
    totalCount += getCountOfPokemonsFromEggGroup(eggGroup, raichuEggsGroupsOptions)
  print(totalCount)

if __name__ == "__main__":
  raichu = getPokeApiJSON('pokemon-species/raichu')
  if not raichu:
    print('Raichu data not exists in PokeApi')
    exit()

  raichuEggsGroups = [ eggGroup.get('name') for eggGroup in raichu.get('egg_groups', [])]
  totalRaichuPartners(raichuEggsGroups)
  
