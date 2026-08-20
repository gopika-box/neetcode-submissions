class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[1]*len(nums)
        pre=1
        post=1
        for i in range(len(nums)):
            j=len(nums)-1-i
            output[i]=output[i]*pre
            output[j]=output[j]*post
            pre*=nums[i]
            post*=nums[j]
            
        return output
            


        




    
            




        