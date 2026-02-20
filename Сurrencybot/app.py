"""
Основной модуль

Команды:
/start, /help - справка
/values - список доступных валют
Шаблон сообщения: <исходная валюта> <целевая валюта> <количество>
"""

import telebot
from config import keys,Token
from extensions import APIException,CurrentConvertor

bot = telebot.TeleBot(Token)
@bot.message_handler(commands=['start','help'])
def help(message: telebot.types.Message):
    text ='Введите параметры ЧЕРЕЗ ПРОБЕЛ в следующем формате:\n \
    1. <имя валюты, из которой переводим>\n \
    2. <имя валюты, в которую переводим>\n \
    3. <количество первой валюты>\n \
    Команда /values для вывода доступных валют'
    bot.reply_to(message,text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text ='Доступные валюты:'
    for key in keys.keys():
     text=   '\n'.join((text, key))
    bot.reply_to(message,text)
@bot.message_handler(content_types=['text'])
def get_price(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        #проверка на равенство 3-м атрибутам
        if len(values) != 3:
            raise APIException('Должно быть 3 атрибутов(через пробел из какой валюты, в какую валюту и кол-во)')
        quote, base, amount = values
        total_base = CurrentConvertor.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message,f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message,f'Не удалось обработать команду\n{e}')
    else:
        sum = float(total_base) * float(amount)
        text = f"Цена {amount} {quote} в {sum}"
        bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)
