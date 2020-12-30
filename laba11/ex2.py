from collections import namedtuple
import time
import asyncio
from concurrent.futures import FIRST_COMPLETED
import aiohttp

Service = namedtuple('Service', ('name', 'url', 'ip_attr'))

SERVICES = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'query')
)

async def fetch_ip(service , session):
    # получение ip
    async with session.get(service.url) as resp:
        ip = await resp.text()


async def asynchronous():
    # TODO:
    # создание футур для сервисов
    # используйте FIRST_COMPLETED
    async with aiohttp.ClientSession() as session:
        fut = await asyncio.wait([fetch_ip(service , session) for service in SERVICES], return_when=FIRST_COMPLETED)
        for i in fut[0]:
            print(i.result())

ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchronous())