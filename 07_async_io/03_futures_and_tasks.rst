Futures and tasks
###################

Example 1
---------

**Basic usage of tasks**

.. code-block:: python

    import asyncio


    async def sleeper(delay):
        await asyncio.sleep(delay)
        print('Finished sleeper with delay: {:.1f}'.format(delay))

*Create an event loop*

>>> loop = asyncio.get_event_loop()

*Create the task*

>>> result = loop.call_soon(loop.create_task, sleeper(1))

*Make sure the loop stops after 2 seconds*

>>> result = loop.call_later(2, loop.stop)

*Start the loop and make it run forever
Or at least until the loop.stop gets called in 2 seconds.*

>>> loop.run_forever()
Finished sleeper with delay: 1.0

Example 2
---------

**Print stack of all tasks for debugging purposes**

.. code-block:: python

    import asyncio


    async def stack_printer():
        for task in asyncio.Task.all_tasks():
            task.print_stack()

*Create an event loop*

>>> loop = asyncio.get_event_loop()

*Create the task*

>>> result = loop.run_until_complete(stack_printer())
Stack for <Task pending...