import os
import tkinter as tk
import requests

# Function to get weather information from OpenWeatherMap API
def get_weather(city):
    api_key = os.environ['API']
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    weather_data = response.json()
    show_weather(weather_data)

# Function to display weather information on the GUI
def show_weather(weather_data):
    weather = weather_data["weather"][0]["description"].capitalize()
    temperature = weather_data["main"]["temp"]
    feels_like = weather_data["main"]["feels_like"]
    humidity = weather_data["main"]["humidity"]
    wind_speed = weather_data["wind"]["speed"]

    weather_label.config(text="Weather: " + weather, fg="white", bg="#1E1E1E", padx=10, pady=5)
    temp_label.config(text="Temperature: " + str(temperature) + " °C", fg="white", bg="#1E1E1E", padx=10, pady=5)
    feels_like_label.config(text="Feels like: " + str(feels_like) + " °C", fg="white", bg="#1E1E1E", padx=10, pady=5)
    humidity_label.config(text="Humidity: " + str(humidity) + "%", fg="white", bg="#1E1E1E", padx=10, pady=5)
    wind_speed_label.config(text="Wind Speed: " + str(wind_speed) + " m/s", fg="white", bg="#1E1E1E", padx=10, pady=5)

# GUI setup
root = tk.Tk()
root.title("Weather App")
root.geometry("450x450")  # Set the window size to 450 by 450 pixels
root.configure(bg="#1E1E1E") # Set the background color to dark grey

city_label = tk.Label(root, text="Enter City Name:", fg="white", bg="#1E1E1E", padx=10, pady=5)
city_label.grid(row=0, column=0, sticky="W")

city_entry = tk.Entry(root)
city_entry.grid(row=0, column=1, padx=10, pady=5)

search_button = tk.Button(root, text="Search", command=lambda: get_weather(city_entry.get()), bg="#4C4C4C", fg="white", padx=10, pady=5)
search_button.grid(row=0, column=2, padx=10, pady=5)

weather_label = tk.Label(root)
weather_label.grid(row=1, column=0, sticky="W")

temp_label = tk.Label(root)
temp_label.grid(row=2, column=0, sticky="W")

feels_like_label = tk.Label(root)
feels_like_label.grid(row=3, column=0, sticky="W")

humidity_label = tk.Label(root)
humidity_label.grid(row=4, column=0, sticky="W")

wind_speed_label = tk.Label(root)
wind_speed_label.grid(row=5, column=0, sticky="W")

root.mainloop()