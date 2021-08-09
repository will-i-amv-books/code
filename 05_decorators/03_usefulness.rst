Usefulness of Decorators
#########################

Example 1
---------

**Original Code without decorators**

.. code-block:: python

    def spam(eggs):
        return 'spam' * (eggs % 5)

>>> output = spam(3)

**Debugging code using print statements 
(not recommended)**

.. code-block:: python

    def spam(eggs):
        output = 'spam' * (eggs % 5)
        print('spam({}): {}'.format(eggs, output))
        return output

>>> output = spam(3)
spam(3): 'spamspamspam'


**Debugging code using a debug decorator
(recommended)**

.. code-block:: python

    import functools

    def debug(function):
        @functools.wraps(function)
        def _debug(*args, **kwargs):
            output = function(*args, **kwargs)
            print('{}({}, {}): {}'.format(
                function.__name__, args, kwargs, output))
            return output
        return _debug

    @debug
    def spam(eggs):
        return 'spam' * (eggs % 5)

>>> output = spam(3)
spam((3,), {}): 'spamspamspam'
