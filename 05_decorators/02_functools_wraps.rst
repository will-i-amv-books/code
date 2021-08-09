functools.wraps()
##################

Example 1
---------

**Incorrect decorator definition 
(not using functools.wraps)**

.. code-block:: python

    def eggs(function):
        def _eggs(*args, **kwargs):
            return function(*args, **kwargs)
        return _eggs

    @eggs
    def spam(a, b, c):
        '''The spam function Returns a * b + c'''
        return a * b + c

>>> help(spam)
Help on function _eggs in module :
<BLANKLINE>
_eggs(*args, **kwargs)
<BLANKLINE>

>>> spam.__name__
'_eggs'

Example 2
---------

**Correct decorator definition 
(using functools.wraps)**

.. code-block:: python

    import functools


    def eggs(function):
        @functools.wraps(function)
        def _eggs(*args, **kwargs):
            return function(*args, **kwargs)
        return _eggs

    @eggs
    def spam(a, b, c):
        '''The spam function Returns a * b + c'''
        return a * b + c


>>> help(spam)
Help on function spam in module ...:
<BLANKLINE>
spam(a, b, c)
    The spam function Returns a * b + c
<BLANKLINE>

>>> spam.__name__
'spam'
