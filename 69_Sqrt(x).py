# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 13:12:14 2019

@author: yp
"""

# 牛顿迭代法求平方根
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 1:
            return x
        r = x
        while r > x/r:
            r = (r + x/r)//2
        return int(r)