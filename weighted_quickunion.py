#!/usr/bin/env python3

''' WeightedQuickUnion Union-Find algorithm implementation '''
class WeightedQuickUnionUF(object):
	def __init__(self, N, debug=False):
		self.__id__ = [i for i in range(N)]
		self.__rank__ = [1]*N
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
		pidp = self.__root__(p)
		pidq = self.__root__(q)
		if pidp == pidq:
			return 
		# Not connected yet
			# Decide which one has a higher rank to hang the other under
		if (self.__rank__[pidp] < self.__rank__[pidq]):
			self.__id__[pidp] = pidq;
			self.__rank__[pidq] += self.__rank__[pidp]
		else:
			self.__id__[pidq] = pidp
			self.__rank__[pidp] += self.__rank__[pidq]
		if (self.__pdebug__):
			print("New values : {}\n".format(self.__id__))

	def connected(self, p, q):
		if (self.__pdebug__):
			print("Connected({},{})".format(p,q))
		return (self.__root__(p) == self.__root__(q))

if __name__ == '__main__':
	uf = WeightedQuickUnionUF(10, True)
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
