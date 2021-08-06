The Y combinator
#################

Example 1
---------

**Definition - Lambda version**

.. code-block:: python

    Y = lambda f: lambda *args: f(Y(f))(*args)

**Definition - Named version**

.. code-block:: python

    def Y(f):
        def y(*args):
            y_function = f(Y(f))
            return y_function(*args)
    return y

Example 2
---------

**Factorial of a number - Named version**

.. code-block:: python

    Y = lambda f: lambda *args: f(Y(f))(*args)

    def factorial(combinator):
        def _factorial(n):
            if n:
                return n * combinator(n - 1)
            else:
                return 1
        return _factorial

>>> Y(factorial)(5)
120

**Factorial of a number - Lambda version**

.. code-block:: python

    Y = lambda f: lambda *args: f(Y(f))(*args)

>>> Y(lambda c: lambda n: n and n * c(n - 1) or 1)(5)
120

>>> Y(lambda c: lambda n: n * c(n - 1) if n else 1)(5)
120

Example 3
---------

**Quicksort using Y combinator**

.. code-block:: python

    Y = lambda f: lambda *args: f(Y(f))(*args)

    quicksort = Y(
        lambda f: lambda x: (
            f([item for item in x if item < x[0]]) +
            [y for y in x if x[0] == y] +
            f([item for item in x if item > x[0]])
        ) if x else [])

>>> quicksort([1, 3, 5, 4, 1, 3, 2])
[1, 1, 2, 3, 3, 4, 5]
