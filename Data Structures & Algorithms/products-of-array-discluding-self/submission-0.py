class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count_zeros = nums.count(0)

        if count_zeros > 1: 
            return [0] * len(nums)

        product = 1
        for i in nums: 
            if i != 0:  
                product = product * i 
        
        res = [] 
        if count_zeros == 1:  
            for i in nums: 
                if i == 0: 
                    res.append(product)
                else: 
                    res.append(0)
        else: 
            for i in nums: 
                res.append(product //i)
        return res  
        