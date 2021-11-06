from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import sys
import asyncio
sys.path.insert(1, '.\secrets')

from secrets import *
from crypto_symbols import *

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': API_TOKEN,
}

session = Session()
session.headers.update(headers)

async def get_latest_quote():
    try:
        quote=[]
        for crypt in crypto:
            response = session.get(quotes_url+'?symbol='+crypt)
            crypt_key=list(json.loads(response.text)['data'].keys())[0]
            data = list(json.loads(response.text)['data'].values())[0]['quote']
            old_key=list(data.keys())
            data[crypt_key]=data.pop(old_key[0])
            quote.append(data)
        current_quote=json.dumps(quote)  
        return current_quote
    except(ConnectionError, Timeout, TooManyRedirects) as error:
        print(error)

loop = asyncio.get_event_loop()
response = loop.run_until_complete(get_latest_quote())

    
