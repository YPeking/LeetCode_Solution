# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 10:21:57 2019

@author: yp
"""

# 我的想法
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        Roman_dict = {'I':1, 'V':5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        Roman_num = []
        result = []
        for Roman_str in s:
            Roman_num.append(Roman_dict[Roman_str])
            
        for i in range(len(Roman_num)):
            if i != (len(Roman_num) -1):
                if Roman_num[i] < Roman_num[i+1]:
                    temp_num = Roman_num[i+1] - Roman_num[i]
                    result.append(temp_num)
                elif (i == 0) or (Roman_num[i] <= Roman_num[i-1]):
                    result.append(Roman_num[i])
            else:
                if Roman_num[i] <= Roman_num[i-1]:
                    result.append(Roman_num[i])
        
        return sum(result)
    

# 简便思路
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        Roman_dict = {'I':1, 'V':5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        Roman_num = []
        result = 0
        for Roman_str in s:
            Roman_num.append(Roman_dict[Roman_str])
            
        for i in range(len(Roman_num)-1):
            if Roman_num[i] < Roman_num[i+1]:
                result = result - Roman_num[i]
            else:
                result = result + Roman_num[i]
        result = result + Roman_num[-1]
        
        return result