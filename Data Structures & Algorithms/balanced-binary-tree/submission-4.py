# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root is None:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            # (2) if either subtree already reported "unbalanced",
            #     pass that signal up immediately
            if left == -1 or right == -1:
                return -1
            
            # (3) if THIS node's two subtrees differ in height by more than 1,
            #     this node is unbalanced
            if abs(left - right) > 1:
                return -1
            
            # (4) otherwise, return the actual height of this subtree
            return 1 + max(left,right)  # combine left and right into a height
        
        return dfs(root) != -1
