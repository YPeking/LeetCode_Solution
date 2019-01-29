# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 13:33:49 2019

@author: yp
"""

# 对异或的运用，厉害
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for num in nums:
            a = a ^ num
        return a