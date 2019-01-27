# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 22:40:18 2019

@author: yp
"""

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        else:
            num_str = self.countAndSay(n-1)
            result = ""
            template = num_str[0]
            template_count = 0
            for i in range(len(num_str)):
                if num_str[i] == template:
                    template_count += 1
                else:
                    result += str(template_count)
                    result += template
                    template = num_str[i]
                    template_count = 1
                    
            result += str(template_count)
            result += template
        
        return result