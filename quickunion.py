#!/usr/bin/env python3

''' QuickUnion Union-Find algorithm implementation '''
class QuickUnionUF(object):
	def __init__(self, N, debug=False):
		self.__id__ = [i for i in range(N)]
		self.__count__ = N
		self.__pdebug__ = debug

	def __root__(self, idx):
		'''  One node is root when the index and the value are the same. This could be using recursion '''
		if (self.__pdebug__):
			print("Root({})".format(idx))
		while(idx != self.__id__[idx]):
			if (self.__pdebug__):
				print("\tRoot of {} is {}".format(idx, self.__id__[idx]))
			idx = self.__id__[idx]
		return idx

	def union(self, p, q):
		if (self.__pdebug__):
			print("Union({}, {})".format(p,q))
		# Check indices
		if (p > self.__count__ or q > self.__count__):
			print('Indices do not exist')
		elif (not self.connected(p, q)): # Not connected yet
			pidp = self.__root__(p)
			pidq = self.__root__(q)
			# Change root of p to hang under root of q
			self.__id__[pidp] = pidq
		if (self.__pdebug__):
			print("New values : {}\n".format(self.__id__))

	def connected(self, p, q):
		if (self.__pdebug__):
			print("Connected({},{})".format(p,q))
		return (self.__root__(p) == self.__root__(q))

if __name__ == '__main__':
	uf = QuickUnionUF(10)
	uf.union(0,8)
	uf.union(2,3)
	uf.union(1,3)
	uf.union(5,0)
	uf.union(8,7)
	print("0:7 => {}".format(uf.connected(0,7))) # true
	print("5:8 => {}".format(uf.connected(5,8))) # true
	print("6:1 => {}".format(uf.connected(6,1))) # false
	print("8:9 => {}".format(uf.connected(8,9))) # false
	uf.union(7,6)
	uf.union(6,1)
	print("7:1 => {}".format(uf.connected(0,3))) # True now
