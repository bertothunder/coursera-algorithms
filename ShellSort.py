#!/usr/bin/env python3

import datetime
from random import SystemRandom

class ShellSort(object):
    def __init__(self, elements, gaps):
        self._elements = elements
        self._gaps = gaps

    def sort(self):
        for idx in range(self._last):
            val1 = self._elements[idx]
            #print('element {}: {}'.format(idx, val1))
            pidx = idx
            idx2 = idx - 1
            while idx2 >= 0:
                if (self._elements[idx2] >= self._elements[pidx]):
                    #print('Found new self._max: {} - {}'.format(idx2, self._elements[idx2]))
                    self._exchange(pidx, idx2)
                    pidx = idx2
                idx2 = idx2 - 1

    def _exchange(self, idx1, idx2):
        self._max = self._elements[idx2]
        #print('switching {}:{} with {}:{}'.format(idx1,self._elements[idx1], idx2, self._elements[idx2]))
        self._elements[idx2] = self._elements[idx1]
        self._elements[idx1] = self._max


if __name__ == '__main__':
    tokuda = [1, 4, 9, 20, 46, 103, 233, 525, 1182, 2660, 5985, 13467, 30301, 68178, 153401, 345152, 776591,]
    s248 = [1, 3, 7, 16, 38, 94, 233, 577, 1431, 3549, 8801, 21826, 54128, 134237, 332908, 825611,]
    ciura = [1, 4, 10, 23, 57, 132, 301, 701,]
    randomizer = SystemRandom()
    randomizer.seed(datetime.datetime.now())
    num_elems = randomizer.randrange(1, 10000)
    elements = [randomizer.randrange(1, num_elems) for i in range(num_elems)]
    randomizer.shuffle(elements)
    print("Unsorted: {}".format(elements))
    sorter = ShellSort(elements, tokuda)
    sorter.sort()
    print("Sorted: {}".format(elements))
