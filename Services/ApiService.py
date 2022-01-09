import configparser
import requests
import time
import random


class ApiService:

    def __init__(self):

        try:

            self.config = configparser.ConfigParser()
            self.config.read('config.ini')
            self.token = self.config.get('CONNECT', 'TOKEN')
            self.url = self.config.get('CONNECT', 'URL')
            self.device_name = self.config.get('CONNECT', 'NAME_DEVICE')

        except Exception as e:
            print("Error al leer la configuración: " + e)

    def post_request(self, payload):
        # Creates the headers for the HTTP requests
        url = "{}/api/v1.6/devices/{}".format(self.url, self.device_name)
        headers = {"X-Auth-Token": self.token,
                   "Content-Type": "application/json"}

        # Makes the HTTP requests
        status = 400
        attempts = 0
        while status >= 400 and attempts <= 5:
            req = requests.post(url=url, headers=headers, json=payload)
            status = req.status_code
            attempts += 1
            # time.sleep(1)

        print(req.status_code, req.json())
        if status >= 400:
            return False

        return True

    def build_payload(self, variables=[]):
        pass

    def fake_data(self):
        result = random.randint(-10, 50)
        return result
