@property
###########

Example 1
---------

**Basic usage - 2 methods**

.. code-block:: python

    class Spam(object):

        # Method 1

        def get_eggs(self):
            print('getting eggs')
            return self._eggs

        def set_eggs(self, eggs):
            print('setting eggs to {}'.format(eggs))
            self._eggs = eggs

        def delete_eggs(self):
            print('deleting eggs')
            del self._eggs

        eggs = property(get_eggs, set_eggs, delete_eggs)

        # Method 2

        @property
        def spam(self):
            print('getting spam')
            return self._spam

        @spam.setter
        def spam(self, spam):
            print('setting spam to {}'.format(spam))
            self._spam = spam

        @spam.deleter
        def spam(self):
            print('deleting spam')
            del self._spam

>>> spam = Spam()

>>> spam.eggs = 123
setting eggs to 123
>>> spam.eggs
getting eggs
123
>>> del spam.eggs
deleting eggs

>>> spam.spam = 456
setting spam to 456
>>> spam.spam
getting spam
123
>>> del spam.spam
deleting spam

Example 2
----------

**Custom implementation of @property**

.. code-block:: python

    class Property(object):
        def __init__(self, fget=None, fset=None, fdel=None, doc=None):
            self.fget = fget
            self.fset = fset
            self.fdel = fdel
            # If no specific documentation is available, copy it
            # from the getter
            if fget and not doc:
                doc = fget.__doc__
            self.__doc__ = doc

        def __get__(self, instance, cls):
            if instance is None:
                # Redirect class (not instance) properties to
                # self
                return self
            elif self.fget:
                return self.fget(instance)
            else:
                raise AttributeError('unreadable attribute')

        def __set__(self, instance, value):
            if self.fset:
                self.fset(instance, value)
            else:
                raise AttributeError("can't set attribute")

        def __delete__(self, instance):
            if self.fdel:
                self.fdel(instance)
            else:
                raise AttributeError("can't delete attribute")

        def getter(self, fget):
            return type(self)(fget, self.fset, self.fdel)

        def setter(self, fset):
            return type(self)(self.fget, fset, self.fdel)

        def deleter(self, fdel):
            return type(self)(self.fget, self.fset, fdel)

Example 3
---------
            
**A more generic implementation of @property using dicts**

.. code-block:: python

    class Spam(object):
        def __init__(self):
            self.registry = {}
        def __getattr__(self, key):
            print('Getting {}'.format(key))
            return self.registry.get(key, 'Undefined')
        def __setattr__(self, key, value):
            if key == 'registry':
                object.__setattr__(self, key, value)
            else:
                print('Setting {} to {}'.format((key, value)))
                self.registry[key] = value
        def __delattr__(self, key):
            print('Deleting {}'.format(key))
            del self.registry[key]

>>> spam = Spam()

>>> spam.a
Getting 'a'
'Undefined'

>>> spam.a = 1
Setting 'a' to 1

>>> spam.a
Getting 'a'
1

>>> del spam.a
Deleting 'a'
