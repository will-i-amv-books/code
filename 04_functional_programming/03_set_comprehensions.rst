Set comprehensions
####################

Example 1
---------

**Basic usage (no duplicates)**

.. code-block:: python

    results = {
        x*y 
        for x in range(3) for y in range(3)}

>>>results
{0, 1, 2, 4}

**Comparison with list comprehensions (duplicates)**

.. code-block:: python

    results = [
        x*y 
        for x in range(3) for y in range(3)]

>>>results
[0, 0, 0, 0, 1, 2, 0, 2, 4]

