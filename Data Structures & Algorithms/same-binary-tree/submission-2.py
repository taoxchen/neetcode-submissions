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
        while z and a: 
            for _ in range(len(z)): 
                node = z.popleft() 
                node2 = a.popleft()

                if node is None and node2 is None: 
                    continue 
                if node is None or node2 is None or node.val != node2.val: 
                    return False 
                z.append(node.left)
                a.append(node2.left)
                z.append(node.right)
                a.append(node2.right)
        return True

        