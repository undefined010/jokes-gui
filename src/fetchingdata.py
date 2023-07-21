import requests


class JokesApi:

    @staticmethod
    def get_random_joke() -> str:
        url = 'https://icanhazdadjoke.com/slack'
        req = requests.get(url)

        if req.status_code != 200:
            print('fuck at line 13 JokesApi')
            exit(1)

        return req.json()['attachments'][0]['text']
