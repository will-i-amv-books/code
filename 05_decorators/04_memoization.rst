Using decorators for memoization
#################################

Example 1
----------

**Example of memoization**

.. code-block:: python

    import functools

    def memoize(function):
        function.cache = dict()
        @functools.wraps(function)
        def _memoize(*args):
            if args not in function.cache:
                function.cache[args] = function(*args)
            return function.cache[args]
        return _memoize

    @memoize
    def fibonacci(n):
        if n < 2:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

>>> fibonacci(10)
55
>>> fibonacci.__wrapped__.cache
{(1,): 1, (0,): 0, (2,): 1, (3,): 2, (4,): 3, (5,): 5, 
(6,): 8, (7,): 13, (8,): 21, (9,): 34, (10,): 55}

Example 2
----------

**Using the lru_cache() module for memoization**

.. code-block:: python

    import functools

    # Create a simple call counting decorator
    def counter(function):
        function.calls = 0
        @functools.wraps(function)
        def _counter(*args, **kwargs):
            function.calls += 1
            return function(*args, **kwargs)
        return _counter

    # Create a LRU cache with size 3 
    @functools.lru_cache(maxsize=3)
    @counter
    def fibonacci(n):
        if n < 2:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

>>> fibonacci(100)
354224848179261915075

*The LRU cache offers some useful statistics*

>>> fibonacci.cache_info()
CacheInfo(hits=98, misses=101, maxsize=3, currsize=3)

*The result from our counter function which is now wrapped
both by our counter and the cache*

>>> fibonacci.__wrapped__.__wrapped__.calls
101
