class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_string = ""
        for i in range(len(strs)): 
                encode_string += strs[i]
                encode_string += "🥹" 
        return encode_string
  
    def decode(self, strs: str) -> List[str]:
        decode_string = [] 
        adding_character = ""
        for char in strs: 
            if char == "🥹": 
                decode_string.append(adding_character)
                adding_character = ""
            else: 
                adding_character += char

        return decode_string 
                
