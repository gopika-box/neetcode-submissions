class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
     strs = sorted(strs)
     ang={}
     for i,st in enumerate(strs):
        b = "".join(sorted(st))
        if b in ang:
            ang[b].append(st)
        else: 
            ang[b]=[st]
     return list(ang.values())
     