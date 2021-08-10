Context Managers
#################

Example 1
---------

**Creating a custom context manager for open()**

.. code-block:: python

    import contextlib

    @contextlib.contextmanager
    def open_context_manager(filename, mode='r'):
        fh = open(filename, mode)
        yield fh
        fh.close()


>>> with open_context_manager('test.txt', 'w') as fh:
...     print('Our test is complete!', file=fh)

Example 2
---------

**Using contextlib.closing() instead of a context manager**

>>> import contextlib

>>> with contextlib.closing(open('test.txt', 'a')) as fh:
...     print('Yet another test', file=fh)


Example 3
---------

**Using contextlib.contextmanager() to create decorators**

.. code-block:: python

    import contextlib

    @contextlib.contextmanager
    def debug(name):
        print('Debugging {}:'.format(name))
        yield
        print('End of debugging {}'.format(name))


    @debug('spam')
    def spam():
        print('This is the inside of our spam function')

>>> spam()
Debugging 'spam':
This is the inside of our spam function
End of debugging 'spam'
