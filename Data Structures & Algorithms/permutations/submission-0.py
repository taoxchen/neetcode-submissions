class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []

        def backtracking(path): 
            if len(path) == len(nums):
                return results.append(path[:])
            for num in nums: 
                if num in path: 
                    continue 
                path.append(num)    
                backtracking(path)
                path.pop()

        backtracking([])
 

        return results