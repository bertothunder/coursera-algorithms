#!/usr/bin/env python3

from Node import Node

"""
A standard LinkedList implementation, implementing all operations from scratch.
Mutable, Iterable and iterator container.
"""
__author__ = "Alberto Curro - bertothunder"
__version__ = "1.0"
__status__ = "Tested"
__license__ = "AGPL"

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._it = self._head
        self._cnt = 0

    def add(self, data):
        """
        Adds a new element into the container
        :param: data: either the data to be added (a new node is created and added to the LinkedList), or the new node directly.
        """
        if (isinstance(data, Node)):
            print("Adding node directly")
            self._add(data)
        else:
            node = Node(data)
            self._add(node)

    def delete(self, data):
        """
        Deletes the given element.
        :except: ValueError if no node is found with the given data on it
        """
        prev, node = self._find(data)
        self._del(node, prev)

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

    """" Internal implementation for adding a node """
    def _add(self, node):
        if self._head == None:
            self._head = node
        if self._tail == None:
            self._tail = self._head
        else:
            self._tail.next = node
            self._tail = node
        self._cnt += 1

    """ Internal implementation for deleting a node """
    def _del(self, node, prev=None):
        # Using head
        if (prev != None):
            prev.next = node.next
        # Using tail
        if node.next == None:
            # move tail
            self._tail = prev
        # Deleting head?
        if node == self._head:
            self._head = node.next
        del node
        self._cnt -= 1

    def _find(self, data):
        """
        Performs a lookup from head to tail looking for the node with the specific data on it.
        :returns: pointer to node with the data, and previous node
        :except: if node is not found with the data, raises ValueError
        """
        prev = None
        node = self._head
        while node != None:
            if (node.data == data):
                return prev, node
            prev = node
            node = node.next
        # Node was not found
        raise ValueError("Element was not found")

    def _find_by_index(self, index):
        """
        Finds a node by index
        :param: index: index node
        :returns: the node by the given index
        :except: IndexError if the index is beyond length or negative
        """
        if index > self._cnt or index < 0:
            raise IndexError("Out of index")
        idx = 0
        node = self._head
        while idx != index:
            node = node.next
            idx += 1
        return node

    # Set of magic methods supporting the standard pythonic ways of doing it
    def __len__(self):
        return self._cnt

    def __getitem__(self, index):
        """
        support for calling list[index]
        :param: index: node index to retrieve
        :returns: the node on the given index.
        :except: IndexError if the index is beyond length
        """
        return self._find_by_index(index)

    def __delitem__(self, index):
        """
        supports del list[index]
        :param: index: node index to retrieve
        :except: IndexError if the index is beyond length
        """
        prev = None
        # No need to check index here, _find_by_index does that already
        node = self._find_by_index(index)
        if (index > 0):
            print("Index > 0")
            prev = self._find_by_index(index-1)
        self._del(node, prev)

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
        while (self._it != None):
            node = self._it
            self._it = node.next
            return node
        # Re-locate iterator node after we
        self._it = self._head
        raise StopIteration

    def __iter__(self):
        """
        This method adds "iterable" implementation support
        """
        self._it = self._head
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


# In a commercial environment, these tests should be in a separate python file, I'm including them
# here for (lazynes?) teaching purposes
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
            self._list.add(node1)
            self._list.add(node3)
            self._list.add(node2)
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

        # Tests __getitem__ implementation
        def test_get_item(self):
            print("Testing __getitem__")
            node1 = Node(300)
            node2 = Node(1345)
            node3 = Node('aaaaa')
            self._list.add(node1)
            self._list.add(node3)
            self._list.add(node2)
            self.assertEqual(self._list[0], node1)
            self.assertEqual(self._list[2], node2)
            self.assertEqual(self._list[1], node3)

        # Tests exception raised on out of index
        def test_get_item_out_of_index(self):
            print("Testing __getitem__ raises IndexError")
            with self.assertRaises(IndexError) as context:
                node = self._list[4]
                self.assertTrue("Out of index" in context.exception)

        # Tests __delitem__ implementation
        def test_del_item(self):
            print("Testing __delitem__")
            node1 = Node(300)
            node2 = Node(1345)
            node3 = Node('aaaaa')
            self._list.add(node1)
            self._list.add(node3)
            self._list.add(node2)
            del self._list[0]
            # after deleting head, 'aaaa' should be index 1
            del self._list[1]
            # check head and length
            self.assertTrue(len(self._list), 1)
            self.assertEqual(self._list.head, node3)
            self.assertEqual(self._list[0], node3)

        # Tests exception raised on out of index
        def test_del_item_out_of_index(self):
            print("Testing __delitem__ raises IndexError on empty list")
            with self.assertRaises(IndexError) as context:
                del self._list[1]
                self.assertTrue("Out of index" in context.exception)


    # Setup testSuite and run the tests
    suite = unittest.TestSuite()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(testLinkedList)
    unittest.TextTestRunner().run(suite)
