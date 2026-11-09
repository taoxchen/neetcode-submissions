class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strsHash = {} 
        for i in strs: 
            key = tuple(sorted(i))
            if key not in strsHash: 
                strsHash[key] = [i]
            else: 
                strsHash[key].append(i)
        return list(strsHash.values()) 

        