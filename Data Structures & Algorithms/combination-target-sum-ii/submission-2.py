class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = [] 
        path = [] 
        def backtrack(start_index, current_target):
            if current_target == 0:
                return results.append(path[:])
            if current_target < 0: 
                return
            candidates.sort() 

            for i in range(start_index, len(candidates)): 
                if i > start_index and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i]) 
                backtrack(i + 1 , current_target - candidates[i]) 
                path.pop() 
    
        backtrack(0,target) 
        return results