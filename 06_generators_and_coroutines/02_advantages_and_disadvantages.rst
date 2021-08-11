Lazy evaluation of generators
##############################

Example 1
---------

**Example of lazy execution of a generator**

.. code-block:: python

    def generator():
        print('Before 1')
        yield 1
        print('After 1')
        print('Before 2')
        yield 2
        print('After 2')
        print('Before 3')
        yield 3
        print('After 3')

>>> g = generator()
>>> print('Got {}'.format(next(g)))
Before 1
Got 1

>>> print('Got {}'.format(next(g)))
After 1
Before 2
Got 2
