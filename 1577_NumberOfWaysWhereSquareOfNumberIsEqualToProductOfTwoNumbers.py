class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        d1, d2 = {}, {}
        for i in nums1:
            d1[i ** 2] = d1.get(i**2, 0) + 1
        for i in nums2:
            d2[i ** 2] = d2.get(i**2, 0) + 1
        
        res = 0
        
        for i in range(len(nums1)-1):
            for j in range(i+1, len(nums1)):
                if nums1[i] * nums1[j] in d2:
                    res += d2[nums1[i] * nums1[j]]
        
        for i in range(len(nums2)-1):
            for j in range(i+1, len(nums2)):
                if nums2[i] * nums2[j] in d1:
                    res += d1[nums2[i] * nums2[j]]
        
        return res
