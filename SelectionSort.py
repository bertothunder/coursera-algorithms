#!/usr/bin/env python3

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
    from sort_resources import hundred_sorted, hundred_random_unsorted, thousand_random_unsorted, thousand_sorted, ten_k_random_unsorted, ten_k_sorted

    elements = hundred_random_unsorted
    sorter = SelectionSort(elements)
    sorter.sort()
    assert(elements == hundred_sorted)
    print("100 elements sorted as expected")

    elements = thousand_random_unsorted
    sorter = SelectionSort(elements)
    sorter.sort()
    assert(elements == thousand_sorted)
    print("1000 elements sorted as expected")

    elements = ten_k_random_unsorted
    sorter = SelectionSort(elements)
    sorter.sort()
    assert(elements == ten_k_sorted)
    print("10000 elements sorted as expected")
