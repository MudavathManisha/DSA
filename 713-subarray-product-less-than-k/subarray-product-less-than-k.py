class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k<=1:
            return 0
        left=0
        count,cur_product=0,1
        for right in range(len(nums)):
            cur_product*=nums[right]
            while cur_product>=k:
                cur_product//=nums[left]
                left+=1
            count+=right-left+1
        return count
        



                

            
