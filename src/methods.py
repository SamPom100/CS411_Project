import requests
import json
import api_keys

key = api_keys.getGoogleKey()
weather_key = api_keys.getWeatherKey()

def call_weather_api():
  api_url = 'https://api.openweathermap.org/data/2.5/weather?q=BOSTON&APPID='+weather_key+'&units=imperial'
  return requests.get(api_url).json()

def call_map_api(location: str):
    URL = "https://maps.googleapis.com/maps/api/place/textsearch/json?query="+("fun things to do in "+ location)+"&key="+key
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
    URL = "https://maps.googleapis.com/maps/api/place/textsearch/json?query="+("hotels in "+ location)+"&key="+key
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
