from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import sys

sys.path.insert(1, '.\secrets')

from secrets import *
from crypto_symbols import *

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': API_TOKEN,
}

session = Session()
session.headers.update(headers)

try:
    for crypt in crypto:
        response = session.get(quotes_url+'?symbol='+crypt)
        data = list(json.loads(response.text)['data'].values())[0]['quote']
        quote = list(data.values())[0]
        print(quote['price'])
except(ConnectionError, Timeout, TooManyRedirects) as error:
    print(error)
