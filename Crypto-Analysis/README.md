# Crypto Price Fetcher

## Project Description

This is a Python script that retrieves the current price of a cryptocurrency in USD using the CoinMarketCap API. It accepts an API key and the symbol of the cryptocurrency as input and returns its price in USD.

## Features

- Fetches the latest price of a cryptocurrency using the CoinMarketCap API.
- Handles errors gracefully with clear messages for debugging.
- Allows for easy customization by changing the cryptocurrency symbol and API key.

## Requirements

- Python 3.6 or later
- Requests library

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Kowalski1212/Crypto-Analysis/crypto-price-fetcher.git
    cd crypto-price-fetcher
    ```

2. Install the required dependencies:

    ```bash
    pip install requests
    ```

## Usage

1. Obtain a free API key from [CoinMarketCap](https://coinmarketcap.com/api/).

2. Replace the placeholder API key in the script with your own:

    ```python
    api_key = 'your_api_key_here'
    ```

3. Set the cryptocurrency symbol (e.g., `BTC`, `ETH`, `TON`) in the script:

    ```python
    symbol = 'TON'
    ```

4. Run the script:

    ```bash
    python crypto_price_fetcher.py
    ```

5. Example output:

    ```
    Стоимость TON в USD: 2.34567
    ```

## Example Code

Here’s the core function used in the script:

```python
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