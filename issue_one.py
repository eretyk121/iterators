import requests
import json

def wikipedia():
    session = requests.Session()
    with open('countries.json', encoding='utf-8') as country:
        json_data = json.load(country)
        for con in json_data:
            name = con['name']['common']
            response = session.get(f'https://ru.wikipedia.org/wiki/{name}')
            url = response.url
            yield {name: url}

if __name__ == '__main__':

    with open('result.txt', 'w', encoding='utf-8') as text:
         for one in wikipedia():
            for key, val in one.items():
                text.write(f'{key}: {val} \n')