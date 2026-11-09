class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right = len(numbers) -1 
        left = 0

        while left < right: 
            curSum = numbers[left] + numbers[right]
            if curSum == target: 
                return [left+1,right + 1]
            if curSum < target:  
                left += 1 
            if curSum > target: 
                right -= 1
        return [] 