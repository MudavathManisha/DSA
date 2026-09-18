class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans=[]
        cur_prod=1
        #left product
        for i in range(len(nums)):
            ans.append(cur_prod)
            cur_prod*=nums[i]
        #right product
        cur_prod=1
        for i in range(len(nums)-1,-1,-1):
            ans[i]*=cur_prod
            cur_prod*=nums[i]
        return ans

        