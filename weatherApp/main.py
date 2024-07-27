import customtkinter as ctk
from weather_api import fetch_weather
from weather_display import display_weather

def get_weather():
    city = entry.get()
    weather_data = fetch_weather(city)
    result_label.configure(text=display_weather(weather_data))

# Setting up the GUI
app = ctk.CTk()
app.title("Weather App")
app.geometry("400x300")

# Creating the input field for city name
entry_label = ctk.CTkLabel(app, text="Enter city name (e.g., London, Tokyo):")
entry_label.pack(pady=10)

entry = ctk.CTkEntry(app, width=250, justify='center')  # Center-align the text
entry.pack(pady=10)

# Creating the button to fetch weather
fetch_button = ctk.CTkButton(app, text="Get Weather", command=get_weather)
fetch_button.pack(pady=10)

# Label to display the weather information
result_label = ctk.CTkLabel(app, text="")
result_label.pack(pady=20)

# Run the GUI loop
app.mainloop()
