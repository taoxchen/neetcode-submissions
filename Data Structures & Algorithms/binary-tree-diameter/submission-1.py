# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0 

        def maxDepth(root: Optional[TreeNode]) -> int: 
            nonlocal diameter
            
            if root is None: 
                return 0 

            left = maxDepth(root.left) 
            right = maxDepth(root.right) 

            diameter = max(diameter, left + right) 

            return max(left, right) + 1 

        maxDepth(root) 

        return diameter




        