class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq={}
        cur_sum=0
        ans,left=0,0
        for right in range(len(nums)):
            cur_sum+=nums[right]
            freq[nums[right]]=freq.get(nums[right],0)+1
            if right-left+1>k:
                cur_sum-=nums[left]
                freq[nums[left]]-=1
                if freq[nums[left]]==0:
                    del freq[nums[left]]
                left+=1
            if right-left+1==k and len(freq)==k:
                ans=max(ans,cur_sum)
        return ans


            



        