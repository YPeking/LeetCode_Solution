# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 10:29:26 2019

@author: yp
"""

# 我的想法：水平扫描
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
            result = ""
            for i in range(min(len(strs[0]), len(strs[1]))):
                if strs[0][i] == strs[1][i]:
                    result += strs[0][i]
                else:
                    break
            for i in range(2, len(strs)):
                temp_result = ""
                for j in range(min(len(strs[i]), len(result))):
                    if strs[i][j] == result[j]:
                        temp_result += result[j]
                    else:
                        break
                result = temp_result
            
            return result

# 简便思路：分治处理
# 转化为集合，求交集
            