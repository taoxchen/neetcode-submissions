class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_string = ""
        for i in range(len(strs)): 
                encode_string += str(len(strs[i])) + "#" 
                encode_string += strs[i]
        return encode_string
  
    def decode(self, strs: str) -> List[str]:
        decode_string = [] 
        i = 0 
        while i < len(strs):
            j = i  
            while strs[j] != "#":
                j += 1
            length = int(strs[i:j])
        
            decode_string.append(strs[j+1: j+ length +1 ])

            i = j + 1 + length  
        return decode_string

