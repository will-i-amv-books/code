List comprehensions
####################

Example 1
---------

**Basic usage**

.. code-block:: python

    squares = [
        x ** 2 
        for x in range(10)]

>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

Example 2
---------

**List comprehensions with filters**

.. code-block:: python
    
    uneven_squares = [
        x ** 2 
        for x in range(10) 
        if x % 2]

>>> uneven_squares
[1, 9, 25, 49, 81]

**Equivalent for loop**

.. code-block:: python

    uneven_squares = []
    for x in range(10):
        if x % 2:
            uneven_squares.append(x ** 2)

>>> uneven_squares
[1, 9, 25, 49, 81]

Example 3
---------

**Flawed list comp implementation**

.. code-block:: python

    import random

    numbers = [
        random.random() 
        for _ in range(10) 
        if random.random() >= 0.5] # doctest: +SKIP

>>> numbers
[0.5211948104577864, 0.650010512129705, 0.021427316545174158] #(1)

*The last element is minor than 0.5 
because the first and last random calls are actually 
separate calls and return different results (1)*

**Correct implementation**

.. code-block:: python

    import random

    numbers = [
        random.random() 
        for _ in range(10)] # doctest: +SKIP

    filteredNumbers = [
        x 
        for x in numbers 
        if x >= 0.5] # doctest: +SKIP

>>> filteredNumbers
[0.715510247827078, 0.8426277505519564, 0.5071133900377911]

Example 4
---------

**Nested list comp**

.. code-block:: python

    import random

    numbers = [
        x 
        for x in [
            random.random() 
            for _ in range(10)] 
        if x >= 0.5] # doctest: +SKIP

**Incomprehensible list comp**

.. code-block:: python

    import random

    numbers = [
        x for _ in range(10) 
        for x in [random.random()] 
        if x >= 0.5] # doctest: +SKIP

Example 5
---------

**2-variable list comp**

.. code-block:: python

    import random

    numbers = [
        (x, y) 
        for x in range(3) for y in range(3, 5)]

>>> numbers
[(0, 3), (0, 4), (1, 3), (1, 4), (2, 3), (2, 4)]

**Equivalent for loop**

.. code-block:: python

    results = []
    for x in range(3):
        for y in range(3, 5):
            results.append((x, y))

>>> results
[(0, 3), (0, 4), (1, 3), (1, 4), (2, 3), (2, 4)]

Example 6
---------

**List comp with multiple nesting (not recommended)**

.. code-block:: python

    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]

    temp_list = [
        y 
        for x in matrix for y in x
    ]
    reshaped_matrix = [
        [
            temp_list[i * len(matrix) + j]
            for j in range(len(matrix))
        ]
        for i in range(len(matrix[0]))
    ]

>>> import pprint
>>> pprint.pprint(reshaped_matrix, width=40)
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9],
 [10, 11, 12]]

