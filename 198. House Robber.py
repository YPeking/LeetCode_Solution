# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 20:08:57 2019

@author: yp
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        else:
            result_pre = nums[0]
            result_last = max(nums[0:2])
            for i in range(2, len(nums)):
                result_now = max(nums[i] + result_pre, result_last)
                result_pre = result_last
                result_last = result_now
            return result_now