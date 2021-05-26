class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        elif len(nums) == 1:
            return 0 if nums[0] <= 0 else 1

        result, idx1, idx2, product = 0, 0, float('inf'), 1
        for i in range(len(nums)):
            if nums[i] == 0:
                idx1, idx2, product = i+1, float('inf'), 1
                continue

            product *= nums[i]
            if product > 0 :
                result = max(result, i-idx1+1)
            else:
                if idx2 == float('inf'):
                    idx2 = i+1
                else:
                    result = max(result, i-idx2+1)
        return result
