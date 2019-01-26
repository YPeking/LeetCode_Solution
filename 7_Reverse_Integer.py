# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 22:56:03 2019

@author: yp
"""

# 我的思路
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        abs_x = abs(x)
        div_num = 1
        result = 0
        while True:
            if div_num <= abs_x:
                result = result*10 + (abs_x//div_num)%10
            else:
                if (result <= 2**31 - 1) and (result >= -2**31):
                    if x > 0:
                        return result
                    else:
                        return -result
                else:
                    return 0
            div_num = div_num*10
            
            
# 简便方法
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        str_x = str(x)
        x = ""
        if str_x[0] == '-':
            x += '-'
        x += str_x[::-1].lstrip("0").rstrip("-")
        x = int(x)
        if -2**31 < x < 2**31-1:
            return x
        return 0