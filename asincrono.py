#libreria asincrona
import asyncio
#importa el módulo aiohttp
from aiohttp import *

async def main(uri):
    async with aiohttp.ClientSession() as session:
        async with session.get(uri) as response:
            if response.status != 200:
                return None
            if response.content_type.startwith("text/"):
                return await response.text()
            else:
                return await response.read()

asyncio.run(main("http://www.formation-python.com/"))

async def wget(session, uri):
    async with session.get(uri) as response:
        if response.status != 200:
            return None
        if response.content_type.startwith("text/"):
            return await response.text()
        else:
            return await response.read()

