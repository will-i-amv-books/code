Decorators
####################

Example 1
---------

.. code-block:: python

    import functools

    def eggs(function):
        @functools.wraps(function)
        def _eggs(*args, **kwargs):
            print('{} got args: {} and kwargs: {}'.format(
                function.__name__, args, kwargs))
            return function(*args, **kwargs)
        return _eggs

    @eggs
    def spam(a, b, c):
        return a * b + c

>>> spam(1, 2, 3)
'spam' got args: (1, 2, 3) and kwargs: {}
5
