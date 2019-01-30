# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 19:41:33 2019

@author: yp
"""

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bin_n = str(bin(n))
        result = 0
        index = 0
        for i in range(1, 33):
            if bin_n[-i] != 'b':
                result = result*2 + int(bin_n[-i])
                index += 1
            else:
                break
        for i in range(index+1, 33):
            result = result*2
        return result