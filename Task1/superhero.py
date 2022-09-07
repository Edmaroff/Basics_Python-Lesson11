import requests

class Superhero:

    def get_list_superhero(self):
        url = 'https://akabab.github.io/superhero-api/api/all.json'
        response = requests.get(url)
        return response.json()

    def get_smart_hero(self, list_hero):
        powerstats_character = {}
        # a = self.get_list_superhero()
        for hero in self.get_list_superhero():
            if hero['name'] in list_hero:
                powerstats_character.setdefault(hero['name'], hero['powerstats']['intelligence'])
        max_int_character = [k for k, v in powerstats_character.items() if
                            v==max(powerstats_character.values())]
        print(f'Cамый умный персонаж — "{max_int_character[0]}". \nИнтелект = {powerstats_character[max_int_character[0]]}.')
