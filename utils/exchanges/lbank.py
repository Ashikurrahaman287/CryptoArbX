import requests
import hashlib
import hmac
import time

class LBankAPI:
    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key
        self.base_url = 'https://api.lbkex.com/v2/'

    def _generate_signature(self, data):
        signature = hmac.new(self.secret_key.encode(), data.encode(), hashlib.sha256).hexdigest()
        return signature

    def _create_headers(self, signature):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'ACCESS-KEY': self.api_key,
            'SIGNATURE': signature
        }
        return headers

    def _request(self, method, endpoint, params=None):
        url = self.base_url + endpoint
        if params is None:
            params = {}
        timestamp = int(time.time() * 1000)
        params['api_key'] = self.api_key
        params['time'] = timestamp
        query_string = '&'.join([f'{key}={params[key]}' for key in sorted(params)])
        data = f'{method.upper()}{url}{query_string}'
        signature = self._generate_signature(data)
        headers = self._create_headers(signature)
        if method == 'GET':
            response = requests.get(url, headers=headers, params=params)
        elif method == 'POST':
            response = requests.post(url, headers=headers, json=params)
        return response.json()

    def get_balance(self):
        endpoint = 'account_info'
        params = {}
        return self._request('POST', endpoint, params)

    def get_market_info(self, symbol):
        endpoint = 'currency_pairs_info'
        params = {'symbol': symbol}
        return self._request('GET', endpoint, params)


