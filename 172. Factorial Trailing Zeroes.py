# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 18:41:49 2019

@author: yp
"""

# 检查小于n的数中5的个数
class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        num_exp = 0
        while 5 ** num_exp <= n:
            num_exp += 1
        
        result = 0
        for i in range(1, num_exp):
            result += n//(5**i)
            
        return result