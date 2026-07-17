# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None: 
            return True 
        elif p is None or q is None: 
            return False 

        z = deque([p]) 
        a = deque([q])
        while z: 
            for i in range(len(z)): 
                node = z.popleft() 
                node2 = a.popleft()
                if node.val != node2.val: 
                    return False 
                if node.left is None and node2.left is None: 
                    pass
                elif node.left is None or node2.left is None: 
                    return False 
                elif node.left.val != node2.left.val: 
                    return False 
                else: 
                    z.append(node.left)
                    a.append(node2.left)

                if node.right is None and node2.right is None: 
                    pass
                elif node.right is None or node2.right is None: 
                    return False 
                elif node.right.val != node2.right.val: 
                    return False 
                else: 
                    z.append(node.right)
                    a.append(node2.right)
        return True

        