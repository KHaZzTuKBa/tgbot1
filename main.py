# coding=utf-8
import horoscopes
import telebot
from weather import get_weather
from news import news
from covid import get_stat
from keyboard_file import kbs

ids = [
    "1024128147",
    "629381447"
]

main_buttons = [
        "Узнать погоду",
        "Узнать количество пробок",
        "Гороскоп",
        "Показать статистику по коронавирусу",
        "Новости",
        "Предложения по улучшению бота"
    ]

bot = telebot.TeleBot("1319907565:AAHkQ3D0-JTMlf5bEn9FigYFc02IHTo305s")

@bot.message_handler(commands=['start'])
def hello(message):
    print(message.text)
    bot.send_message(message.chat.id, F"Привет, {message.from_user.username} Спасибо, что подписались на меня. Я буду очень рад, если вы будете мной пользоваться.", reply_markup=kbs(main_buttons))

@bot.message_handler(content_types=['text'])
def body(message):
    print(message.from_user.username, message.text)
    if message.text == "Узнать погоду":
        weather = get_weather()
        bot.send_message(message.chat.id, weather)

    elif message.text == "Гороскоп":
        hors = horoscopes.find_links().keys()
        bot.send_message(message.chat.id, "Выбирете свой гороскоп", reply_markup=kbs(hors))
        bot.register_next_step_handler(message, horoscope)

    elif message.text == "Показать статистику по коронавирусу":
        bot.send_message(message.chat.id, get_stat())

    elif message.text == "Новости":
        themes = {i["theme"] for i in news()}
        themes = list(themes)
        bot.send_message(message.chat.id, "Выбирете тему для новостей", reply_markup=kbs(themes))
        bot.register_next_step_handler(message, send_news)

    elif message.text == "Узнать количество пробок":
        bot.send_message(message.chat.id, "На данный момент пробки в ижевске оцениваются в 3 балла.")
        bot.send_message(message.chat.id, "Для более подробного ознакомления вы можете посмотреть карту целиком : https://clck.ru/TMSto", reply_markup=kbs(main_buttons))


    elif message.text == "Предложения по улучшению бота":
        bot.send_message(message.chat.id, "Кратко опишите свое предложение по улучшению работы бота")
        bot.register_next_step_handler(message, supply)

    elif message.text == "id":
        bot.send_message(message.chat.id, message.chat.id)

    else:
        bot.send_message(message.chat.id, "На данный момент такой функции нет.", reply_markup=kbs(main_buttons))

def supply(message):
    for i in ids:
        bot.send_message(i, F"{message.from_user.username} хочет, чтобы вы добавили функцию: {message.text}")
    bot.send_message(message.chat.id, "Ваш запрос добавлен в список улучшений. Спасибо за помощь!")

def send_news(message):
    themes = {i["theme"] for i in news()}
    themes = list(themes)
    need_news = [i if i["theme"] == message.text else None for i in news()]
    for i in need_news:
        try:
            need = "\n\n".join([i['theme'], i['idea'], i['epilog'], "Дата создания: " + i["date"], "Ссылка на полную статью: " + i["link"]])
            bot.send_message(message.chat.id, need, reply_markup=kbs(main_buttons))
        except TypeError:
            pass

def horoscope(message):
    link = horoscopes.find_links()[message.text]
    text = horoscopes.get_info(link)
    bot.send_message(message.chat.id, text, reply_markup=kbs(main_buttons))


bot.polling(none_stop=True)