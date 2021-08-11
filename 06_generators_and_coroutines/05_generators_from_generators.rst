Generating from generators
###########################

Example 1
---------

**Basic usage**

.. code-block:: python

    import itertools

    def powerset(sequence):
        for size in range(len(sequence) + 1):
            for item in itertools.combinations(sequence, size):
                yield item

>>> for result in powerset('abc'):
...     print(result)
()
('a',)
('b',)
('c',)
('a', 'b')
('a', 'c')
('b', 'c')
('a', 'b', 'c')

Example 2
---------

**Using the 'yield from' statement**

.. code-block:: python

    import itertools

    def powerset(sequence):
        for size in range(len(sequence) + 1):
            # Replace inner for loop with 'yield from'
            yield from itertools.combinations(sequence, size)

>>> for result in powerset('abc'):
...     print(result)
()
('a',)
('b',)
('c',)
('a', 'b')
('a', 'c')
('b', 'c')
('a', 'b', 'c')

Example 3
---------

**Using generators to print a nested data structure
recursively**

.. code-block:: python

    def flatten(sequence):
        for item in sequence:
            # Using a try/except block for demostration purposes
            try:
                yield from flatten(item)
            except TypeError:
                yield item

>>> list(flatten([1, [2, [3, [4, 5], 6], 7], 8]))
[1, 2, 3, 4, 5, 6, 7, 8]
