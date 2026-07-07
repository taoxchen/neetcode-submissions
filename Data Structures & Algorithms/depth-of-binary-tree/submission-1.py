# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: 
            return 0 
        if (root.val is not None) and (root.left is None and root.right is None): 
            return 1  
        
        counterLeft = 1
        counterRight = 1
        counterLeft += self.maxDepth(root.left)
        counterRight += self.maxDepth(root.right)
        mDepth = max(counterLeft,counterRight)
        return mDepth 