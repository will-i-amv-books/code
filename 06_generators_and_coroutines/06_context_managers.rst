Creating context managers with generators
##########################################

Example 1
---------

**Using generators to implement a context manager**

.. code-block:: python

    import datetime
    import contextlib

    # Context manager that shows how long a context was active
    @contextlib.contextmanager
    def timer(name):
        start_time = datetime.datetime.now()
        yield
        stop_time = datetime.datetime.now()
        print('{} took {}'.format((name, stop_time - start_time)))

    # The write to log function writes all stdout (regular print data) to
    # a file. The contextlib.redirect_stdout context wrapper
    # temporarily redirects standard output to a given file handle, in
    # this case the file we just opened for writing.
    @contextlib.contextmanager
    def write_to_log(name):
        with open('{}.txt'.format(name, 'w')) as fh:
            with contextlib.redirect_stdout(fh):
                with timer(name):
                    yield

    # Use the context manager as a decorator
    @write_to_log('some_function')
    def some_function():
        print('This function takes a bit of time to execute')
        print('Do more...')

>>> some_function()

Example 2
---------

**Using contextlib.ExitStack() to combine multiple context managers**

.. code-block:: python

    import contextlib
    import datetime


    # Context manager that shows how long a context was active
    @contextlib.contextmanager
    def timer(name):
        start_time = datetime.datetime.now()
        yield
        stop_time = datetime.datetime.now()
        print('{} took {}'.format((name, stop_time - start_time)))

    @contextlib.contextmanager
    def write_to_log(name):
        with contextlib.ExitStack() as stack:
            fh = stack.enter_context(open('stdout.txt', 'w'))
            stack.enter_context(contextlib.redirect_stdout(fh))
            stack.enter_context(timer(name))
            yield

    @write_to_log('some_function')
    def some_function():
        print('This function takes a bit of time to execute')
        print('Do more...')

>>> some_function()

Example 3
---------

**Using contextlib.ExitStack() to to transfer the contexts 
to a new ExitStack and manually handle the closing**

.. code-block:: python

    import contextlib


    with contextlib.ExitStack() as stack:
        spam_fh = stack.enter_context(open('spam.txt', 'w'))
        eggs_fh = stack.enter_context(open('eggs.txt', 'w'))
        spam_bytes_written = spam_fh.write('writing to spam')
        eggs_bytes_written = eggs_fh.write('writing to eggs')
        # Move the contexts to a new ExitStack and store the
        # close method
        close_handlers = stack.pop_all().close

>>> spam_bytes_written = spam_fh.write('still writing to spam')
>>> eggs_bytes_written = eggs_fh.write('still writing to eggs')

*After closing we can't write anymore*

>>> close_handlers()
>>> spam_bytes_written = spam_fh.write('cant write anymore')
Traceback (most recent call last):
...
ValueError: I/O operation on closed file.
