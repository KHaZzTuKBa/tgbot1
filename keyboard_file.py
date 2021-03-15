from telebot import types

def kbs(buttons):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

    for i in buttons:
        kb.add(types.KeyboardButton(i))

    return kb