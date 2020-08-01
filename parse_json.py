import json

JSON_NAME = "persons.json"


def get_gender(json_name):
    json_file = open(json_name, 'r')
    json_data = json_file.read()
    obj = json.loads(json_data)
    obj = obj['results'][0]["gender"]
    return obj