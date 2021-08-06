Itertools - permutations()
#########################

Example 1
---------

**Basic usage**

.. code-block:: python

    import itertools
    perms = list(itertools.permutations(range(3), 2))

>>> perms
[(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]

**Comparison with combinations**

.. code-block:: python

    import itertools
    combs = list(itertools.combinations(range(3), 2))

>>> combs
[(0, 1), (0, 2), (1, 2)]