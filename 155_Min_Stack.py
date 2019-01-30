# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 12:41:52 2019

@author: yp
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack_List = []
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.stack_List) == 0:
            self.min_stack.append(x)
        else:
            if x <= self.min_stack[-1]:
                self.min_stack.append(x)
        
        self.stack_List.append(x)        

    def pop(self):
        """
        :rtype: void
        """
        if self.stack_List[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack_List.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack_List[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()