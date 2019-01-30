# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 13:37:01 2019

@author: yp
"""

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        # 和26进制类似
        result = ""
        division = n
        while division > 26:
            residual = division % 26
            if residual == 0:
                division = division // 26 - 1
                residual = 26
            else:
                division = division // 26
            result = chr(residual+64) + result
        result = chr(division+64) + result
        
        return result