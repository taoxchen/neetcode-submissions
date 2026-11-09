class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_string = ""
        if len(strs) == 0: 
                return encode_string
        for words in strs: 
                encode_string += str(len(words)) + "#" + words
        return encode_string

    def decode(self, s: str) -> List[str]:
        decode_list = [] 
        i = 0  
        while i < len(s):
                j = i  
                while s[j] != "#": 
                        j += 1 
                length = int(s[i:j])
                decode_list.append(s[j+1: j+1+ length])
                i = j + 1 + length
        return decode_list 
                

                
