from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import sys

sys.path.insert(1, '.\secrets')
from secrets import *

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': API_TOKEN,
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(quotes_url+'?symbol=SHIB')
    data = json.loads(response.text)
    print(data['data'])
except(ConnectionError, Timeout, TooManyRedirects) as error:
    print(error)
