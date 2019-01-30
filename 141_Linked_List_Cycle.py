# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 12:26:43 2019

@author: yp
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if (head == None) or (head.next == None) or (head.next.next == None):
            return False
        else:
            fast_ptr = head.next
            low_ptr = head
            while (fast_ptr != low_ptr):
                if (fast_ptr.next != None) and (fast_ptr.next.next != None):
                    fast_ptr = fast_ptr.next.next
                    low_ptr = low_ptr.next
                else:
                    return False
            return True