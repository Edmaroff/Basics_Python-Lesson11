from pprint import pprint
import time
import requests


class Stackoverflow:

    def get_unix_time(self, quantity_day=2):
        number_seconds = 86400 * quantity_day
        current_date = int(time.time())
        past_date = current_date - number_seconds
        return [current_date, past_date]

    def get_list_questions(self, tag, quantity_day):
        url = "https://api.stackexchange.com/2.3/questions"
        params = {
            'tagged': tag,
            'fromdate': self.get_unix_time()[-1],
            'todate': self.get_unix_time()[0],
            'site': 'stackoverflow'
        }
        response = requests.get(url,params=params)
        questions_list = response.json()
        return questions_list['items']


if __name__ == '__main__':
    stack = Stackoverflow()
    quantity_day = 2
    tags = 'Python'
    list_questions = stack.get_list_questions(tags, quantity_day)
    print(f'Количество вопросов за последние {quantity_day} дня с тегом "{tags}" = {len(list_questions)} шт.')
    # pprint(list_questions)

