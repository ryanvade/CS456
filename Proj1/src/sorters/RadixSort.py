#!/usr/bin/env python3
from sorters.Sorter import Sorter
import math

class RadixSort(Sorter):
    """docstring for RadixSort."""

    def __init__(self, A):
        super(RadixSort, self).__init__(A)

    def sort(self):
        B = self.A.copy()
        return self.__radix_sort(B, 10, 6)

    def __radix_sort(self, ARR, N, MAXLEN):
        RADIX = 1
        for x in range(MAXLEN):
            bins = [[] for i in range(N)]
            for y in ARR:
                bins[math.floor((y/RADIX ** x)%N)].append(y)
            RADIX = RADIX * 10
            ARR=[]
            for section in bins:
                ARR.extend(section)
        return ARR
