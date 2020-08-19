import requests
from requests.exceptions import HTTPError


def get_data_from_api():
    try:
        response = requests.get('https://randomuser.me/api/?results=1000')
        response.raise_for_status()
        json_response = response.json()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

    return json_response