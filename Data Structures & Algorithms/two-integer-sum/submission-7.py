class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited={}
        for i in range(len(nums)):
            needed_value= target - nums[i]
            if needed_value not in visited:
                visited[nums[i]] = i
            else:
                return [visited[needed_value],i]
            
            



       
            
