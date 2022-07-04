''' 1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев
 для конкретного пользователя, сохранить JSON-вывод в файле *.json.'''

import requests
import json

link_1 = "https://api.github.com"
user = "EvgeniyaSobolevskaya"
response = requests.get(f"{link_1}/users/{user}/repos")
j_data = response.json()
print(response.url)
for el in j_data:
    print(f"Репозиторий {el['name']}")
with open('data.json', 'w') as file:
    json.dump(j_data, file)
