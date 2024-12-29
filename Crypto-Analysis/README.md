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
    git clone https://github.com/Kowalski1212/Practical-methods-in-the-field-of-data-analysis/blob/main/Crypto-Analysis
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

Here is the main script used to fetch cryptocurrency prices:

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
        print("Error parsing the API response to JSON.")
        print(f"Response status code: {response.status_code}")
        print(f"API Response: {response.text}")
        return None

    if response.status_code == 200:
        try:
            price = data['data'][symbol]['quote']['USD']['price']
            return price
        except KeyError:
            print("Error extracting price data. Check the request parameters.")
            print(f"API Response: {data}")
            return None
    else:
        print(f"Error: {data['status']['error_message']}")
        return None


# Example usage
api_key = 'your_api_key_here'
symbol = 'TON'
price = get_crypto_price(api_key, symbol)

if price:
    print(f"The price of {symbol} in USD: {round(price, 5)}")
