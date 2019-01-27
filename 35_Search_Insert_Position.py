# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 21:39:09 2019

@author: yp
"""

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        for i in range(len(nums)):
            if (target == nums[i]) or (target < nums[i]):
                return i
            
        return len(nums)