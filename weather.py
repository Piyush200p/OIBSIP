import requests
def weather_data(city_name):
 API_key = "bac3ee43d78265147d28ad0c53805c4e"
 geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={API_key}"
 geo_response = requests.get(geo_url)
 if geo_response.status_code == 200:
    geo_data= geo_response.json()
    if not geo_data:
       print("city not found")
       return
    lat = geo_data[0]['lat']
    lon = geo_data[0]['lon']
 else:
    print("Failed to fetch geo data:", geo_response.status_code)
    return
 weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric"
 response=requests.get(weather_url)
 if response.status_code == 200:
    print("Request successful!")
    output = response.json()
    menu= output['main']
    temperature = menu['temp']
    humidity = menu['humidity']
    weather= output['weather'][0]
    discription = weather['description']
    print("Weather data for:", city_name)
    print("Temperature:", temperature)
    print("Humidity:", humidity)
    print("Weather:", weather) 
    print("Description:", discription)  
 elif response.status_code == 404:
    print("City not found. Please check the city name and try again.") 
 else:
    print("Failed to fetch data:", response.status_code)
city_name = input("Enter the city name: ")
weather_data(city_name)