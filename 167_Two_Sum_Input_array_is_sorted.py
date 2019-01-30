# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 13:16:29 2019

@author: yp
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
    
        i = 0
        j = len(numbers) - 1
        while(1):
            t = numbers[i] + numbers[j]
            if i == j:
                return []
            elif t == target:
                return [i+1, j+1]
            elif(t > target):
                j -= 1
            else:
                i += 1
            