Decorators using classes
#########################

Example 1
---------

**Basic Usage**

.. code-block:: python

    import functools

    class Debug(object):

        def __init__(self, function):
            self.function = function
            # functools.wraps for classes
            functools.update_wrapper(self, function)

        def __call__(self, *args, **kwargs):
            output = self.function(*args, **kwargs)
            print('{}({}, {}): {}'.format(
                self.function.__name__, args, kwargs, output))
            return output

    @Debug
    def spam(eggs):
        return 'spam' * (eggs % 5)

>>> output = spam(3)
spam((3,), {}): 'spamspamspam'
