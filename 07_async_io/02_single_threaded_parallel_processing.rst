Single-threaded parallel processing
####################################

Example 1
---------

**Example implementation of asyncronous function calls**

.. code-block:: python

    import asyncio


    async def sleeper(delay):
        await asyncio.sleep(delay)
        print('Finished sleeper with delay: {:.1f}'.format(delay))


>>> loop = asyncio.get_event_loop()
>>> results = loop.run_until_complete(
...     asyncio.wait((sleeper(0.1), sleeper(0.3), sleeper(0.2),)))
Finished sleeper with delay: 0.1
Finished sleeper with delay: 0.2
Finished sleeper with delay: 0.3
