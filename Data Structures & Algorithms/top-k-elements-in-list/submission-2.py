class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for x in nums:
            if x not in dic:
                dic[x]=1
            else:
                dic[x]= dic[x]+1
        dic = sorted(dic.items(),key=lambda x:x[1],reverse=True)
        ans = [x[0] for x in dic[:k]]
        return ans

        
