# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 13:24:25 2019

@author: yp
"""

# 斐波那契数列，递归形式，时间开销比较大
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)
        

# 非递归形式
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            a, b = 1, 2
            i = 2
            while i < n:
                a, b = b, a+b
                i += 1
            return b