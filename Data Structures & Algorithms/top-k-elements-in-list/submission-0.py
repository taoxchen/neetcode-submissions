class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsMap = {} 

        for i in nums: 
            numsMap[i] = numsMap.get(i,0) + 1 
        
        result = []
        for j in range(k):  
            numMax = 0
            keyMax = None 
            for i in numsMap.keys(): 
                if numMax < numsMap[i]: 
                    numMax = numsMap[i]
                    keyMax = i 
            result.append(keyMax)
            numsMap.pop(keyMax)
        return result 
        
            
        