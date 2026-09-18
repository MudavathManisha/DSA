class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        total=sum(nums)
        cur_max=max_sum=nums[0]
        cur_min=min_sum=nums[0]
        for i in range(1,len(nums)):
            cur_max=max(nums[i],cur_max+nums[i])
            max_sum=max(cur_max,max_sum)
            cur_min=min(nums[i],cur_min+nums[i])
            min_sum=min(min_sum,cur_min)
        if max_sum<0:
            return max_sum
        circular_sum=total-min_sum
        return max(max_sum,circular_sum)
        


        