import string
class Solution:
    def isPalindrome(self, s: str) -> bool: 
        cleaned_text=s.lower().translate(str.maketrans('','',string.punctuation+ " "))
        length=len(cleaned_text)
        i,j=0,length-1
        while i<j:
            if(cleaned_text[i]!=cleaned_text[j]):
                return False
            i+=1
            j-=1
        return True
        print(cleaned_text)
        