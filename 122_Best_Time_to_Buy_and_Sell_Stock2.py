# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 13:18:14 2019

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
            
            sum = 0
            for diff in diffs:
                if diff > 0:
                    sum += diff
            return sum