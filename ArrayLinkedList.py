#!/usr/bin/env python3


"""
The Array-based LinkedList implementation.
Mutable, Iterable and Iterator container.
"""
class ArrayLinkedList(object):
    def __init__(self, size=0):
        self.__size = size
        self.__data = []

    def add(self, data):
        """
        Adds a new element into the container
        """
        node = Node(data)
        self.__data[-1].next = node
        self.__data.append(node)
        self.__tail = node

    def delete(self, data):
        """
        Deletes the given element
        """
        try:
            self.__data.remove(data)
        except ValueError:
            # Convert into a IndexError
            raise IndexError("Element was not found")
        finally:
            self.__data[-1].next = None

    @property
    def count(self):
        return len(self.__data)

    @property
    def tail(self):
        return self.__data[-1]

    @property
    def head (self):
        return self.__data[0]

    # Set of magic methods supporting the standard pythonic ways of doing it
    def __len__(self):
        return len(self.__data)

    def __getitem__(self, data):
        return self.__data[data]

    def __delitem__(self, data):
        self.delete(data)

    def __iter__(self):
        """
        This method adds "iterable" implementation support
        """
        # iter(data) should not be necessary, since data is iterable itself!
        return iter(data)

    #def __reversed__(self):
    #    """
    #    Supporting reversed() call
    #    """
    # Tricky one! the internal array supports reversion, but the single linked list
    # should not support it (next() only goes forward, never back, that needs a
    # double linked list!). So this should not be present
    #    return iter(data.reversed())

    def __contains__(self, data):
        """
        Supporting "in" call
        """
        try:
            self.__data.index(data)
        except ValueError:
            return False
        return True

    def __next__(self):
        """
        This method adds the iterator support (for i in x)
        """
        for i in self.__data:
            yield i
        raise StopIteration


