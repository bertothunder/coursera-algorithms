#!/usr/bin/env python3

class InsertionSort(object):
    def __init__(self, elements):
        self._elements = elements
        self._last = len(elements)

    def sort(self):
        for idx in range(self._last):
            val1 = self._elements[idx]
            pidx = idx
            idx2 = idx - 1
            while idx2 >= 0:
                if (self._elements[idx2] > self._elements[pidx]):
                    self._exchange(pidx, idx2)
                    pidx = idx2
                idx2 = idx2 - 1

    def _exchange(self, idx1, idx2):
        self._max = self._elements[idx2]
        #print('switching {}:{} with {}:{}'.format(idx1,self._elements[idx1], idx2, self._elements[idx2]))
        self._elements[idx2] = self._elements[idx1]
        self._elements[idx1] = self._max


if __name__ == '__main__':
    from sort_resources import hundred_sorted, hundred_random_unsorted, thousand_random_unsorted, thousand_sorted, ten_k_random_unsorted, ten_k_sorted

    elements = hundred_random_unsorted
    sorter = InsertionSort(elements)
    sorter.sort()
    assert(elements == hundred_sorted)
    print("100 elements sorted as expected")

    elements = thousand_random_unsorted
    sorter = InsertionSort(elements)
    sorter.sort()
    assert(elements == thousand_sorted)
    print("1000 elements sorted as expected")

    elements = ten_k_random_unsorted
    sorter = InsertionSort(elements)
    sorter.sort()
    assert(elements == ten_k_sorted)
    print("10000 elements sorted as expected")
