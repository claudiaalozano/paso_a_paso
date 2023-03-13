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

async def download(session, uri):
    content = await wget(session, uri)
    if content is None:
        return None
    with open(uri.split(sep)[-1], "wb") as f:
        f.write(content)
        return uri
    