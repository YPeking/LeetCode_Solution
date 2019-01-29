# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 12:53:23 2019

@author: yp
"""

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            pre_list = [1, 1]
            for row_num in range(1, rowIndex):
                if row_num != 1:
                    pre_list = result_list
                result_list = []
                result_list.append(1)
                for i in range(1, row_num+1):
                    result_list.append(pre_list[i-1] + pre_list[i])
                result_list.append(1)
            return result_list