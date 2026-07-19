class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []

        def backtracking(path, index): 
            if index == len(nums): 
                return results.append(path[:]) 

            path.append(nums[index])
            backtracking(path, index + 1)
            path.pop() 

            backtracking(path, index +1)
        result = backtracking([], 0)
        return results 