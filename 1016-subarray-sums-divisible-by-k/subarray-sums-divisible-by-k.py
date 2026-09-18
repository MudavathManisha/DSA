class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        cur_sum=0
        rem_map={0:1}
        count=0
        for i in range(len(nums)):
            cur_sum+=nums[i]
            rem=cur_sum%k
            if rem in rem_map:
                count+=rem_map[rem]
            rem_map[rem]=rem_map.get(rem,0)+1
        return count

        