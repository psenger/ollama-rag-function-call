import json
import requests

from env import API_URL, AI_MODEL


def main(country):
    print(f'Calling {API_URL}')
    schema = {
        "city": {
            "type": "string",
            "description": "The name of the city"
        },
        "latitude": {
            "type": "float",
            "description": "Decimal latitude of the city"
        },
        "longitude": {
            "type": "float",
            "description": "Decimal longitude of the city"
        }
    }
    payload = {
        "model": AI_MODEL,
        "messages":[
            {
                "role": "system",
                "content": "You are a helpful AI assistant. " +
                           "The user will enter a country name and as the assistant will return the decimal latitude " +
                           "and decimal longitude of the capital of the country with the capital city name. Your output "
                           f"should be in in JSON format using the schema defined here: {schema}"
            },
            {
                "role": "user",
                "content": "France"
            },
            {
                "role": "assistant",
                "content": "{\"city\":\"Paris\", \"latitude\":48.8556, \"longitude\":2.3522 }"
            },
            {
                "role": "user",
                "content": country
            }
        ],
        "format": "json",
    }

    res = requests.post(API_URL, json=payload)

    for message in res.iter_lines():
        json_str = json.loads(message)
        print(json_str["message"]["content"], end="")

if __name__ == '__main__':
    main("australia")

