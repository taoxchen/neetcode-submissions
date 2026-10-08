class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""
        for c in s: 
            if c.isalnum(): 
                newS += (c.lower())
        left = 0 
        right = len(newS) - 1 

        while left < right: 
            if newS[left] != newS[right]: 
                return False 
            left += 1 
            right -= 1 
        print(left,right)
        return True
        