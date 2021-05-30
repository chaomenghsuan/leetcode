class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        diff_count = {}
        res = 0
        acc = 0
        for i in range(len(nums)):
            acc += nums[i]
            if acc == goal:
                res += 1
            if acc-goal in diff_count:
                res += diff_count[acc-goal]
            if acc in diff_count:
                diff_count[acc] += 1
            else:
                diff_count[acc] = 1
        return res
