class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []

        def backtrack(start, current_target): 
            if current_target == 0:
                return result.append(path[:])
            if current_target < 0:
                return 
            for i in range(start, len(nums)): 
                path.append(nums[i])
                backtrack(i, current_target - nums[i])
                path.pop()
        backtrack(0, target)
        return result

        

