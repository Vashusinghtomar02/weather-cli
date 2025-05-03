import requests
api_key = "74fdbd924e1e3291958ce6186b273074"
city = input("Enter city name: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
response = requests.get(url).json()
print(f"Temperature: {round(response['main']['temp']-273.15)}°C")