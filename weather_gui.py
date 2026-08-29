import tkinter as tk
import requests
import os

from dotenv import load_dotenv

load_dotenv()

api_key =os.getenv("OPENWEATHER_API_KEY")

url = "https://api.openweathermap.org/data/2.5/weather"


def get_weather():

    city = city_entry.get().strip()
    

    if city == "":
        result_label.config(text="Please enter a city name.")
        return

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:

        data = response.json()

        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        city_name = data["name"]
        condition = data["weather"][0]["description"]

        result_label.config(
            text=f"{city_name}\n\n"
                 f"{temperature:.1f}°C\n"
                 f"{condition.title()}\n\n"
                 f"Humidity: {humidity}%\n"
                 f"Wind: {wind_speed} m/s"
        )

    else:

        result_label.config(
            text="City not found.\nPlease try again."
        )


window = tk.Tk()

window.title("Weather Dashboard")
window.geometry("400x500")
window.configure(bg="#F4C8ED")


title = tk.Label(
    window,
    text="WEATHER DASHBOARD",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="#572354"
)

title.pack(pady=20)


city_entry = tk.Entry(
    window,
    font=("Arial", 14),
    width=25,
    justify="center"
)

city_entry.pack(pady=10)


button = tk.Button(
    window,
    text="GET WEATHER",
    command=get_weather,
    font=("Arial", 12, "bold"),
    bg="#51004C",
    fg="white",
    padx=20,
    pady=8
)

button.pack(pady=15)


weather_frame = tk.Frame(
    window,
    bg="white",
    padx=30,
    pady=20
)

weather_frame.pack(pady=20)


result_label = tk.Label(
    weather_frame,
    text="Enter a city to get weather",
    font=("Arial", 13),
    bg="white",
    fg="#610051"
)

result_label.pack()


window.mainloop()