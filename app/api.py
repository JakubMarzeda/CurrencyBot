import requests

def get_data_from_API(link):
    return requests.get(link).json()

gold_price = get_data_from_API("https://api.nbp.pl/api/cenyzlota/?format=json")[0]["cena"]
euro_price = get_data_from_API("https://api.nbp.pl/api/exchangerates/rates/A/EUR/?format=json")["rates"][0]["mid"]
usd_price = get_data_from_API("https://api.nbp.pl/api/exchangerates/rates/A/USD/?format=json")["rates"][0]["mid"]