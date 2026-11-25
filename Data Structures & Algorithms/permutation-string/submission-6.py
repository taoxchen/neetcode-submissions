class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2): 
            return False 

        left = 0 
        right = len(s1) 

        freq_count = {} 

        for i in range(len(s1)):
            freq_count[s1[i]] = freq_count.get(s1[i], 0) + 1  
        
        print(freq_count)
        while right <= len(s2):             
            temp_freq_count = {} 

            for i in range(left, right): 
                temp_freq_count[s2[i]] = temp_freq_count.get(s2[i], 0) + 1 

            print(temp_freq_count)
            if temp_freq_count == freq_count: 
                return True

            #print(left, right)
            left += 1 
            right += 1 

        return False  

