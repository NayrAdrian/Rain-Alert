import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "9d8bc79a5475666165e79e492993d334"  # Sample API Key from Sample Account

MY_LAT = 14.612034  # Sample Coordinates
MY_LONG = 121.086786  # Sample Coordinates

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

forecasts = weather_data["list"]
for forecast in forecasts:
    weather = forecast["weather"][0]
    weather_id = weather["id"]
    description = weather["description"]
    print(f"Weather ID: {weather_id}, Description: {description}")