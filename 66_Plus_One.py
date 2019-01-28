# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 12:28:17 2019

@author: yp
"""

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digit_str = ""
        for num in digits:
            digit_str += str(num)
        digit_int = int(digit_str)
        digit_int += 1
        digit_str = str(digit_int)
        result_list = []
        for num_str in digit_str:
            result_list.append(int(num_str))
        
        return result_list
