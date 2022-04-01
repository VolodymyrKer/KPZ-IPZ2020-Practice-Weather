from datetime import datetime
import json
from urllib.request import urlopen
import settings
from geocoding import get_coordinates


def get_forecast_five_day():
    forecast = []
    coordinates = get_coordinates()
    r = urlopen(
        f"https://api.openweathermap.org/data/2.5/forecast?lat={coordinates[0]}&"
        f"units=metric&"
        f"lon={coordinates[1]}&"
        f"appid={settings.API_KEY}")
    j = json.loads(r.read())
    for element in j.get("list"):
        forecast.append(f"------------------------------------------------------\n"
                        f"Погода о {datetime.fromtimestamp(element.get('dt'))}\n"
                        f"Температура: {element.get('main').get('temp')}°C\n"
                        f"Відчувається як: {element.get('main').get('feels_like')}°C\n"
                        f"Мінімальна температура: {element.get('main').get('temp_min')}°C\n"
                        f"Мінімальна температура: {element.get('main').get('temp_max')}°C\n"
                        f"Атмосферний тиск на рівні моря: {round(element.get('main').get('sea_level') / 1.33)} мм.рт.ст.\n"
                        f"Атмосферний тиск на рівні землі: {round(element.get('main').get('grnd_level') / 1.33)} мм.рт.ст.\n"
                        f"Влажність: {element.get('main').get('humidity')}%\n"
                        f"Швидкість вітру: {element.get('wind').get('speed')} м/с\n"
                        f"------------------------------------------------------")
    return forecast
