class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left=0
        min_len=float('inf')
        s=0
        for right in range(len(nums)):
            s+=nums[right]
            while s>=target:
                
                min_len=min(min_len,right-left+1)
                s-=nums[left]
                left+=1
        if min_len==float('inf'):
            return 0
        return min_len
        

        