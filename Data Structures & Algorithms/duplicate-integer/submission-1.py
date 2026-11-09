class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        container = {}
        for i in nums: 
            if i not in container: 
                container[i] = 1 
            else:
                return True 
        return False 