Event loop usage
#################

Example 1
---------

**Example usage of call_at(), call_soon() and call_later()**

.. code-block:: python

    import time
    import asyncio


    t = time.time()

    def printer(name):
        print('Started {} at {:.1f}'.format(name, time.time() - t))
        time.sleep(0.2)
        print('Finished {} at {:.1f}'.format(name, time.time() - t))


>>> loop = asyncio.get_event_loop()
>>> result = loop.call_at(loop.time() + .2, printer, 'call_at')
>>> result = loop.call_later(.1, printer, 'call_later')
>>> result = loop.call_soon(printer, 'call_soon')
>>> result = loop.call_soon_threadsafe(printer, 'call_soon_threadsafe')

*Make sure we stop after a second*

>>> result = loop.call_later(1, loop.stop)

>>> loop.run_forever()
Started call_soon at 0.0
Finished call_soon at 0.2
Started call_soon_threadsafe at 0.2
Finished call_soon_threadsafe at 0.4
Started call_later at 0.4
Finished call_later at 0.6
Started call_at at 0.6
Finished call_at at 0.8

Example 2
---------

**Example usage of call_at(), call_soon() and call_later()
with create_task**

.. code-block:: python

    import time
    import asyncio


    t = time.time()

    async def printer(name):
        print('Started {} at {:.1f}'.format(name, time.time() - t))
        time.sleep(0.2)
        print('Finished {} at {:.1f}'.format(name, time.time() - t))

>>> loop = asyncio.get_event_loop()

>>> result = loop.call_at(
    loop.time() + .2, loop.create_task, printer('call_at'))

>>> result = loop.call_later(
    .1, loop.create_task, printer('call_later'))

>>> result = loop.call_soon(
    loop.create_task, printer('call_soon'))

>>> result = loop.call_soon_threadsafe(
    loop.create_task, printer('call_soon_threadsafe'))

*Make sure we stop after a second*

>>> result = loop.call_later(1, loop.stop)

>>> loop.run_forever()
Started call_soon at 0.0
Started call_soon_threadsafe at 0.0
Started call_later at 0.1
Started call_at at 0.2
Finished call_soon at 0.2
Finished call_soon_threadsafe at 0.2
Finished call_later at 0.3
Finished call_at at 0.4
