Coroutines
###########

Example 1
---------

**Basic usage**

.. code-block:: python

    def generator():
        value = yield 'spam'
        print('Generator received: {}'.format(value))
        yield 'Previous value: {}'.format(value)

>>> g = generator()

>>> print('Result from generator: {}'.format(next(g)))
Result from generator: spam

>>> print(g.send('eggs'))
Generator received: eggs
Previous value: 'eggs'
