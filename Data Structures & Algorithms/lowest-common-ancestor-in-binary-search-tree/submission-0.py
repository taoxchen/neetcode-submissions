# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def traverse(root: TreeNode, p:TreeNode, q: TreeNode): 

            if root is None: 
                return None 

            if root.val == p.val: 
                return p
            elif root.val == q.val: 
                return q

            if (root.val > p.val and root.val < q.val) or (root.val < p.val and root.val > q.val): 
                return root
            elif root.val > p.val and root.val > q.val: 
                print("hello")
                return traverse(root.left, p, q)
            elif root.val < p.val and root.val < q.val: 
                print("hello2")
                return traverse(root.right, p, q)

        result = traverse(root, p, q)
        return result
