# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 22:20:38 2019

@author: yp
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        else:
            left_depth = self.minDepth(root.left)
            right_depth = self.minDepth(root.right)
            if min(left_depth, right_depth) == 0:
                return 1 + left_depth + right_depth
            else:
                return 1 + min(left_depth, right_depth)