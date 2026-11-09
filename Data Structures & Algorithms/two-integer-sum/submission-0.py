class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        countNums = {} 
        for i in range(len(nums)): 
            difference = target - nums[i]
            if difference in countNums: 
                return [countNums[difference],i]
            else:  
                countNums[nums[i]] = i 