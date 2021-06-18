class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i, n in enumerate(nums):
            while res and res[-1] > n and i < len(nums)-k+len(res):
                res.pop()
            if len(res) < k:
                res.append(n)
            
        return res
