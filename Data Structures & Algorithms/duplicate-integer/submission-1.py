class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num1=[]
        for i in nums:
            if i not in num1:
                num1.append(i)
            else:
                return True   
        return False