#!/usr/bin/env python3

import logging
import datetime
from random import SystemRandom

class SelectionSort(object):
    def __init__(self, elements):
        self._elements = elements
        self._last = len(elements)
        self._minim = 0

    def sort(self):
        for idx in range(self._last):
            val1 = self._elements[idx]
            self._minim = self._elements[idx]
            #print('element {}: {}'.format(idx, val1))
            for idx2 in range(idx+1, self._last):
                if (self._elements[idx2] <= self._minim):
                    #print('Found new self._minim: {} - {}'.format(idx2, self._elements[idx2]))
                    self._exchange(idx, idx2)

    def _exchange(self, idx1, idx2):
        self._minim = self._elements[idx2]
        #print('switching {}:{} with {}:{}'.format(idx1,self._elements[idx1], idx2, self._elements[idx2]))
        self._elements[idx2] = self._elements[idx1]
        self._elements[idx1] = self._minim


if __name__ == '__main__':
    randomizer = SystemRandom()
    randomizer.seed(datetime.datetime.now())
    num_elems = randomizer.randrange(1, 1000)
    elements = [randomizer.randrange(1, num_elems) for i in range(num_elems)]
    randomizer.shuffle(elements)
    print("Unsorted: {}".format(elements))
    sorter = SelectionSort(elements)
    sorter.sort()
    print("Sorted: {}".format(elements))
