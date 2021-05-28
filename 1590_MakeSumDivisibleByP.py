class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        rmd = sum(nums) % p
        if rmd == 0:
            return 0

        subarray_sum_rmd_dict = {0:-1}
        subarray_rmd = 0
        length = len(nums)

        for i in range(len(nums)):
            subarray_rmd = (subarray_rmd + nums[i]) % p
            if (subarray_rmd - rmd) % p in subarray_sum_rmd_dict:
                if i - subarray_sum_rmd_dict[(subarray_rmd - rmd) % p] < length:
                    length = i - subarray_sum_rmd_dict[(subarray_rmd - rmd) % p]
            subarray_sum_rmd_dict[subarray_rmd] = i

        return -1 if length == len(nums) else length
