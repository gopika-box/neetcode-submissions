class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=defaultdict(int)
        for n in nums:
            res[n] +=1
        sorted_Dict = dict(sorted(res.items(),key= lambda item: item[1], reverse=True))
        return [item[0] for item in list(sorted_Dict.items())[0:k]]

        