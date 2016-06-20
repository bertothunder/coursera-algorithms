#!/usr/bin/env python3

class ShellSort(object):
    def __init__(self, elements, gaps):
        self._elements = elements
        self._gaps = gaps

    def sort(self):
        size = len(self._elements)
        for gap in reversed(self._gaps):
            if (gap > size):
                continue
            for idx in range(gap,size):
                #print("Idx: {}".format(idx))
                idx2 = idx
                while (idx2 >= gap and self._elements[idx2] < self._elements[idx2-gap]):
                    self._exchange(idx2, idx2-gap)
                    idx2 = idx2 - gap

    def _exchange(self, idx1, idx2):
        old = self._elements[idx2]
        #print('switching {}:{} with {}:{}'.format(idx1,self._elements[idx1], idx2, self._elements[idx2]))
        self._elements[idx2] = self._elements[idx1]
        self._elements[idx1] = old


if __name__ == '__main__':
    from sort_resources import hundred_random_unsorted, hundred_sorted, thousand_random_unsorted, thousand_sorted, ten_k_random_unsorted, ten_k_sorted

    tokuda = [1, 4, 9, 20, 46, 103, 233, 525, 1182, 2660, 5985, 13467, 30301, 68178, 153401, 345152, 776591,]
    s248 = [1, 3, 7, 16, 38, 94, 233, 577, 1431, 3549, 8801, 21826, 54128, 134237, 332908, 825611,]
    ciura = [1, 4, 10, 23, 57, 132, 301, 701,]

    elements = hundred_random_unsorted
    sorter = ShellSort(elements, ciura)
    sorter.sort()
    assert(elements == hundred_sorted)
    print("100 elements sorted as expected")

    elements = thousand_random_unsorted
    sorter = ShellSort(elements, ciura)
    sorter.sort()
    assert(elements == thousand_sorted)
    print("1000 elements sorted as expected")

    elements = ten_k_random_unsorted
    sorter = ShellSort(elements, ciura)
    sorter.sort()
    assert(elements == ten_k_sorted)
    print("10000 elements sorted as expected")
