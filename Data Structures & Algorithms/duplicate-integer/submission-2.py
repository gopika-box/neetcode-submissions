class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num1=[]
        for n in nums:
            if n not in num1:
                num1.append(n)
            else:
                return True
        return False

    