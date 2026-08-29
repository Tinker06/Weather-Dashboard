
import requests
import os

from dotenv import load_dotenv

load_dotenv()

print("===============================")
print("         Weather App")
print("===============================")
print()
print()
print("Welcome to the Weather App!")
print()
api_key = os.getenv("OPENWEATHER_API_KEY")
url="https://api.openweathermap.org/data/2.5/weather"
def info(city):
    params ={
            "q":city,
            "appid":api_key,
            "units":"metric"
        }
    response = requests.get(url, params=params)
    if response.status_code == 200:
            data=response.json()
            temperature = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            city_name = data["name"]
            condition = data["weather"][0]["description"]

            return city_name, temperature, feels_like, humidity, wind_speed, condition

            
    else:
        return None
        
while True:
    city= input("Enter city name(or 'quit' to exit): ")
    if city.lower() == "quit":
        print("Thank you for using the Weather App!")
        break
    weather=info(city)
    if weather:
        city_name, temperature, feels_like, humidity, wind_speed, condition = weather
        print()
        print("-------------------------------------------------------")
        print("City:        ", city_name)
        print("Temperature: ", temperature)
        print("Feels like:  ", feels_like)
        print("Humidity:    ", humidity)
        print("Condition:   ", condition)
        print("Wind Speed:  ", wind_speed)
        print("-------------------------------------------------------")
    else:
        print("City not found. Please check the city name and try again.")

    
    
    

    