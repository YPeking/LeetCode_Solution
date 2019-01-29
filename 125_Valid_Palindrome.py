# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 13:26:06 2019

@author: yp
"""

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        clean_str = ""
        for string in s:
            if string.isdigit() or string.isalpha():
                clean_str += string.lower()
        
        if len(clean_str) <2:
            return True
        else:
            for i in range(len(clean_str) // 2):
                if clean_str[i] != clean_str[-i-1]:
                    return False
            return True