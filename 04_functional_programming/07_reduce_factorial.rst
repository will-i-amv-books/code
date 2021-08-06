Functools - reduce()
######################

Example 1
---------

**Using reduce() to calculate a factorial with operator.mul**

.. code-block:: python

    import operator
    import functools

    factorial = functools.reduce(operator.mul, range(1, 6))

>>> factorial
120

**Using reduce() to calculate a factorial with lambda (slower)**

.. code-block:: python

    import functools

    factorial = functools.reduce(lambda a, b: a * b, range(1, 6))

>>> factorial
120

Example 2
---------

**Implementing reduce() using operator.mul**

.. code-block:: python

    import operator

    f = operator.mul
    factorial = f(f(f(f(1, 2), 3), 4), 5)

>>> factorial
120

**Step-by-step execution**

.. code-block:: python

    import operator

    iterable = range(1, 6)

    # The initial values:
    a, b, *iterable = iterable
    
    # First run
    a = operator.mul(a, b)
    b, *iterable = iterable
    
    # Second run
    a = operator.mul(a, b)
    b, *iterable = iterable
    
    # Third run
    a = operator.mul(a, b)
    b, *iterable = iterable
    
    # Fourth and last run
    a = operator.mul (a, b)
    
>>> a
120

Example 3
---------

**Implementing reduce() using the deque collection**

.. code-block:: python

    import operator
    import collections
    iterable = collections.deque(range(1, 6))

    value = iterable.popleft()
    while iterable:
        value = operator.mul(value, iterable.popleft())

>>> value
120

