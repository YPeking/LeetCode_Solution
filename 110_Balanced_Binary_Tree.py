# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 22:33:31 2019

@author: yp
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        else:
            if (abs(self.tree_depth(root.left) - self.tree_depth(root.right)) < 2) and self.isBalanced(root.left) and self.isBalanced(root.right):
                return True
            else:
                return False
        
        
    def tree_depth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        else:
            return 1 + max(self.tree_depth(root.left), self.tree_depth(root.right))