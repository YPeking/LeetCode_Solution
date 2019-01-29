# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 13:10:30 2019

@author: yp
"""

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        else:
            diffs = []
            for i in range(len(prices) - 1):
                diffs.append(prices[i+1] - prices[i])
            
            temp_sum = 0
            max_sum = 0
            for diff in diffs:
                temp_sum += diff
                if temp_sum > max_sum:
                    max_sum = temp_sum
                if temp_sum < 0:
                    temp_sum = 0
            return max_sum
        