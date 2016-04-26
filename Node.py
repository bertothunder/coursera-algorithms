''' Node is the basic node structure to use in the linked list '''
__author__ = "Alberto Curro - bertothunder"
__version__ = "1.0"
__status__ = "No automation tests"
__license__ = "AGPL"

class Node(object):
    def __init__(self, data=None):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data=None):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next=None):
        self.__next = next

    def __cmp__(self, other):
        # Magic method for comparison
        return self.__data == other.data

    def __str__(self):
        return self.__data
