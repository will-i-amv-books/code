Itertools - chain()
#########################

Example 1
---------

**Basic usage**

.. code-block:: python

    import itertools

    a = range(3)
    b = range(5)
    concat = list(itertools.chain(a, b))

>>> concat
[0, 1, 2, 0, 1, 2, 3, 4]

Example 2
---------

**Chain an iterable containing iterables**

.. code-block:: python

    import itertools

    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    vector = list(itertools.chain.from_iterable(matrix))

>>> vector
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
