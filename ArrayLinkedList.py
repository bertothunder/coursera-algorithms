#!/usr/bin/env python3

''' Node is the basic node structure to use in the linked list '''

class Node(object):
    def __init__(self, data=None):
        self._data = data
        self.__next = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data=None):
        self._data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next=None):
        self.__next = next

    def __cmp__(self, other):
        # Magic method for comparison
        return self._data == other.data

    def __str__(self):
        return self._data


"""
The Array-based LinkedList implementation.
Mutable, Iterable and Iterator container.
"""
class ArrayLinkedList(object):
    def __init__(self, size=0):
        self._data = []

    def _add(self, node):
        if (len(self._data) != 0):
            self._data[-1].next = node
        self._data.append(node)
        self.__tail = node

    def add(self, data):
        """
        Adds a new element into the container
        """
        node = Node(data)
        self._add(node)

    def add_node(self, node):
        """
        Adds a new node element to the list (on the tail)
        """
        self._add(node)

    def clear(self):
        self._data.clear()

    def _find(self, data):
        idx = 0
        for node in self._data:
            if (node.data == data):
                return node, idx
            idx += 1
        raise IndexError("Node was not found in the list")

    def delete(self, data):
        """
        Deletes the given element
        """
        node, index = self._find(data)
        if (index > 0):
            self._data[index-1].next = self._data[index].next
        self._data.remove(node)

    @property
    def count(self):
        return len(self._data)

    @property
    def tail(self):
        return self._data[-1]

    @property
    def head (self):
        return self._data[0]

    # Set of magic methods supporting the standard pythonic ways of doing it
    def __len__(self):
        return len(self._data)

    def __getitem__(self, data):
        return self._data[data]

    def __delitem__(self, data):
        self.delete(data)

    def __iter__(self):
        """
        This method adds "iterable" implementation support
        """
        # iter(data) should not be necessary, since data is iterable itself!
        return iter(self._data)

    def __contains__(self, data):
        """
        Supporting "in" call
        """
        try:
            self._find(data)
        except IndexError:
            return False
        return True

    def __next__(self):
        """
        This method adds the iterator support (for i in x)
        """
        for node in self._data:
            return node
        raise StopIteration

    def __str__(self):
        """ Supporting print(LinkedList) """
        str = ''
        for node in self._data:
           str += '{} -> '.format(node.data)
        str += 'None'
        return str


if __name__ == '__main__':
    import unittest

    class testArrayLinkedList(unittest.TestCase):
        def __init__(self, *args, **kwargs):
            super(testArrayLinkedList, self).__init__(*args, **kwargs)
            self._list = ArrayLinkedList()

        def setUp(self):
            self._list.clear()

        # Add capabilities
        def test_add(self):
            print("Testing add()")
            self._list.add('aaaa')
            self._list.add(123)
            self._list.add(float(123.4))
            self._list.add(list())
            self._list.add(set())
            self.assertEqual(len(self._list), 5)

        def test_count_len(self):
            print("Testing length")
            self._list.add('1234')
            self._list.add('3230')
            self.assertEqual(len(self._list), 2)
            self.assertEqual(self._list.count, 2)
            self._list.add('8080')
            self._list.add('300')
            self.assertEqual(len(self._list), 4)
            self.assertEqual(self._list.count, 4)
            # Delete nodes
            self._list.delete('3230')
            self._list.delete('8080')
            self._list.delete('1234')
            self.assertEqual(len(self._list), 1)
            self.assertEqual(self._list.count, 1)

        # Positioning -> head
        def test_head(self):
            print("Testing positioning -> head")
            self._list.add(1234)
            self._list.add(2345)
            head = self._list.head
            self.assertNotEqual(head, None)
            self.assertEqual(head.next, self._list.tail)
            self.assertEqual(head.data, 1234)


        # Positioning -> tail
        def test_tail(self):
            print("Testing positioning -> tail")
            self._list.add(1234)
            self._list.add(2345)
            tail = self._list.tail
            self.assertNotEqual(tail, None)
            self.assertEqual(tail.next, None)
            self.assertEqual(tail.data, 2345)


        # Positioning -> head == tail
        def test_head_and_tail(self):
            print("Testing unique node list")
            self._list.add(1234)
            self.assertEqual(self._list.head, self._list.tail)

        # Traversing
        def test_iterator(self):
            print("Testing iteration")
            for i in range(100):
                self._list.add(i)
            i = 0
            for node in self._list:
                self.assertEqual(node.data, i)
                i += 1

        # It fails, check out why!
        # Test contains idiom
        def test_find(self):
            node1 = Node(300)
            node2 = Node(1345)
            node3 = Node('aaaaa')
            self._list.add_node(node1)
            self._list.add_node(node3)
            self._list.add_node(node2)
            self.assertEqual(300 in self._list, True)
            self.assertEqual(2000 in self._list, False)
            self.assertEqual('aaaaa' in self._list, True)

        # Test string output
        def test_string(self):
            strt = ''
            for i in range(10):
                self._list.add(i)
                strt += '{} -> '.format(i)
            strt += 'None'
            self.assertEqual(str(self._list), strt)

    # Setup testSuite and run the tests
    suite = unittest.TestSuite()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(testArrayLinkedList)
    unittest.TextTestRunner().run(suite)
