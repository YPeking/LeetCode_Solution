# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 21:21:23 2019

@author: yp
"""

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) < 1:
            return len(nums)
        
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        
        return index