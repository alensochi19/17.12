import requests
import json
from config import keys

class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        amount = amount.replace(",", ".")
        if quote == base:
            raise ConvertionException(f'Вы ввели две одинаковые валюты "{base}", введите разные валюты для конвертации')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Вы допустили ошибку в наименовании валюты "{quote}", воспользуйтесь списком доступных валют /value')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Вы допустили ошибку в наименовании валюты "{base}", воспользуйтесь списком доступных валют /value')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Вы допустили ошибку в количестве валюты "{amount}"')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]] * amount

        return '%.2f' % total_base
