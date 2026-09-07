import string
class Solution:
    def isPalindrome(self, s: str) -> bool: 
       cleaned_text=[c.lower() for c in s if c.isalnum()]
       print(cleaned_text)
       return cleaned_text == cleaned_text[::-1]

       
        