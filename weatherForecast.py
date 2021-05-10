import requests  

# Extracting weather info using weatherapi.com API
url='http://api.weatherapi.com/v1/current.json?key=(write_your_API_Key_here)' # Write your own API Key after "key=" 
city=input("Enter name of the city:\n")
data=requests.get(url+city).json()

print(f"City: {city}\nCountry: {data['location']['country']}\nLatitude: {data['location']['lat']} degrees\nLongitude: {data['location']['lon']} degrees")

print(f"Time Zone: {data['location']['tz_id']}")
      
print(f"Local Time: {data['location']['localtime']}")
      
print("The temperature in degree celsius:",data['current']['temp_c'],"degrees")
      
print("The temperature in degree fahrenheit:",data['current']['temp_f'],"degrees")
      
print(f"Humidity: {data['current']['humidity']}")
      
print(f"Wind speed: {data['current']['wind_mph']} mph / {data['current']['wind_kph']} kph")
      
print("\nHAVE A NICE DAY !!")
