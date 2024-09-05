import requests
from pprint import pprint

API_Key = 'fa0dad3aa61b84b37cb1bebb708909b0'
city = input("Enter City:")

# Correct the base_url with '=' between 'q' and city
base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_Key + "&q=" + city

weather_data = requests.get(base_url).json()

pprint(weather_data)
