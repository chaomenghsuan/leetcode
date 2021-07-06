class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      """
      :type nums: List[int]
      :rtype: int
      """
      if not nums:
          return 0
      else:
          curmax = maxnum = nums[0]
          for i in range(1,len(nums)):
              curmax = max(nums[i], curmax+nums[i])
              maxnum = max(curmax, maxnum)
          return maxnum
