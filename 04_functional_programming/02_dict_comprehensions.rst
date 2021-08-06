Dict comprehensions
####################

Example 1
---------

**Basic usage**

.. code-block:: python

    result = {
        x: x ** 2 
        for x in range(10)}

>>> result
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

**Dict comprehensions with filters**

.. code-block:: python

    filteredResult = {
        x: x ** 2 
        for x in range(10) 
        if x % 2}

>>> filteredResult
{1: 1, 3: 9, 9: 81, 5: 25, 7: 49}

Example 2
---------

**Mixing dict and list comprehensions**

.. code-block:: python

    result = {
        x ** 2: [y for y in range(x)] 
        for x in range(5)}

>>> result
{0: [], 1: [0], 4: [0, 1], 16: [0, 1, 2, 3], 9: [0, 1, 2]}

