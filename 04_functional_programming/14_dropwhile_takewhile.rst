Itertools - dropwhile()/takewhile()
####################################

Example 1
---------

**Basic usage of dropwhile**

.. code-block:: python

    import itertools

    lastItems = list(itertools.dropwhile(
        lambda x: x <= 3, 
        [1, 3, 5, 4, 2]))

>>> lastItems
[5, 4, 2] 

Example 2
---------

**Basic usage of takewhile**

.. code-block:: python

    import itertools
    
    firstItems = list(itertools.takewhile(
        lambda x: x <= 3, 
        [1, 3, 5, 4, 2]))

>>> firstItems
[1, 3]
