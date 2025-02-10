import requests

def get_weather(city):
    API_KEY = "your_api_key_here"  # Replace with a valid API key
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Error fetching weather data:", e)
        return None

def weather_recommendation(weather_data):
    if not weather_data:
        return "Weather data unavailable."
    
    temp = weather_data['main']['temp']
    condition = weather_data['weather'][0]['main']
    
    recommendation = ""
    
    if temp > 25:
        recommendation += "It's hot outside! Wear light clothing. "
    elif 15 <= temp <= 25:
        recommendation += "The weather is pleasant. Enjoy your day! "
    else:
        recommendation += "It's cold! Wear warm clothes. "
    
    if condition.lower() in ['rain', 'drizzle', 'thunderstorm']:
        recommendation += "Don't forget an umbrella!"
    elif condition.lower() == 'snow':
        recommendation += "Wear boots and stay warm!"
    
    return recommendation

if __name__ == "__main__":
    city = input("Enter city name: ")
    weather_data = get_weather(city)
    print(weather_recommendation(weather_data))
