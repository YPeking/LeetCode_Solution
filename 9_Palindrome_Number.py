# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 23:16:44 2019

@author: yp
"""

# 我的思路
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x < 10:
            return True
        else:
            str_x = str(x)
            for i in range(len(str_x) // 2):
                if str_x[i] != str_x[len(str_x) - i -1]:
                    return False
            return True
        

# 简便方法
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            y = str(x)[::-1]
            if y == str(x):
                return True
            else:
                return False