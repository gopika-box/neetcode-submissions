class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str=""

        for s in strs:
            encoded_str +=f'{len(s)}#{s}'
            
        return encoded_str


    def decode(self, s: str) -> List[str]:
        res,i=[],0
        while i < len(s):
            j=i
            while s[j]!="#":
                j+=1
            leng=int(str(s[i:j]))
            
            word= s[j+1:j+1+leng]
            i=j+leng+1
            res.append(word)
        return res

            

        
     
        
        
