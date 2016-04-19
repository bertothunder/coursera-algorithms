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


"""
A standard LinkedList implementation, implementing all operations from scratch.
Mutable, Iterable and iterator container.
"""
class LinkedList(object):
	def __init__(self):
		self.__head = None
		self.__tail = None
		self.__cnt = 0

	def add(self, data):
		"""
		Adds a new element into the container
		"""
		node = Node(data)
		if self.__head == None:
			self.__head = node
		if self.__tail == None:
			self.__tail = self.__head
		else:
			self.__tail.next = node
			self.__tail = node
		self.__cnt += 1

	def __find(self, data):
		node = self.__head
		prev = None
		while node != None:
			prev = node
			node = node.next
			if (node.data == data):
				break

		if node == None:
			raise IndexError("Element was not found")
		return prev, node

	def delete(self, data):
		"""
		Deletes the given element.
		:except: IndexError if no node is found with the given data on it
		"""
		prev, node = self.__find(data)
		prev.next = node.next
		if node.next == None:
			# move tail
			self.__tail = prev
		del node
		self.__cnt -= 1

	@property
	def count(self):
		return self.__len__()

	@property
	def tail(self):
	    return self.__tail

	@property
	def head(self):
	    return self.__head

	# Set of magic methods supporting the standard pythonic ways of doing it
	def __len__(self):
		return self.__cnt

	def __getitem__(self, data):
		"""
		:except: IndexError: no node containing given data could be found
		"""
		return self.__find(data)

	def __delitem__(self, data):
		"""
		:except: IndexError: no node containing given data could be deleted
		"""
		self.delete(data)

	def __iter__(self):
		"""
		This method adds "iterable" implementation support
		"""
		return self

	def __contains__(self, data):
		"""
		Supporting "in" call (is 1 in list?)
		"""
		try:
			self.__find(data)
		except IndexError:
			return False
		return True

	def next(self):
		"""
		This method adds the iterator support (for each i in container x)
		"""
		node = self.__head
		while (node.next != None):
			yield node
			node = node.next
		raise StopIteration


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
	#	"""
	#	Supporting reversed() call
	#	"""
	# Tricky one! the internal array supports reversion, but the single linked list
	# should not support it (next() only goes forward, never back, that needs a
	# double linked list!). So this should not be present
	#	return iter(data.reversed())

	def __contains__(self, data):
		"""
		Supporting "in" call
		"""
		try:
			self.__data.index(data)
		except ValueError:
			return False
		return True

	def next(self):
		"""
		This method adds the iterator support (for i in x)
		"""
		for i in self.__data:
			yield i
		raise StopIteration
