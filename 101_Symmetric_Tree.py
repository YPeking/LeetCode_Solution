# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 19:22:50 2019

@author: yp
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return self.digui(root.left, root.right)
        else:
            return True
    
    def digui(self, q, p):
        if q and p:
            return q.val == p.val and self.digui(q.left, p.right) and self.digui(q.right, p.left)
        else:
            return not q and not p
        