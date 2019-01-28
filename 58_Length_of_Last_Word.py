# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 12:18:43 2019

@author: yp
"""

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        str_list = s.lstrip(" ").rstrip(" ").split(" ")
        if len(str_list):
            return len(str_list[-1])
        else:
            return 0