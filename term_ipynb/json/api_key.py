import requests

API_KEY='***************************'
url1 = 'https://api.openweathermap.org/data/2.5/weather?id=935695&lang=fr&units=metric&appid=' + API_KEY
url2 = 'https://api.openweathermap.org/data/2.5/forecast?id=935223&lang=fr&units=metric&appid=' + API_KEY
req = requests.get(url1)
data = req.json()
print(data)
