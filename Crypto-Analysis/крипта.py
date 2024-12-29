import requests


def get_crypto_price(api_key, symbol):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }
    parameters = {
        'symbol': symbol,
        'convert': 'USD'
    }

    response = requests.get(url, headers=headers, params=parameters)

    try:
        data = response.json()
    except ValueError:
        print("Ошибка преобразования ответа в JSON.")
        print(f"Статус-код ответа: {response.status_code}")
        print(f"Ответ от API: {response.text}")
        return None

    if response.status_code == 200:
        try:
            price = data['data'][symbol]['quote']['USD']['price']
            return price
        except KeyError:
            print("Ошибка извлечения данных. Проверь параметры запроса.")
            print(f"Ответ от API: {data}")
            return None
    else:
        print(f"Ошибка: {data['status']['error_message']}")
        return None



api_key = '4021f0d9-56b4-4eb2-812c-962be1765941'
symbol = 'TON'
price = get_crypto_price(api_key, symbol)

if price:
    print(f"Стоимость {symbol} в USD: {round(price,5)}")