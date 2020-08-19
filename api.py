import requests
from requests.exceptions import HTTPError


def get_data_from_api():
    try:
        response = requests.get('https://randomuser.me/api/')
        response.raise_for_status()
        json_response = response.json()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

    return json_response

records = get_data_from_api()

for record in range(10):
    one_record = get_data_from_api()
    one_record = one_record["results"]
    for key, value in records.items():
        if key == "results":
            value += one_record

print(records)