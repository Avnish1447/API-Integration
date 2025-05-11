import customtkinter as ctk
import requests
import datetime as dt
from tkinter import messagebox

def ReadAPI_Key(path):
    try:
        with open(path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        messagebox.showerror("Error", "API key file not found.")
        return None
    except requests.exceptions.RequestException as err:
        messagebox.showerror("Error", f"Request error: {err}")
        return None

def GetWeatherData(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    url = f"{base_url}appid={api_key}&q={city}&units=metric"
    try:
        response = requests.get(url).json()
        if response.get("cod") != 200:
            messagebox.showerror("API Error", response.get("message", "Unknown error"))
            return None
        return response
    except requests.RequestException as e:
        messagebox.showerror("Connection Error", f"Error fetching data: {e}")
        return None

def display_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Input Error", "City name cannot be empty.")
        return

    api_key = ReadAPI_Key("api_key")
    if not api_key:
        return

    data = GetWeatherData(city, api_key)
    if data:
        temp_celsius = data['main']['temp']
        temp_fahrenheit = round((temp_celsius * 9 / 5) + 32, 2)

        feels_like_celsius = data['main']['feels_like']
        feels_like_fahrenheit = round((feels_like_celsius * 9 / 5) + 32, 2)

        humidity = data['main']['humidity']
        description = data['weather'][0]['description'].capitalize()

        sunrise_timestamp = data['sys']['sunrise']
        sunset_timestamp = data['sys']['sunset']
        timezone_offset = data['timezone']
        sunrise_time = dt.datetime.utcfromtimestamp(sunrise_timestamp + timezone_offset)
        sunset_time = dt.datetime.utcfromtimestamp(sunset_timestamp + timezone_offset)

        wind_speed = data['wind']['speed']

        output = (
            f"🌍\tCity   \t\t :\t{city.capitalize()}\n"
            f"🌡️\tTemperature\t :\t{temp_celsius:>5}°C / {temp_fahrenheit:>6}°F\n"
            f"🥵\tFeels Like \t :\t{feels_like_celsius:>5}°C / {feels_like_fahrenheit:>6}°F\n"
            f"💧\tHumidity   \t :\t{humidity}%\n"
            f"☁️\tWeather    \t :\t{description}\n"
            f"🌅\tSunrise    \t :\t{sunrise_time.strftime('%H:%M:%S')}\n"
            f"🌇\tSunset     \t :\t{sunset_time.strftime('%H:%M:%S')}\n"
            f"💨\tWind Speed \t :\t{wind_speed} m/s"
        )

        result_label.configure(text=output)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
app = ctk.CTk()
app.geometry("500x550")
app.title("🌤️ Weather App")

title_label = ctk.CTkLabel(app, text="Weather Forecast", font=("Segoe UI", 24, "bold"))
title_label.pack(pady=20)

city_entry = ctk.CTkEntry(app, placeholder_text="Enter city name", width=300, font=("Segoe UI", 14))
city_entry.pack(pady=10)

get_weather_btn = ctk.CTkButton(app, text="Get Weather", command=display_weather, width=160)
get_weather_btn.pack(pady=15)

result_label = ctk.CTkLabel(app, text="", font=("Segoe UI", 14), justify="left", wraplength=450)
result_label.pack(pady=20)

app.mainloop()
