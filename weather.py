from pyowm import OWM
from translate import Translator

def get_weather():
    translator = Translator(to_lang="ru")
    token = "2a9fbb22b26dc0418c51e9268680be1c"
    owm = OWM(token)
    manager = owm.weather_manager()
    weather = manager.weather_at_place("izhevsk,RU").weather
    temp = weather.temperature("celsius")
    status = weather.detailed_status
    status = translator.translate(str(status))
    full_respone = F"Сегодня {status}.\nСредняя температура на сегодня {round(int(temp['temp']))}°C.\nЧувствуется на {round(int(temp['feels_like']))}°C."
    return full_respone