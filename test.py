import os
import telebot
bot = telebot.TeleBot("1319907565:AAHkQ3D0-JTMlf5bEn9FigYFc02IHTo305s")
@bot.message_handler(content_types=["text"])
def body(message):
    bot.send_message(message.chat.id, os.getenv("fuck"))

bot.polling(none_stop=True)