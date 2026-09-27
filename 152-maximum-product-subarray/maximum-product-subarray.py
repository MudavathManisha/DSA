class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        cur_max=nums[0]
        cur_min=nums[0]
        max_prod=nums[0]
        for i in range(1,len(nums)):
            num=nums[i]
            old_max=cur_max
            old_min=cur_min
            cur_max=max(num,old_max*num,old_min*num)
            cur_min=min(num,old_max*num,old_min*num)
            max_prod=max(cur_max,max_prod)
        return max_prod
        




        # cur_prod=1
        # max_prod=float('-inf')
        # for num in nums:
        #     cur_prod*=num
        #     max_prod=max(max_prod,cur_prod)
        # if cur_prod<0:
        #     cur_prod=0
        # return max_prod
            
        
        