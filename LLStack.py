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

from LinkedList import LinkedList
from Node import Node

class LLStack(object):
	def __init__(self, size=0):
		self._list = LinkedList()
		if (size):
			for n in range(size):
				self.push()

	def push(self, data=None):
		self._list.add(data)

	def __len__(self):
		return len(self._list)

if __name__ == '__main__':
	import unittest

	class StackTests(unittest.TestCase):
		def setUp(self):
			pass

    # Setup testSuite and run the tests
    suite = unittest.TestSuite()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(StackTests)
    unittest.TextTestRunner().run(suite)
