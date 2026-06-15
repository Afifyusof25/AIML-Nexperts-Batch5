import tkinter as tk
import requests

API_KEY = "f535321cb3ad6af0b8209364b28caa82"

def get_weather():
    city = textfield.get()

    api_url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    try:
        weather_data = requests.get(api_url).json()

        if weather_data["cod"] != 200:
            raise Exception("City not found")

        condition = weather_data["weather"][0]["main"]
        temperature = weather_data["main"]["temp"]
        min_temperature = weather_data["main"]["temp_min"]
        max_temperature = weather_data["main"]["temp_max"]
        pressure = weather_data["main"]["pressure"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]

        weather_summary = f"{condition}\n{temperature}°C"

        weather_details = (
            f"Maximum Temperature: {max_temperature}°C\n"
            f"Minimum Temperature: {min_temperature}°C\n"
            f"Pressure: {pressure} hPa\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_speed} m/s"
        )

        label1.config(text=weather_summary)
        label2.config(text=weather_details)

    except Exception:
        label1.config(text="Error")
        label2.config(text="City not found or API request failed")


# Main Window
window = tk.Tk()
window.geometry("600x500")
window.title("Weather Application")

heading_font = ("Poppins", 35, "bold")
details_font = ("Poppins", 15, "bold")

# City Input
textfield = tk.Entry(window, font=heading_font)
textfield.pack(pady=20)
textfield.focus()

# Search Button
search_button = tk.Button(
    window,
    text="Get Weather",
    font=details_font,
    command=get_weather
)
search_button.pack(pady=10)

# Output Labels
label1 = tk.Label(window, font=heading_font)
label1.pack()

label2 = tk.Label(window, font=details_font)
label2.pack()

window.mainloop()
