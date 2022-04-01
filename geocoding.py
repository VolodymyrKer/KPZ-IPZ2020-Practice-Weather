import json
from urllib.request import urlopen
import settings


def get_coordinates():
    result = []
    r = urlopen(
        f"http://api.openweathermap.org/geo/1.0/direct?q={settings.CITY}&limit=5&appid={settings.API_KEY}")
    j = json.loads(r.read())
    result.append(j[0].get("lat"))
    result.append(j[0].get("lon"))
    return result

