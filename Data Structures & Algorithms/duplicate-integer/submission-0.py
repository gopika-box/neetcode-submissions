class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newN=[]
        for n in nums:
            if n in newN:
                return True
            else:
                newN.append(n)
        return False

