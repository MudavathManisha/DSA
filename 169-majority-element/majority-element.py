class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n=len(nums)
        freq={}
        for nu in nums:
            freq[nu]=freq.get(nu,0)+1
            if freq[nu]>n/2:
                return nu
        