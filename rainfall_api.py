# import required modules
import json
import requests

def get_rain():
    # Enter your API key here
    api_key = "6273246fe07a2c71789e7415c6d18d31"

    # Give latitude
    # lat = input("Enter Latitude : ")

    # # Give longitude
    # lon = input("Enter Longitude: ")

    # Give city name
    #city_name = input("Enter city name: ")

    # complete_url variable to store
    # complete url address
    url = "https://api.openweathermap.org/data/2.5/forecast?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)
    #url = "https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s&units=metric" % (city_name, api_key)

    # get method of requests module
    # return response object
    response = requests.get(url)

    # json method of response object
    data = response.json()

    # create a list to store the rainfall data
    rainfall_data = []
    for forecast in data['list']:
        if 'rain' in forecast:
            rainfall_data.append(forecast['rain']['3h'])

    # create a variable to store the mean of the rainfall data list
    mean = sum(rainfall_data) / len(rainfall_data)

    # print the mean
    #print(mean)

    return mean
