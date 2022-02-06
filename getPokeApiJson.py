from unittest import result
import requests

def getPokeApiJSON(path):
  url = f'https://pokeapi.co/api/v2/{path}/'
  args = {'offset' : 0, 'limit' : 1118 }
  response = requests.get(url, params=args)
  if response.status_code != 200:
    return {}
  payload = response.json()
  results = payload.get("results")
  if not results: return payload        
  return results