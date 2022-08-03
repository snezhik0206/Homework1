import requests


def search_hero():
    response = requests.get(url="https://akabab.github.io/superhero-api/api/all.json")
    dictionary = response.json()

    heroes = ["Hulk", "Captain America", "Thanos"]
    max_inteligence = 0
    for hero in dictionary:
        if hero["name"] in heroes:
            if hero["powerstats"]["intelligence"] > max_inteligence:
                max_inteligence = hero["powerstats"]["intelligence"]
                max_inteligence_hero = hero["name"]

    print(f"Самый умный герой: {max_inteligence_hero}")


search_hero()
