from numpy import cumsum

class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        cumm = [0] + list(cumsum(nums))
        n = len(nums)
        res = 0

        l, st = [0], [[nums[0], 0]]
        for i in range(1, n):
            cur = 0
            while st and nums[i] <= st[-1][0]:
                cur += st.pop()[1] + 1
            st.append([nums[i], cur])
            l.append(cur)

        r, st = [0], [[nums[-1], 0]]
        for i in range(n-2, -1, -1):
            cur = 0
            while st and nums[i] <= st[-1][0]:
                cur += st.pop()[1] + 1
            st.append([nums[i], cur])
            r.append(cur)
        r.reverse()

        for i in range(n):
            res = max(res, nums[i]*(cumm[i + r[i] + 1] - cumm[i-l[i]]))

        return res % (10 ** 9 + 7)
