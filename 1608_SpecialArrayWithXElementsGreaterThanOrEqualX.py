class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)+1):
            if i == sum([n >= i for n in nums]):
                return i
        return -1
