#!/usr/bin/env python3

class QuickFindUF(object):
	def __init__(self, N):
		self.__id__ = [i for i in range(N)]
		self.__count__ = N

	def union(self, p, q):
		# Check indices
		if (p > self.__count__ or q > self.__count__):
			print('Indices do not exist')
		elif (self.__id__[q] != self.__id__[p]): # Not connected yet
			pidp = self.__id__[p]
			pidq = self.__id__[q]
			self.__id__[p] = pidq
			for n in range(self.__count__):
				if self.__id__[n] == pidp: # or self.__id__[n] == pidq:
					print("Writing {} to {}".format(q, n))
					self.__id__[n] = pidq			
			print("New values: {}".format(self.__id__))
		else:
			print("Something went wrong!")

	def connected(self, p, q):
		if (p > self.__count__ or q > self.__count__):
			print("Out of indices")
			return false
		return (self.__id__[p] == self.__id__[q])


if __name__ == '__main__':
	uf = QuickFindUF(50)
	uf.union(1,49)
	uf.union(0,1)
	uf.union(45,4)
	uf.union(46,45)
	print("0:49 => {}".format(uf.connected(0,49))) #true
	print("45:46 => {}".format(uf.connected(45,46))) #true
	print("1:2 => {}".format(uf.connected(1,2))) #false
	print("49:48 => {}".format(uf.connected(49, 48))) #false