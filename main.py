import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "9d8bc79a5475666165e79e492993d334"  # Sample API Key from Sample Account

MY_LAT = 14.612034  # Sample Coordinates
MY_LONG = 121.086786  # Sample Coordinates

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "cnt": 4,
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    print("Bring an umbrella.")