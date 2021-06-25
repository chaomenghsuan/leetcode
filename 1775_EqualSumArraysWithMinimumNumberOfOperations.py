class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) == len(nums2) == 1:
            return 1
        sum1, sum2 = sum(nums1), sum(nums2)
        if sum1 == sum2:
            return 0
        if sum2 < sum1:
            nums1, nums2 = nums2, nums1
            sum1, sum2 = sum2, sum1
        nums1.sort()
        nums2.sort(reverse=True)
        i = j = 0
        while sum1 < sum2:
            if i == len(nums1) and j == len(nums2):
                break
            if i < len(nums1) and j < len(nums2):
                if (6 - nums1[i]) >= (nums2[j] - 1):
                    sum1 += (6 - nums1[i])
                    i += 1
                else:
                    sum2 -= (nums2[j] - 1)
                    j += 1
            if i == len(nums1) and j < len(nums2):
                sum2 -= (nums2[j] - 1)
                j += 1
            if i < len(nums1) and j == len(nums2):
                sum1 += (6 - nums1[i])
                i += 1
        if sum1 >= sum2:
            return i+j
        else: return -1
