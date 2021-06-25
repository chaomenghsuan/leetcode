class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = res = 0
        acc1 = acc2 = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                acc2 += nums2[j]
                j += 1
            elif nums1[i] < nums2[j]:
                acc1 += nums1[i]
                i += 1
            elif nums1[i] == nums2[j]:
                res += max(acc1, acc2)
                res += nums1[i]
                acc1 = acc2 = 0
                i += 1
                j += 1
        while i < len(nums1):
            acc1 += nums1[i]
            i += 1
        while j < len(nums2):
            acc2 += nums2[j]
            j += 1
        return (res + max(acc1, acc2)) % (10 ** 9 + 7)
