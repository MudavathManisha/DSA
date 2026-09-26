class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        s=sum(nums)
        n=len(nums)
        total=(n*(n+1))//2
        res=total-s
        return res

        