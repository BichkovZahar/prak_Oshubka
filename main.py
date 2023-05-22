import requests
class InvalidUrlError(Exception):
    def __init__(self, url):
        self.url = url
        super().__init__('Invalid URL: {}'.format(url))

def fetch_data_from_url(url):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            raise InvalidUrlError(url)
        else:
            print('Вірний URL:', url)
    except requests.exceptions.RequestException:
        raise InvalidUrlError(url)

try:
    url = input('Введить URL: ')
    fetch_data_from_url(url)
except InvalidUrlError as a:
    print(a)