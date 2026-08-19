class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        feq = {}
        for i,num in enumerate(nums):
            if num in feq:
                feq[num]=feq[num]+1
            else:
                feq[num]=1
        sortli = sorted(feq.items(),key=lambda x:x[1] ,reverse=True)
        li= [x[0] for x in sortli[:k]]
        return li

        
