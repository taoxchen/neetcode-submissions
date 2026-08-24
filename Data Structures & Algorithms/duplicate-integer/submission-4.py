class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        container = {} 

        for i in nums: 
            if i in container: 
                return True
            else: 
                container[i] = 1 
        return False