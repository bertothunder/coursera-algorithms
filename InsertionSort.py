#!/usr/bin/env python3

import datetime
from random import SystemRandom

class InsertionSort(object):
    def __init__(self, elements):
        self._elements = elements
        self._last = len(elements)

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
    randomizer = SystemRandom()
    randomizer.seed(datetime.datetime.now())
    num_elems = randomizer.randrange(1, 1000)
    elements = [randomizer.randrange(1, num_elems) for i in range(num_elems)]
    randomizer.shuffle(elements)
    print("Unsorted: {}".format(elements))
    sorter = InsertionSort(elements)
    sorter.sort()
    print("Sorted: {}".format(elements))
