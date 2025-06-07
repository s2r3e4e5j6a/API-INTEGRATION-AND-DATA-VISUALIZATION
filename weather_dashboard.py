import requests
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta

# --- Configuration ---
API_KEY = "5e2fadaacbed143919c30654b6c054a7" # <<--- IMPORTANT: Replace with your actual API key
CITY_NAME = "London" # You can change this to any city
# API_KEY = "00000000000000000000000000000000" # Dummy API key. Replace with your actual key.

# --- API Endpoints ---
CURRENT_WEATHER_URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}&units=metric"
ONE_CALL_API_URL = f"https://api.openweathermap.org/data/2.5/onecall?lat={{lat}}&lon={{lon}}&exclude=minutely,hourly,alerts&appid={API_KEY}&units=metric"

def fetch_current_weather(city):
    """Fetches current weather data for a given city."""
    print(f"Fetching current weather for {city}...")
    try:
        response = requests.get(CURRENT_WEATHER_URL.replace(CITY_NAME, city))
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        print("Current weather data fetched successfully.")
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching current weather: {e}")
        return None

def fetch_forecast_data(lat, lon):
    """Fetches daily forecast data using the One Call API."""
    print(f"Fetching 7-day forecast for lat={lat}, lon={lon}...")
    try:
        url = ONE_CALL_API_URL.format(lat=lat, lon=lon)
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print("Forecast data fetched successfully.")
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching forecast data: {e}")
        return None

def visualize_current_weather(data):
    """Creates a visualization for current weather."""
    if not data:
        print("No current weather data to visualize.")
        return

    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description'].capitalize()
    wind_speed = data['wind']['speed']

    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Create a bar chart for temperature and feels like
    categories = ['Temperature (°C)', 'Feels Like (°C)']
    values = [temp, feels_like]
    ax.bar(categories, values, color=['skyblue', 'lightcoral'])
    ax.set_ylabel('Temperature (°C)')
    ax.set_title(f"Current Weather in {data['name']}")
    
    # Add text annotations for other details
    ax.text(0.5, 0.95, f"Description: {description}", transform=ax.transAxes, fontsize=12, ha='center')
    ax.text(0.5, 0.90, f"Humidity: {humidity}%", transform=ax.transAxes, fontsize=12, ha='center')
    ax.text(0.5, 0.85, f"Wind Speed: {wind_speed} m/s", transform=ax.transAxes, fontsize=12, ha='center')
    
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def visualize_daily_forecast(data):
    """Creates visualizations for daily forecast data."""
    if not data or 'daily' not in data:
        print("No forecast data to visualize.")
        return

    dates = []
    max_temps = []
    min_temps = []
    humidities = []
    wind_speeds = []
    descriptions = []

    for day in data['daily']:
        dt_object = datetime.fromtimestamp(day['dt'])
        dates.append(dt_object.strftime('%a, %b %d'))
        max_temps.append(day['temp']['max'])
        min_temps.append(day['temp']['min'])
        humidities.append(day['humidity'])
        wind_speeds.append(day['wind_speed'])
        descriptions.append(day['weather'][0]['description'].capitalize())

    df = pd.DataFrame({
        'Date': dates,
        'Max Temp (°C)': max_temps,
        'Min Temp (°C)': min_temps,
        'Humidity (%)': humidities,
        'Wind Speed (m/s)': wind_speeds,
        'Description': descriptions
    })

    # Plot 1: Max and Min Temperatures
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Max Temp (°C)'], marker='o', label='Max Temp (°C)', color='red')
    plt.plot(df['Date'], df['Min Temp (°C)'], marker='o', label='Min Temp (°C)', color='blue')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title(f'7-Day Temperature Forecast for {CITY_NAME}')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    # Plot 2: Humidity
    plt.figure(figsize=(12, 6))
    plt.bar(df['Date'], df['Humidity (%)'], color='lightgreen')
    plt.xlabel('Date')
    plt.ylabel('Humidity (%)')
    plt.title(f'7-Day Humidity Forecast for {CITY_NAME}')
    plt.grid(axis='y')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
    
    # Plot 3: Wind Speed
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Wind Speed (m/s)'], marker='x', linestyle='--', color='purple')
    plt.xlabel('Date')
    plt.ylabel('Wind Speed (m/s)')
    plt.title(f'7-Day Wind Speed Forecast for {CITY_NAME}')
    plt.grid(True)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    if API_KEY == "YOUR_OPENWEATHERMAP_API_KEY":
        print("WARNING: Please replace 'YOUR_OPENWEATHERMAP_API_KEY' with your actual OpenWeatherMap API key.")
        print("You can get a free API key from https://openweathermap.org/api")
    else:
        # Fetch current weather to get lat/lon for forecast
        current_weather_data = fetch_current_weather(CITY_NAME)

        if current_weather_data:
            # Visualize current weather
            visualize_current_weather(current_weather_data)

            lat = current_weather_data['coord']['lat']
            lon = current_weather_data['coord']['lon']
            
            # Fetch and visualize daily forecast
            forecast_data = fetch_forecast_data(lat, lon)
            visualize_daily_forecast(forecast_data)
        else:
            print(f"Could not fetch data for {CITY_NAME}. Please check your API key and city name.")