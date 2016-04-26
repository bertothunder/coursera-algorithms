#!/usr/bin/env python3

__author__ = "Alberto Curro - bertothunder"
__version__ = "1.0"
__status__ = "Tested"
__license__ = "AGPL"

"""
Stack implementation using internally an array. The tradeoff of using the array is a less inmediate
speed when adding/deleting nodes. Since Python implementation for array uses a highly optimized
amortized memory management, this container will be useful if we are looking for a general speed
(for the entire set of operations).
"""

class ArrayStack(object):
	def __init__(self):
		self._list = []  # why I love Python: [None]*0 is [] :)

	def push(self, data=None):
		self._list.append(data)

	def pop(self):
		try:
			return self._list.pop()
		except IndexError:
			raise IndexError("pop from an empty stack")

	def __len__(self):
		return len(self._list)


if __name__ == '__main__':
	import unittest

	class StackTests(unittest.TestCase):
		def setUp(self):
			self._stack = ArrayStack()

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
