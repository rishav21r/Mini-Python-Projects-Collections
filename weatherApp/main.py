import customtkinter as ctk
from weather_api import fetch_weather
from weather_display import display_weather

def get_weather(event=None):
    city = entry.get()
    result_label.configure(text="Fetching weather data...")
    weather_data = fetch_weather(city)
    if weather_data:
        result_label.configure(text=display_weather(weather_data))
        entry.delete(0, 'end')
    else:
        result_label.configure(text="Error: City not found. Please try again.")

# Setting up the GUI
app = ctk.CTk()
app.title("Weather App")
app.geometry("400x350")

# Creating the input field for city name
entry_label = ctk.CTkLabel(app, text="Enter city name (e.g., London, Tokyo):", font=("Helvetica", 14))
entry_label.pack(pady=10)

entry = ctk.CTkEntry(app, width=300, justify='center', font=("Helvetica", 14))
entry.pack(pady=10)
entry.bind('<Return>', get_weather)  # Bind the Enter key to fetch weather

# Creating the button to fetch weather
fetch_button = ctk.CTkButton(app, text="Get Weather", command=get_weather, font=("Helvetica", 14))
fetch_button.pack(pady=10)

# Label to display the weather information
result_label = ctk.CTkLabel(app, text="", font=("Helvetica", 14), justify='left')
result_label.pack(pady=20)

# Run the GUI loop
app.mainloop()
