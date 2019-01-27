# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 21:38:31 2019

@author: yp
"""

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        elif len(haystack) < len(needle):
            return -1
        else:
            for i in range(len(haystack)-len(needle)+1):
                if haystack[i:i+len(needle)] == needle:
                    return i
            return -1