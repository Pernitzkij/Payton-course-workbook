
import requests
import json

# print(swapi.get_film(1))
# Сейчас библиотека не работает, получить начало сюжета можно напрямую

result = requests.get("https://swapi.dev/api/films/3/")

json_dict = json.loads(result.text)

with open("swap2.json", "w") as file:
    json_text = json.dump(json_dict, file, indent=4)

print(json_dict["opening_crawl"])