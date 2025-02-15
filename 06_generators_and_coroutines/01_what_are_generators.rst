What are generators
####################

Example 1
---------

**A basic counter with a generator function**

.. code-block:: python

    def count(start=0, step=1, stop=10):
        n = start
        while n <= stop:
            yield n
            n += step

>>> for x in count(10, 2.5, 20):
...     print(x)
10
12.5
15.0
17.5
20.0

Example 2
---------

**Comparing yield and return statements**

.. code-block:: python

    def generator():
        yield 'this is a generator'
        return 'returning from a generator'

>>> g = generator()
>>> next(g)
'this is a generator'
>>> next(g)
Traceback (most recent call last):
...
StopIteration: returning from a generator

Example 3
---------

**Generator comprehensions**

.. code-block:: python

    generator = (x ** 2 for x in range(4))

>>> for x in generator:
...     print(x)
0
1
4
9

------------------------------------------------------------------------------

Example 3
---------

**A basic counter with a generator class**

.. code-block:: python

    class Count(object):
        def __init__(self, start=0, step=1, stop=10):
            self.n = start
            self.step = step
            self.stop = stop

        def __iter__(self):
            return self

        def __next__(self):
            n = self.n
            if n > self.stop:
                raise StopIteration()
            self.n += self.step
            return n

>>> for x in Count(10, 2.5, 20):
...     print(x)
10
12.5
15.0
17.5
20.0
