class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False 
        hashS = {}
        hashT = {}
        for i in s: 
            if i not in hashS: 
                hashS[i] = 1 
            else: 
                hashS[i] += 1 
        for i in t: 
            if i not in hashT: 
                hashT[i] = 1 
            else: 
                hashT[i] += 1 
        for i in s: 
            if i not in hashT or hashT[i] != hashS[i]: 
                return False
        return True 