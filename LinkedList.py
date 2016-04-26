#!/usr/bin/env python3

from Node import Node

"""
A standard LinkedList implementation, implementing all operations from scratch.
Mutable, Iterable and iterator container.
"""
class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self.__it = self._head
        self.__cnt = 0

    def _add(self, node):
        if self._head == None:
            self._head = node
        if self._tail == None:
            self._tail = self._head
        else:
            self._tail.next = node
            self._tail = node
        self.__cnt += 1

    def add(self, data):
        """
        Adds a new element into the container
        """
        node = Node(data)
        self._add(node)

    def add_node(self, node):
        """
        Adds a preconstructed node to the tail of the list
        """
        if (node == None):
            raise ValueError("New node can't be none")
        self._add(node)

    """
    Performs a lookup from head to tail looking for the node with the specific data on it.
    :returns: pointer to node with the data, and previous node
    :except: if node is not found with the data, raises ValueError
    """
    def _find(self, data):
        prev = None
        node = self._head
        while node != None:
            if (node.data == data):
                return prev, node
            prev = node
            node = node.next
        # Node was not found
        raise ValueError("Element was not found")


    def delete(self, data):
        """
        Deletes the given element.
        :except: ValueError if no node is found with the given data on it
        """
        prev, node = self._find(data)
        # Found head
        if (prev != None):
            prev.next = node.next
        # Found tail
        if node.next == None:
            # move tail
            self._tail = prev
        # Deleting head?
        if node == self._head:
            self._head = node.next
        del node
        self.__cnt -= 1

    def clear(self):
        """
        Deletes all nodes from the list
        """
        while (self._head != None):
            node = self._head
            self._head = self._head.next
            del node
        self._head = None
        self._tail = None

    @property
    def count(self):
        return self.__len__()

    @property
    def tail(self):
        return self._tail

    @property
    def head(self):
        return self._head

    # Set of magic methods supporting the standard pythonic ways of doing it
    def __len__(self):
        return self.__cnt

    def __getitem__(self, data):
        """
        :except: ValueError: no node containing given data could be found
        """
        return self._find(data)

    def __delitem__(self, data):
        """
        :except: ValueError: no node containing given data could be deleted
        """
        self.delete(data)

    def __contains__(self, data):
        """
        Supporting "in" call (is X in list?)
        """
        try:
            self._find(data)
        except ValueError:
            return False
        return True

    def __next__(self):
        """
        This method adds the iterator support (for each i in container x)
        """
        while (self.__it != None):
            node = self.__it
            self.__it = node.next
            return node
        # Re-locate iterator node after we
        self.__it = self._head
        raise StopIteration

    def __iter__(self):
        """
        This method adds "iterable" implementation support
        """
        self.__it = self._head
        return self

    def __str__(self):
        """ Supporting print(LinkedList) """
        node = self._head
        str = ''
        while node != None:
           str += '{} -> '.format(node.data)
           node = node.next
        str += 'None'
        return str


if __name__ == '__main__':
    import unittest

    class testLinkedList(unittest.TestCase):
        def __init__(self, *args, **kwargs):
            super(testLinkedList, self).__init__(*args, **kwargs)
            self._list = LinkedList()

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
        def test_contains(self):
            print("Testing contains")
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
            print("Testing string representation")
            strt = ''
            for i in range(10):
                self._list.add(i)
                strt += '{} -> '.format(i)
            strt += 'None'
            self.assertEqual(str(self._list), strt)

        """
        For anyone not realizing it yet, the next two tests are **utterly** wrong: they're tightly
        coupled to the internal implementation, not to the interface API.
        I'm just testing my internal _find method is right, but in production code this
        should ever pass a code review!
        """
        def test_find_raises(self):
            print("Testing find raises exception ValueError")
            self._list.add(100)
            self._list.add(200)
            self._list.add('aaaa')
            self.assertRaises(ValueError, self._list._find, 'bbbb')

        def test_find_get_nodes(self):
            print("Testing find return the right pointers for data")
            self._list.add(100)
            self._list.add(200)
            self._list.add('aaaa')
            prev, node = self._list._find(200)
            self.assertEqual(prev, self._list._head)
            self.assertEqual(node, self._list._head.next)
            prev, node = self._list._find(100)
            self.assertEqual(prev, None)
            self.assertEqual(node, self._list._head)
            prev, node = self._list._find('aaaa')
            self.assertEqual(prev, self._list._head.next)
            self.assertEqual(node, self._list._tail)


    # Setup testSuite and run the tests
    suite = unittest.TestSuite()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(testLinkedList)
    unittest.TextTestRunner().run(suite)
