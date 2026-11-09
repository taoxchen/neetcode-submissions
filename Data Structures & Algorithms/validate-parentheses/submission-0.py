class Solution:
    def isValid(self, s: str) -> bool:
        sHash = {")" : "(", "}" : "{", "]" :"["} 
        stack = [] 

        for i in s: 
            if i in sHash.values(): 
                stack.append(i)
            elif i in sHash: 
                if not stack: 
                    return False 
                verify = stack.pop() 
                if sHash[i] != verify: 
                    return False 
        return len(stack) == 0

        