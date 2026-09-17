class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        cur_sum=0
        rem_map = {0: -1}
        for i in range(len(nums)):
            cur_sum+=nums[i]
            rem=cur_sum%k
            if rem in rem_map:
                old_index=rem_map[rem]
                if i-old_index>=2:
                    return True
            else:
                rem_map[rem]=i
        return False

        