Itertools - islice()
#########################

Example 1
---------

**Basic usage**

.. code-block:: python

    from itertools import islice, count

    items2to6 = list(islice(count(), 2, 7))

>>> items2to6
[2, 3, 4, 5, 6]

Example 2
----------

**Incorrect implementation 
(generators can't be sliced like lists)**

>>> from itertools import islice, count
>>> count()[:10]
Traceback (most recent call last):
...
TypeError: 'itertools.count' object is not subscriptable


>>> from itertools import islice, count
>>> len(count()[:10])
Traceback (most recent call last):
...
TypeError: 'itertools.count' object is not subscriptable

**Correct implementation**

.. code-block:: python

    from itertools import islice, count

    first10 = list(islice(count(), 10))

>>> first10
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> len(first10)
10