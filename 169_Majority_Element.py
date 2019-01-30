# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 18:15:26 2019

@author: yp
"""

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_dict = {}
        for num in nums:
            if num not in nums_dict.keys():
                nums_dict[num] = 1
            else:
                nums_dict[num] += 1
        
        for key in nums_dict.keys():
            if nums_dict[key] > len(nums)//2:
                return key