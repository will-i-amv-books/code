##################################################
# Using asyncio - Python 3.4

import asyncio


@asyncio.coroutine
def sleeper():
    yield from asyncio.sleep(0.1)

##################################################
# Using asyncio - Python 3.5+

import asyncio


async def sleeper():
    await asyncio.sleep(0.1)
