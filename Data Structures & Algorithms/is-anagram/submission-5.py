class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hash1 = {}
        hash2 = {}
        
        for i, j in zip(s,t):
            hash1[i] = hash1.get(i,0)+1
            hash2[j] = hash2.get(j,0)+1

        return hash1 == hash2