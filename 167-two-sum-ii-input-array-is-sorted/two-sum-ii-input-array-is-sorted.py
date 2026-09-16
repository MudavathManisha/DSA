class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n=len(nums)
        l,r=0,n-1
        while (l<r):
            sum_=nums[l]+nums[r]
            if sum_>target:
                r-=1
            elif sum_<target:
                l+=1
            else:
                return [l+1,r+1]
        
        
        
        