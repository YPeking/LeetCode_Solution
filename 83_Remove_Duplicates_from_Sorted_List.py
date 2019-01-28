# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 18:28:57 2019

@author: yp
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ptr = head
        result_ptr = ptr
        while (ptr) and (ptr.next):
            if ptr.val == ptr.next.val:
                ptr.next = ptr.next.next
                continue
            ptr = ptr.next
        
        return result_ptr