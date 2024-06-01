import requests
import hashlib
import hmac
import time

class GateAPI:
    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key
        self.base_url = 'https://api.gate.io/api/v4/'

    def _generate_signature(self, data):
        signature = hmac.new(self.secret_key.encode(), data.encode(), hashlib.sha512).hexdigest()
        return signature

    def _create_headers(self, signature):
        headers = {
            'KEY': self.api_key,
            'SIGNATURE': signature
        }
        return headers

    def get_balance(self):
        endpoint = 'spot/accounts'
        timestamp = str(int(time.time() * 1000))
        data = timestamp + 'GET' + endpoint
        signature = self._generate_signature(data)
        headers = self._create_headers(signature)
        url = self.base_url + endpoint
        response = requests.get(url, headers=headers)
        return response.json()

    def get_market_info(self, symbol):
        endpoint = f'spot/tickers/{symbol}'
        url = self.base_url + endpoint
        response = requests.get(url)
        return response.json()

    def place_order(self, symbol, side, amount, price, order_type='limit'):
        endpoint = 'spot/orders'
        timestamp = str(int(time.time() * 1000))
        data = timestamp + 'POST' + endpoint + f'symbol={symbol}&side={side}&amount={amount}&price={price}&type={order_type}'
        signature = self._generate_signature(data)
        headers = self._create_headers(signature)
        url = self.base_url + endpoint
        payload = {
            'symbol': symbol,
            'side': side,
            'amount': amount,
            'price': price,
            'type': order_type
        }
        response = requests.post(url, headers=headers, json=payload)
        return response.json()

    def cancel_order(self, order_id):
        endpoint = f'spot/orders/{order_id}'
        timestamp = str(int(time.time() * 1000))
        data = timestamp + 'DELETE' + endpoint
        signature = self._generate_signature(data)
        headers = self._create_headers(signature)
        url = self.base_url + endpoint
        response = requests.delete(url, headers=headers)
        return response.json()

