class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        diff = sum(nums) - x
        if diff == 0:
            return len(nums)
        max_len = -1
        l = 0
        sub_sum = 0
        
        for r in range(len(nums)):
            sub_sum += nums[r]
            while sub_sum > diff and l < r:
                sub_sum -= nums[l]
                l += 1
            if sub_sum == diff:
                max_len = max(max_len, (r-l+1))

        return -1 if max_len == -1 else len(nums) - max_len
