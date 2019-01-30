# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 19:53:01 2019

@author: yp
"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while (n != 0):
            result = result + n % 2
            n = n >> 1
                
        return result