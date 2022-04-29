import requests
import json
from api_keys import google_maps_key, weather_key

def call_weather_api(location: str):
  api_url = 'https://api.openweathermap.org/data/2.5/weather?q='+location+'&APPID='+weather_key+'&units=imperial'
  return requests.get(api_url)

def call_map_api(location: str):
    URL = "https://maps.googleapis.com/maps/api/place/textsearch/json?query="+("fun things to do in "+ location)+"&key="+google_maps_key
    response = json.loads(requests.get(URL).text)['results']
    returnList = []
    for entry in response:
        returnDict = {}
        returnDict['name'] = entry['name']
        returnDict['address'] = entry['formatted_address']
        returnDict['rating'] = entry['rating']
        returnDict['category'] = entry['types']
        returnList.append(returnDict)
    return json.dumps(returnList, indent = 4)

def call_travel_api(location: str):
    URL = "https://maps.googleapis.com/maps/api/place/textsearch/json?query="+("hotels in "+ location)+"&key="+google_maps_key
    response = json.loads(requests.get(URL).text)['results']
    returnList = []
    for entry in response:
        returnDict = {}
        returnDict['name'] = entry['name']
        returnDict['address'] = entry['formatted_address']
        returnDict['rating'] = entry['rating']
        returnDict['category'] = entry['types']
        returnList.append(returnDict)
    return json.dumps(returnList, indent = 4)