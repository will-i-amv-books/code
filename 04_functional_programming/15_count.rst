Itertools - count()
####################

Example 1
---------

**Except for being infinite, the standard version returns the same
results as the range function does.**

.. code-block:: python

    items = [
        (a, b)
        for a, b in zip(range(3), itertools.count())]

>>> items
[(0, 0), (1, 1), (2, 2)]


**With a different starting point the results are still the same**

.. code-block:: python

    items = [
        (a, b)
        for a, b in zip(range(5, 8), itertools.count(5))]

>>> items
[(5, 5), (6, 6), (7, 7)]

**And a different step works the same as well**

.. code-block:: python

    items = [
        (a, b)
        for a, b in zip(range(5, 10, 2), itertools.count(5, 2))]

>>> items
[(5, 5), (7, 7), (9, 9)]

**Unless you try to use floating point numbers**

>>> range(5, 10, 0.5)
Traceback (most recent call last):
    ...
TypeError: 'float' object cannot be interpreted as an integer

**Which does work for count**

.. code-block:: python

    items = [
        (a, b)
        for a, b in zip(range(5, 10), itertools.count(5, 0.5))]

>>> items
[(5, 5), (6, 5.5), (7, 6.0), (8, 6.5), (9, 7.0)]
