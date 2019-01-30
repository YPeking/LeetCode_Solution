# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 18:19:30 2019

@author: yp
"""

class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for num_str in s:
            temp_num = ord(num_str) - 64
            result = result*26 + temp_num
        
        return result