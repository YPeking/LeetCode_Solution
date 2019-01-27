# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 22:40:50 2019

@author: yp
"""

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        temp_sum = 0
        max_sum = nums[0]
        for num in nums:
            temp_sum += num
            if temp_sum > max_sum:
                max_sum = temp_sum
            if temp_sum < 0:
                temp_sum = 0
        return max_sum
                