import requests
import asyncio
import json
import logging


logging.basicConfig(filename='client.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)

request_api2 = {'request' : 'hello from cycle2'}

async def send_request_to_api1():
    while True:
        response1 = requests.get('http://localhost:5000/api1')
        logging.info('response from api1 : {}'.format(response1.json()))
        await asyncio.sleep(2.0)

async def send_request_to_api2():
    while True:
        response2 = requests.post('http://localhost:5000/api2', headers={'Content-Type': 'application/json'},
                                  data=json.dumps(request_api2))
        logging.info('response from api2 : {}'.format(response2.json()))
        await asyncio.sleep(3.0)

def main():
    cycle1 = asyncio.ensure_future(send_request_to_api1())
    cycle2 = asyncio.ensure_future(send_request_to_api2())

    yield from asyncio.gather(cycle1, cycle2)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()