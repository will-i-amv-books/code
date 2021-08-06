Itertools - combinations()
###########################

Example 1
---------

**Basic usage**

.. code-block:: python

    import itertools

    comb = list(itertools.combinations(range(3), 2))

>>> comb
[(0, 1), (0, 2), (1, 2)]

Example 2
---------

**Combinations with replacement**

.. code-block:: python

    import itertools

    comb_with_repl = list(itertools.combinations_with_replacement(range(3), 2))

>>> comb_with_repl
[(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]

Example 3
---------

**Implement a powerset with combinations and chain**

.. code-block:: python

    import itertools

    def calc_powerset(iterable):
        return itertools.chain.from_iterable(
            itertools.combinations(iterable, i)
            for i in range(len(iterable) + 1))

    powerSet = list(calc_powerset(range(3)))

>>> powerSet
[(), (0,), (1,), (2,), (0, 1), (0, 2), (1, 2), (0, 1, 2)]
