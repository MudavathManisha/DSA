class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq={0:1}
        count,cur_sum=0,0
        for i in range(len(nums)):
            cur_sum+=nums[i]
            prev_sum=cur_sum-k
            if prev_sum in freq:
                count+=freq[prev_sum]
            freq[cur_sum]=freq.get(cur_sum,0)+1
        return count