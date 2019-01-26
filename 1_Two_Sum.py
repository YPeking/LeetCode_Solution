# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 23:15:40 2019

@author: yp
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index1, num1 in enumerate(nums):
            for index2, num2 in enumerate(nums[index1 + 1:]):
                if num1 + num2 == target:
                    return [index1, index2+index1+1]
        return []