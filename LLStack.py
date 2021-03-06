#!/usr/bin/env python3

"""
Stack implementation using the LinkedList implemented before. The advantages of using LinkedLists
vs arrays is the constant speed factor of adding new data, while the overall total time is higher
(if array uses amortized memory assignment and deleted, otherwise array is incredibly slower - O ~ 3N).

"""
__author__ = "Alberto Curro - bertothunder"
__version__ = "1.0"
__status__ = "Tested"
__license__ = "AGPL"

from LinkedList import LinkedList, Node

class LLStack(object):
	def __init__(self):
		self._list = LinkedList()

	def push(self, data=None):
		self._list.add(data)

	def pop(self):
		try:
			node = self._list[-1]
			del self._list[-1]
			return node.data
		except IndexError:
			# Mimicing the array error message
			raise IndexError("pop from empty stack")

	def __len__(self):
		return len(self._list)


if __name__ == '__main__':
	import unittest

	class StackTests(unittest.TestCase):
		def setUp(self):
			self._stack = LLStack()

		def test_index_error_pop_empty_stack(self):
			print("Testing IndexError on pop() from empty stack")
			self.assertRaises(IndexError, self._stack.pop)

		def test_len(self):
			print("Test push / pop changes length")
			for i in range(10):
				self._stack.push(i)
			self.assertEqual(len(self._stack), 10)
			for i in range(4):
				self._stack.pop()
			self.assertEqual(len(self._stack), 6)

    # Setup testSuite and run the tests
	suite = unittest.TestSuite()
	suite = unittest.defaultTestLoader.loadTestsFromTestCase(StackTests)
	unittest.TextTestRunner().run(suite)
