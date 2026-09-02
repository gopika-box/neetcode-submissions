class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #optimized approach O(n)=>1 loop

        checked_list={}
        for i in range(0,len(nums)):
            needed_value= target - nums[i] #[0]=>3  7-3=4 ondo
            if needed_value in checked_list:
                return [checked_list[needed_value],i]
            else:
                checked_list[nums[i]] = i


            
