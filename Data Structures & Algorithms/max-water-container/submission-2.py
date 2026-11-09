class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        right = len(heights) - 1 
        if len(set(heights)) == 1: 
            return heights[left] * (len(heights) -1 )
        
        maxVal = 0 
        while left < right: 
            maxVal = max(maxVal, min(heights[left], heights[right]) * (right - left))
            if heights[right] >= heights[left]: 
                left += 1 
            elif heights[right] < heights[left]: 
                right -= 1 
        return maxVal