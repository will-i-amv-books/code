Itertools - groupby()
#######################

Example 1
---------

.. code-block:: python

    from itertools import groupby
    tuples = [('a', 1), ('b', 0), ('b', 2), ('c', 3), ('a', 2)]

**Group items by the first element**

.. code-block:: python

    sortedTuples = sorted(tuples, key=lambda x: x[0])

    groupedByLetter = {
        group:[val for key, val in items]
        for group, items in groupby(sortedTuples, lambda x: x[0])}

>>> groupedByLetter
{'a': [1, 2], 'b': [2, 0], 'c': [3]}

**Group items by the second element**

.. code-block:: python

    sortedTuples = sorted(tuples, key=lambda x: x[1])

    groupedByNumber = {
        group:[key for key, val in items]
        for group, items in groupby(sortedTuples, lambda x: x[1])}

>>> groupedByNumber
{0: ['b'], 1: ['a'], 2: ['b', 'a'], 3: ['c']}


Example 2
---------

**Flawed implementation (list should be sorted before grouped)**

.. code-block:: python

    from itertools import groupby
    tuples = [('a', 1), ('c', 3), ('b', 2), ('a', 2), ('b', 0)]

    groupedByLetter = {
        group:[val for key, val in items]
        for group, items in groupby(tuples, lambda x: x[0])}

>>> groupedByLetter
{'a': [2], 'c': [3], 'b': [0, 2]}

**Correct implementation (list sorted by the grouping key)**

.. code-block:: python

    from itertools import groupby
    tuples = [('a', 1), ('c', 3), ('b', 2), ('a', 2), ('b', 0)]

    ###
    sortedTuples = sorted(tuples, key=lambda x: x[0])
    ###

    groupedByLetter = {
        group:[val for key, val in items]
        for group, items in groupby(sortedTuples, lambda x: x[0])}

>>> groupedByLetter
{'a': [1, 2], 'b': [2, 0], 'c': [3]}
