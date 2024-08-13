import requests
import tokens
import random
import json

URL = "https://api.artifactsmmo.com/my/"
MOVE = "/action/move"

FRANI = "Frani"
GARRET = "Garret"
BULOCHKA = "Bulochka"

HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": "Bearer " + tokens.MY_TOKEN
}

def moveFrani(x, y):
    x = random.randint(-5, 11)
    y = random.randint(-15, 15)


    payload = {
        "x": x,
        "y": y
    }

    response = requests.post(URL + FRANI + MOVE, json=payload, headers=HEADERS)

    content = json.load(response)

    print(content)

    print(response.json())
