Lambda functions
####################

Example 1
---------

**Basic usage (no duplicates)**

.. code-block:: python

    class Spam(object):
        def __init__(self, value):
            self.value = value
        def __repr__(self):
            return '<{}: {}>'.format(self.__class__.__name__, self.value)

**Sorting using a lambda function**
>>> spams = [Spam(5), Spam(2), Spam(4), Spam(1)]
>>> sorted_spams = sorted(spams, key=lambda spam: spam.value)

**Sorting using a named function**

.. code-block:: python

    def key_function(spam):
        return spam.value

>>> spams = [Spam(5), Spam(2), Spam(4), Spam(1)]
>>> sorted_spams = sorted(spams, key=key_function)

>>> spams
[<Spam: 5>, <Spam: 2>, <Spam: 4>, <Spam: 1>]
>>> sorted_spams
[<Spam: 1>, <Spam: 2>, <Spam: 4>, <Spam: 5>]

Example 2
---------

**Bad practices**

*Don't define a named function as one-liner*
>>> def key(spam): return spam.value

*Don't use a lambda function with a variable,
use it as anonymous argument to another function*
>>> key = lambda spam: spam.value

