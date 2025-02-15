Functools - reduce()
######################

Example 1
---------

**Create a nested tree using defaultdict**

.. code-block:: python

    import json
    import functools
    import collections

    def tree():
        return collections.defaultdict(tree)

    # Build the tree:
    taxonomy = tree()
    reptilia = taxonomy['Chordata']['Vertebrata']['Reptilia']
    reptilia['Squamata']['Serpentes']['Pythonidae'] = [
        'Liasis', 'Morelia', 'Python']

**The actual contents of the tree**

>>> print(json.dumps(taxonomy, indent=4))
{
    "Chordata": {
        "Vertebrata": {
            "Reptilia": {
                "Squamata": {
                    "Serpentes": {
                        "Pythonidae": [
                            "Liasis",
                            "Morelia",
                            "Python",
                        ]
                    }
                }
            }
        }
    }
}

**Get the suborder**

.. code-block:: python

    # The path we wish to get
    path = 'Chordata.Vertebrata.Reptilia.Squamata'.split('.')

    # Fetch the path using reduce to recursively fetch the items
    suborder = functools.reduce(lambda a, b: a[b], path, taxonomy)

>>> suborder.keys()
dict_keys(['Serpentes'])

**Get the family**

.. code-block:: python

    # The path we wish to get
    path = 'Chordata.Vertebrata.Reptilia.Squamata.Serpentes'.split('.')

    # Fetch the path using reduce to recursively fetch the items
    family = functools.reduce(lambda a, b: a[b], path, taxonomy)

>>> family.items()
dict_items([('Pythonidae', ['Liasis', 'Morelia', 'Python'])])

Example 2
---------

**Using reduce inside lambda functions**

.. code-block:: python

    fold_left = lambda iterable, initializer=None: functools.reduce(
        lambda x, y: function(x, y),
        iterable,
        initializer,
        )

    fold_right = lambda iterable, initializer=None: functools.reduce(
        lambda x, y: function(y, x),
        reversed(iterable),
        initializer,
        )
