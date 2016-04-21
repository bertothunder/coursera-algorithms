#!/usr/bin/env python3

''' Node is the basic node structure to use in the linked list '''

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

    def _find(self, data):
        node = self._head
        prev = None
        while node != None:
            prev = node
            if (node.data == data):
                break
            node = node.next
        if node == None:
            raise IndexError("Element was not found")
        return prev, node

    def delete(self, data):
        """
        Deletes the given element.
        :except: IndexError if no node is found with the given data on it
        """
        prev, node = self._find(data)
        prev.next = node.next
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
        :except: IndexError: no node containing given data could be found
        """
        return self._find(data)

    def __delitem__(self, data):
        """
        :except: IndexError: no node containing given data could be deleted
        """
        self.delete(data)

    def __contains__(self, data):
        """
        Supporting "in" call (is 1 in list?)
        """
        try:
            self._find(data)
        except IndexError:
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
           str += '{} -> '.format(node)
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
        def test_find(self):
            node1 = Node(300)
            node2 = Node(1345)
            node3 = Node('aaaaa')
            self.assertEqual(300 in self._list, True)
            self.assertEqual(2000 in self._list, False)
            self.assertEqual('aaaaa' in self._list, True)

    suite = unittest.TestSuite()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(testLinkedList)
    unittest.TextTestRunner().run(suite) 
