import requests

s_city = "Moscow,RU"
appid = "0e79b59c56fc67936f82f0be0e5d5542"
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                   params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Город:", s_city)
print("Погодные условия☁:", data['weather'][0]['description'])
print("Температура🌡:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])
print("Видимость", data['visibility'])
print("Скорость ветра💨", data['wind']['speed'])
print("____________________________")

res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nТемпература🌡 <",
          '{0:+3.0f}'.format(i['main']['temp']), "> \r\nПогодные условия☁ <",
          i['weather'][0]['description'], ">", "Скорость ветра💨 <", i['wind']['speed'], "> \r\nВидимость <", i['visibility'], ">")
    print("____________________________")
