Priming coroutines
###################

Example 1
---------

**A custom implementation of the @coroutine decorator, 
that converts an ordinary function to a coroutine**

.. code-block:: python

    import functools


    def coroutine(function):
        @functools.wraps(function)
        def _coroutine(*args, **kwargs):
            active_coroutine = function(*args, **kwargs)
            next(active_coroutine)
            return active_coroutine
        return _coroutine


    @coroutine
    def spam():
        while True:
            print('Waiting for yield...')
            value = yield
            print('spam received: {}'.format(value))

>>> generator = spam()
Waiting for yield...

>>> generator.send('a')
spam received: a
Waiting for yield...

>>> generator.send('b')
spam received: b
Waiting for yield...
