"""
Модуль для конвертации валют через API сайта cryptocompare.com
Классы:
    APIException: Пользовательское исключение для обработки ошибок
    CurrentConvertor: Класс со статическим методом get_price() для получения курса валют
"""

import requests
import json
from config import keys

class APIException(Exception):
       pass

class CurrentConvertor:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        # Проверка на несовпадение валют
        if quote==base:
            raise APIException(f'Нельзя переводить одинаковую валюту {quote}.')
        #Получаем тикеры валют
        try:
            quote_ticker= keys[quote]
        except KeyError:
            raise APIException(f'Нельзя удалось обработать валюту {quote}')
        try:
            base_ticker =keys[base]
        except KeyError:
            raise APIException(f'Нельзя удалось обработать валюту  {base}')
        # Проверка на число типа float
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'"{amount}" Не является числом')
        # Проверка на всякий случай, если будет недоступно API
        try:
            r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
            total_base = json.loads(r.content)[keys[base]]
            return total_base
        except Exception as e:
            raise APIException(f'Ошибка при получении курса: {e}')
