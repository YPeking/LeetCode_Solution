# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 12:41:54 2019

@author: yp
"""

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) < len(b):
            a = "0" * (len(b) - len(a)) + a
        else:
            b = "0" * (len(a) - len(b)) + b
            
        bit = 0
        result = ""
        for i in range(1, len(a)+1):
            if (int(a[-i]) + int(b[-i]) + bit) >= 2:
                remainder = (int(a[-i]) + int(b[-i]) + bit)%2
                result = str(remainder) + result
                bit = 1
            else:
                result = str(int(a[-i]) + int(b[-i]) + bit) + result
                bit = 0
        if bit == 1:
            result = "1" + result
        return result