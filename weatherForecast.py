import requests

url='http://api.weatherapi.com/v1/current.json?key=f13ca0b3389c42bc83813337212404&q='
city=input("Enter any city:\n")
data=requests.get(url+city).json()

print(f"City: {city}\nCountry: {data['location']['country']}\nLatitude: {data['location']['lat']} degrees\nLongitude: {data['location']['lon']} degrees")
print(f"Time Zone: {data['location']['tz_id']}")
print(f"Local Time: {data['location']['localtime']}")
print("The temperature in degree celsius:",data['current']['temp_c'],"degrees")
print("The temperature in degree fahrenheit:",data['current']['temp_f'],"degrees")
print(f"Humidity: {data['current']['humidity']}")
print(f"Wind speed: {data['current']['wind_mph']} mph / {data['current']['wind_kph']} kph")
print("\nHAVE A NICE DAY !!")
