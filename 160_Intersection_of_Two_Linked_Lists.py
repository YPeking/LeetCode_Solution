# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 13:01:22 2019

@author: yp
"""

# 碉堡
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if (not headA) or (not headB):
            return None
        else:
            A_ptr = headA
            B_ptr = headB
            while (A_ptr != B_ptr):
                if A_ptr:
                    A_ptr = A_ptr.next
                else:
                    A_ptr = headB
                
                if B_ptr:
                    B_ptr = B_ptr.next
                else:
                    B_ptr = headA
            
            return A_ptr
        