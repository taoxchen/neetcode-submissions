class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 
        right = len(prices) - 1 
        index = 0 
        max_profit = 0 
        while index < right: 
            if prices[left] > prices[index]: 
                left += 1 
                index = left 
            else: 
                if index < right: 
                    index += 1 
                    current_profit = prices[index] - prices[left] 
                    max_profit = max(current_profit, max_profit)   
        
        return max_profit 