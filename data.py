import json

import requests
from requests.exceptions import HTTPError


class DataFile:
    def __init__(self, file_name):
        self.file = self.set_data(file_name)

    def set_data(self, file_name):
        with open(file_name, encoding='utf-8') as f:
            json_content = json.load(f)
        return json_content


class DataAPI:
    def __init__(self, num_results):
        self.num_results = num_results
        self.response = self.get_api_data()

    def _get_url(self):
        url = f'https://randomuser.me/api/?results={self.num_results}'
        return url

    def get_api_data(self):
        try:
            url = self._get_url()
            response = requests.get(url=url)
            json_response = response.json()
            return json_response
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')

    def create_json(self):
        with open('persons_api.json', 'w') as write_file:
            json.dump(self.response, write_file, indent=4)

# data = DataAPI(num_results=50)
# print(data.response)
