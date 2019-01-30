# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 19:01:52 2019

@author: yp
"""

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #for i in range(k):
        #    nums.insert(0, nums.pop())
        
        nums[:] = nums[-(k%len(nums)):] + nums[:-(k%len(nums))]