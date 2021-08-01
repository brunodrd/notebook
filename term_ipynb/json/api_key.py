import requests

API_KEY='46faf1f7a58f94ffc36fe94bf9e8ea95'
url1 = 'https://api.openweathermap.org/data/2.5/weather?id=935695&lang=fr&units=metric&appid=' + API_KEY
url2 = 'https://api.openweathermap.org/data/2.5/forecast?id=935223&lang=fr&units=metric&appid=' + API_KEY
req = requests.get(url1)
data = req.json()
print(data)
