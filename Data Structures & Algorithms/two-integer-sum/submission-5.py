class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference = {} 

        for i in range(len(nums)): 
            diff = target - nums[i]
            if diff not in difference: 
                difference[nums[i]] = i 
            else: 
                return [difference[diff], i]        
                
