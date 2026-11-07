class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0
        result = 0 
        freq = {} 
        maxf = 0 

        for i in range(len(s)): 
            char = s[i]
            freq[char] = freq.get(char, 0) + 1
            
            maxf = max(maxf, freq[char])
            
            #when window is invalid? 
            while (i - left + 1) - maxf > k :  
                freq[s[left]] -= 1
                left += 1
            result = max(result, i - left + 1)

        return result