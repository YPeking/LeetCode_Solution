# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 11:04:43 2019

@author: yp
"""

# 我的错误解法
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parenth_dict = {r'(': r")", r"[":r"]", r"{":r"}"}
        flag = False
        if len(s) > 1: 
            if s[0] in r"([{":
                for index, string in enumerate(s):
                    if parenth_dict[s[0]] == string:
                        flag = True
                        left_flag = self.isValid(s[1:index])
                        if index != (len(s) - 1):
                            right_flag = self.isValid(s[index+1:])
                        else:
                            right_flag = True
                        return (flag and left_flag and right_flag)
                    else:
                        continue
            else:
                return False
        elif len(s) == 1:
            return False
        elif s == "":
            return True
        
        return flag
    
# 用栈作为数据结构
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parenth_dict = {r')': r"(", r"]":r"[", r"}":r"{"}
        stack = []
        for string in s:
            if string in r"({[":
                stack.append(string)
            elif string in r")]}":
                if len(stack) == 0:
                    return False
                if stack[-1] == parenth_dict[string]:
                    stack.pop(-1)
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False