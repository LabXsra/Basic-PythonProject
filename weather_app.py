import requests

api_key='785104f0e4d41976d584f28889a163bf'
user_input=input("Enter city:")
weather_data=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

print(weather_data.status_code)
print(weather_data.json())
weather=weather_data.json()['weather'][0]['main']
temp=round(weather_data.json()['main']['temp'])
print(weather,temp)
print(f"the weather in {user_input} is: {weather}")
print(f"the temperature in {user_input}s :{temp}F")
