import requests
from typing import Dict


class Sender:
    def __init__(self, message: Dict, telegram_bot_url: str):
        self.message = message
        self._telegram_bot_url = telegram_bot_url

    def send_message(self):
        try:
            response = requests.post(self._telegram_bot_url, json=self.message)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}

    def run(self):
        return self.send_message()
