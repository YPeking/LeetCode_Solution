# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 21:05:15 2019

@author: yp
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        r = ListNode(0)
        p = r
        while l1 and l2:
            if l1.val <= l2.val:
                p.next = l1
                p = p.next
                l1 = l1.next
            else:
                p.next = l2
                p = p.next
                l2 = l2.next
        if l1:
            while l1:
                p.next = l1
                p = p.next
                l1 = l1.next
        elif l2:
            while l2:
                p.next = l2
                p = p.next
                l2 = l2.next
                
        return r.next
            