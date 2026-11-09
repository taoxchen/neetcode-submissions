class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = "" 
        for c in s.lower():
            if c.isalnum(): 
                newS += c

        right = len(newS) - 1 
        left = 0 

        while left < right: 
            if newS[left] != newS[right]: 
               return False 
            left += 1 
            right -= 1 
        return True  


        