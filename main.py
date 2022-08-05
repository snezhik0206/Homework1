import requests


def search_hero():
    response = requests.get(url="https://akabab.github.io/superhero-api/api/all.json")
    hero_list = response.json()

    heroes = ["Hulk", "Captain America", "Thanos"]
    max_intelligence = 0
    heroes_filter_object = filter(lambda hero: hero.get('name') in heroes, hero_list)

    for hero in list(heroes_filter_object):
        if hero['powerstats']['intelligence'] > max_intelligence:
            max_intelligence = hero['powerstats']['intelligence']
            max_intelligence_hero = hero['name']

    print(f"Самый умный герой: {max_intelligence_hero}")


search_hero()
