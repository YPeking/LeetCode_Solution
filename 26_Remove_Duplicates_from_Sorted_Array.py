# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 20:48:58 2019

@author: yp
"""
# 性能差距很大

# 我的思路
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        less_element = 0
        for i in range(len(nums)):
            if i < (len(nums)-1-less_element):
                temp_less_element = 0
                for j in range(i, len(nums)-1-less_element) :
                    if nums[j] == nums[j+1]:
                        temp_less_element += 1
                    else:
                        break
                less_element += temp_less_element
                for j in range(i+1, len(nums)-less_element):
                    nums[j] = nums[j+temp_less_element]
            else:
                break
        
        return (len(nums)-less_element)
    
    

# 设置两个索引，不用每次都进行赋值
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        
        index_i = 0
        for j in range(1, len(nums)):
            if nums[j] == nums[index_i]:
                continue
            else:
                index_i += 1
                nums[index_i] = nums[j]
        return index_i+1



