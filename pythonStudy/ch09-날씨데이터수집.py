import json
import requests

api_key = "여기에 복사한 API 키 붙여넣기"
city_name = "Seoul"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
data = requests.get(url)
# print(data.text["name"])
data_dict = json.loads(data.text)
# print(data_dict)
print(f"도시명 : {data_dict['name']}")
print(f"현재 날씨 : {data_dict['weather'][0]['main']}") 
print(f"현재 기온 : {round(data_dict['main']['temp'] - 273.15)}도")
print(f"체감 기온 : {round(data_dict['main']['feels_like'] - 273.15)}도")
print(f"습도 : {data_dict['main']['humidity']} %")
print(f"풍속 : {data_dict['wind']['speed']} m/s")