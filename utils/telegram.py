import requests

class TelegramBot:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}/'

    def send_message(self, chat_id, text):
        endpoint = 'sendMessage'
        params = {'chat_id': chat_id, 'text': text}
        url = self.base_url + endpoint
        response = requests.post(url, json=params)
        return response.json()

    def send_photo(self, chat_id, photo_url, caption=None):
        endpoint = 'sendPhoto'
        params = {'chat_id': chat_id, 'photo': photo_url, 'caption': caption}
        url = self.base_url + endpoint
        response = requests.post(url, json=params)
        return response.json()

    def send_document(self, chat_id, document_url, caption=None):
        endpoint = 'sendDocument'
        params = {'chat_id': chat_id, 'document': document_url, 'caption': caption}
        url = self.base_url + endpoint
        response = requests.post(url, json=params)
        return response.json()

    def get_updates(self, offset=None, limit=None, timeout=None):
        endpoint = 'getUpdates'
        params = {'offset': offset, 'limit': limit, 'timeout': timeout}
        url = self.base_url + endpoint
        response = requests.get(url, params=params)
        return response.json()


