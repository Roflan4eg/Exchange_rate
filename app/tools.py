import requests
import json
from conf import API_KEY


def currency_converter(fr, to, amount):
    headers = {
        "apikey": API_KEY,
    }

    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={fr}&amount={amount}"
    response = requests.get(url, headers=headers).json()
    return round(response['result'], 2)


def check_valid(fr, to):
    with open("symbols.json", "r") as f:
        syms = json.load(f)
        return fr in syms and to in syms
