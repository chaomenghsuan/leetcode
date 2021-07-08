class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        accu = 0
        count = 0
        d = {0:1}
        for i in range(len(nums)):
            accu += nums[i]
            count += d.get(accu-k, 0)
            d[accu] = d.get(accu, 0) + 1
        return count
