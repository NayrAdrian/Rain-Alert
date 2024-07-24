import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "123456789"  # Sample API Key from Sample Account
account_sid = "123456789"  # Sample(Dummy)
auth_token = "123456789"  # Sample(Dummy)

MY_LAT = 14.612034  # Sample Coordinates
MY_LONG = 121.086786  # Sample Coordinates

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "cnt": 4,
    "appid": api_key,
    "units": "metric"  # To get the temperature in Celsius
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
temperature = weather_data["list"][0]["main"]["temp"]
weather_description = weather_data["list"][0]["weather"][0]["description"]

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        break

message_body = f"Current temperature: {temperature}°C.\nWeather: {weather_description.capitalize()}.\n"
if will_rain:
    message_body += "It is going to rain today, Remember to bring an ☂️."

    try:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_='whatsapp:+123456789',  # Enter From Number here
            body=message_body,
            to='whatsapp:+63123456789' # Enter To Number here
        )
        print(f"Message status: {message.status}")
    except Exception as e:
        print(f"Error sending SMS: {e}")
else:
    print("No rain expected.")
