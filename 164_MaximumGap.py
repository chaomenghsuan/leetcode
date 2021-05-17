class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        else:
            nums.sort()
            result = nums[1] - nums[0]
            for i in range(2, len(nums)):
                result = max(result, nums[i]-nums[i-1])
            return result
