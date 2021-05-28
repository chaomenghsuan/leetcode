class Solution:
    def longestAwesome(self, s: str) -> int:
        res, mask = 0, 0
        seen = [-1] + [len(s)] * 2 ** 10
        for i in range(len(s)):
            mask ^= 1 << int(s[i])
            for a in range(10):
                res = max(res, i - seen[mask ^ (1 << a)])
            res = max(res, i - seen[mask])
            seen[mask] = min(seen[mask], i)
        return res
