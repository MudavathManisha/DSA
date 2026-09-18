class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        cur_min=nums[0]
        cur_max=nums[0]
        max_prod=nums[0]
        
        
        
        for i in range(1,len(nums)):
            num=nums[i]
            old_max=cur_max
            old_min=cur_min
            
            cur_max=max(num,old_max*num,old_min*num)
            cur_min=min(num,old_max*num,old_min*num)
            max_prod=max(max_prod,cur_max)

        return max_prod
        