Itertools - compress()
#######################

Example 1
---------

**Basic usage (no duplicates)**

.. code-block:: python

    import itertools

    compressed = list(itertools.compress(
        range(1000), 
        [0, 1, 1, 1, 0, 1]))

>>> compressed
[1, 2, 3, 5]
