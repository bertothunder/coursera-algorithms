#!/usr/bin/env python3

import unittest
from ..LinkedLists import Node, LinkedList

class testLinkedList(unittest.TestCase):
    def __init__(self):
        self._list = LinkedList()

    def test_count(self):
        self._list.add('1234')
        self._list.add('3230')
        self.assertEqual(self._list.len(), 2)

    def test_tail(self):
        tail = self._list.tail
        self.assertNotEqual(tail, None)
        self.assertEqual(tail.next, None)
        self.assertEqual(tail.data, '3230')

    def test_head(self):
        head = self._list.head
        self.assertNotEqual(head, None)
        self.assertEqual(head.next, self._list.tail)
        self.assertEqual(head.data, '1234')
