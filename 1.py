def smartest_hero(name_heroes):
    url = 'https://akabab.github.io/superhero-api/api//all.json'
    response = requests.get(url=url)
    all_heroes = name_heroes.split(', ')
    heroes = {}
    intelligence_level = []
    for i in response.json():
        if i.get('name') in all_heroes:
            heroes[i['name']] = i['powerstats']['intelligence']
    for number in heroes.values():
        intelligence_level.append(int(number))
    for key, value in heroes.items():
        if value == max(intelligence_level):
            res = f'{key} cамый умный герой. Его интеллект - {value}!'
    return print(res)

if __name__ == '__main__':
    smartest_hero('Hulk, Captain America, Thanos')