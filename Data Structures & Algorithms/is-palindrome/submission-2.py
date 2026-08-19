class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=re.sub(r'[^a-zA-Z0-9]','',s)
        s=s.lower()
        leng = len(s)
        for i in range(0,(leng//2)):
            if s[i]!=s[-i-1]:
                return False
            
        return True

        